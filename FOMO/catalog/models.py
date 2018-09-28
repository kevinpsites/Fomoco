from django.db import models, transaction
from django.conf import settings
from polymorphic.models import PolymorphicModel
from django.forms.models import model_to_dict
from decimal import Decimal
from datetime import datetime
from account import models as amod
import stripe



# Create your models here.
class Category(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    name = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Product(PolymorphicModel):

    TYPE_CHOICES = (
        ('BulkProduct', 'Bulk Product'),
        ('IndividualProduct', 'Individual Product'),
        ('RentalProduct', 'Rental Product'),
    )
    STATUS_CHOICES = (
        ('A', 'Active'),
        ('I', 'Inactive'),
    )

    create_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    status = models.TextField(choices=STATUS_CHOICES, default='A')
    name = models.TextField()
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def get_quantity(self):
        return 1

    def image_url(self):
        img = ProductImage.objects.filter(product=self.id).first()
        if img is None:
            url = settings.STATIC_URL + "/catalog/media/products/image_unavailable.gif"
        else:
            url = settings.STATIC_URL + "/catalog/media/products/" + img.filename
        return url

    def image_urls(self):
        img = ProductImage.objects.filter(product=self.id)
        if img is None:
            url =  ["image_unavailable.gif"]
        else:
            url = img
        return url


class BulkProduct(Product):
    '''A bulk Product'''
    TITLE = 'Bulk'
    quantity = models.IntegerField()
    reorder_trigger = models.IntegerField()
    reorder_quantity = models.IntegerField()

    def get_quantity(self):
        return self.quantity

class IndividualProduct(Product):
    TITLE = 'Individual'
    pid = models.TextField()

class RentalProduct(Product):
    '''A rental product (tracked individually)'''
    TITLE = 'Rental'
    pid = models.TextField()
    max_rental_days = models.IntegerField(default=0)
    retire_date = models.DateField(null=True, blank=True)


class ProductImage(models.Model):
    filename = models.TextField()
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name="images")
    create_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)




#Orders models



class Order(models.Model):
    '''An order in the system'''
    STATUS_CHOICES = (
        ( 'cart', 'Shopping Cart' ),
        ( 'payment', 'Payment Processing' ),
        ( 'sold', 'Finalized Sale' ),
    )
    order_date = models.DateTimeField(null=True, blank=True)
    name = models.TextField(blank=True, default="Shopping Cart")
    status = models.TextField(choices=STATUS_CHOICES, default='cart', db_index=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0) # max number is 999,999.99
    user = models.ForeignKey('account.User', related_name='orders',  on_delete=models.CASCADE)
    # shipping information
    ship_date = models.DateTimeField(null=True, blank=True)
    ship_tracking = models.TextField(null=True, blank=True)
    ship_name = models.TextField(null=True, blank=True)
    ship_address = models.TextField(null=True, blank=True)
    ship_city = models.TextField(null=True, blank=True)
    ship_state = models.TextField(null=True, blank=True)
    ship_zip_code = models.TextField(null=True, blank=True)

    def __str__(self):
        '''Prints for debugging purposes'''
        return 'Order {}: {}: {}'.format(self.id, self.user.get_full_name(), self.total_price)

        #I did this one DJ
    def active_items(self, include_tax_item=True):
        '''Returns the active items on this order'''
        # create a query object (filter to status='active')
        if include_tax_item:
            act = OrderItem.objects.filter(order=self, status='active')
        else:
            act = OrderItem.objects.filter(order=self, status='active').exclude(product__name='Sales Tax')
        return act


        # if we aren't including the tax item, alter the
        # query to exclude that OrderItem
        # I simply used the product name (not a great choice,
        # but it is acceptable for credit)


    def get_item(self, product, create=False):
        '''Returns the OrderItem object for the given product'''
        item = OrderItem.objects.filter(order=self, product=product).first()
        if item is None and create:
            item = OrderItem.objects.create(order=self, product=product, price=product.price, quantity=0)
        elif create and item.status != 'active':
            item.status = 'active'
            item.quantity = 0
        if item is not None:
            item.recalculate()
        item.recalculate()
        item.save()
        return item


    def num_items(self):
        '''Returns the number of items in the cart'''
        return sum(self.active_items(include_tax_item=False).values_list('quantity', flat=True))


    def recalculate(self):
        '''
        Recalculates the total price of the order,
        including recalculating the taxable amount.

        Saves this Order and all child OrderLine objects.
        '''
        # iterate the order items (not including tax item) and get the total price
        self.total_price = 0
        for i in self.active_items(include_tax_item=False):
            self.total_price = self.total_price + i.extended

            # call recalculate on each item
            i.recalculate()
        # update/create the tax order item (calculate at 7% rate)
        tax = OrderItem.objects.filter(order= self, product__name="Sales Tax",status="active").first()


        if tax is None:
            tax = self.get_item(Product.objects.filter(name='Sales Tax').first(), True)

        tax.price = self.total_price * Decimal(.07)
        if tax.quantity == 1:
            tax.recalculate(0)
        else:
            tax.recalculate(1)


        tax.save()
        # update the total and save
        self.total_price = self.total_price + tax.price
        self.save()




    def finalize(self, stripe_charge_token):
        '''Runs the payment and finalizes the sale'''
        with transaction.atomic():
            # recalculate just to be sure everything is updated
            self.recalculate()
            # check that all products are available
            cart = self.active_items(include_tax_item=False)

            for i in cart:
                if i.quantity > i.product.get_quantity():
                    raise ValueError("Sorry we don't have enough "  + i.product.name + "s to fill your order")
            # contact stripe and run the payment (using the stripe_charge_token)
            charge = stripe.Charge.create(
                 amount=int(self.total_price * 100),
                 currency="usd",
                 description="Example charge",
                 source=stripe_charge_token,
            )
            self.order_date= datetime.today()
            # finalize (or create) one or more payment objects
            payment, created = Payment.objects.get_or_create(order=self)
            payment.payment_date = datetime.now()
            payment.amount = self.total_price
            payment.validation_code= charge['id']
            payment.save()
            # set order status to sold and save the order
            self.status = 'sold'
            self.save()
            # update product quantities for BulkProducts
            for i in self.active_items(include_tax_item=False):
                if i.product.TITLE=='Bulk':
                    i.product.quantity -= i.quantity

                    # update status for IndividualProducts
                else:
                    i.product.status='I'

                i.product.save()
                i.save()

class OrderItem(PolymorphicModel):
    '''A line item on an order'''
    STATUS_CHOICES = (
        ( 'active', 'Active' ),
        ( 'deleted', 'Deleted' ),
    )
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    status = models.TextField(choices=STATUS_CHOICES, default='active', db_index=True)
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0) # max number is 999,999.99
    quantity = models.IntegerField(default=0)
    extended = models.DecimalField(max_digits=8, decimal_places=2, default=0) # max number is 999,999.99

    def __str__(self):
        '''Prints for debugging purposes'''
        return 'OrderItem {}: {}: {}'.format(self.id, self.product.name, self.extended)


    def recalculate(self,quant=0):
        '''Updates the order item's price, quantity, extended'''
        # update the price if it isn't already set and we have a product
        if self.product.name != "Sales Tax":
            self.price = self.product.price
        # default the quantity to 1 if we don't have a quantity set
        if self.quantity is None:
            self.quantity = 1
        self.quantity = self.quantity + quant
        # calculate the extended (price * quantity)
        self.extended = self.price * self.quantity
        # save the changes
        self.save()

class Payment(models.Model):
    '''A payment on a sale'''
    order = models.ForeignKey(Order, null=True, on_delete=models.CASCADE)
    payment_date = models.DateTimeField(null=True, blank=True)
    amount = models.DecimalField(blank=True, null=True, max_digits=8, decimal_places=2) # max number is 999,999.99
    validation_code = models.TextField(null=True, blank=True)
