from django.conf import settings
from django_mako_plus import view_function, jscontext
from catalog import models as cmod
from django import forms
from formlib.form import Formless
from django.http import HttpResponseRedirect
from django.forms.models import model_to_dict



@view_function
def process_request(request):

    if not request.user.has_perm('auth.manager_view'):
        return HttpResponseRedirect('/homepage/index')
		
    form = CreateProductForm(request)

    if form.is_valid():
        form.commit()
        return HttpResponseRedirect('/manager/ProductList')

#render the format
    context = {
        'form': form,

    }
    return request.dmp.render('createProduct.html',context)


class CreateProductForm(Formless):
    def init(self):

        self.fields['type'] = forms.ChoiceField( choices=cmod.Product.TYPE_CHOICES)
        self.fields['name'] = forms.CharField(label='Product Name', max_length=100)
        self.fields['description'] = forms.CharField(label='Description', max_length=100)
        self.fields['category'] = forms.ModelChoiceField(label='Category', queryset=cmod.Category.objects.all(), empty_label=None)
        self.fields['price'] = forms.DecimalField(label='Price', max_digits=5)
        self.fields['quantity'] = forms.IntegerField(label='Quantity', required=False)
        self.fields['quantity'].widget.attrs = {'class':'bulk'}
        self.fields['reorder_trigger'] = forms.IntegerField(label='Reorder Trigger', required=False)
        self.fields['reorder_trigger'].widget.attrs = {'class':'bulk'}
        self.fields['reorder_quantity'] = forms.IntegerField(label='Reorder Quantity', required=False)
        self.fields['reorder_quantity'].widget.attrs = {'class': 'bulk'}
        self.fields['pid'] = forms.CharField(label='Product Id', required=False)
        self.fields['max_rental_days'] = forms.IntegerField(label='Max Rental Days', required=False)
        self.fields['max_rental_days'].widget.attrs = {'class':'rental'}
        self.fields['retire_date'] = forms.DateField(label='Retire Date', required=False)
        self.fields['retire_date'].widget.attrs = {'class':'rental'}


    def clean_quantity(self):
        ptype = self.cleaned_data.get('type')
        quantity = self.cleaned_data.get('quantity')
        if ptype == 'BulkProduct':

            if quantity == None:
                raise forms.ValidationError("Must have a quantity")

            elif quantity <= 0:
                raise forms.ValidationError("Quantity must be greater than 0")

            return quantity

    def clean_reorder_trigger(self):
        ptype = self.cleaned_data.get('type')
        trigger = self.cleaned_data.get('reorder_trigger')
        if ptype == 'BulkProduct':

            if trigger == None:
                raise forms.ValidationError("Must have a reorder trigger")

            elif trigger <= 0:
                raise forms.ValidationError("Reorder trigger must be greater than 0")

            return trigger

    def clean_reorder_quantity(self):
        ptype = self.cleaned_data.get('type')
        trigger = self.cleaned_data.get('reorder_quantity')
        if ptype == 'BulkProduct':

            if trigger == None:
                raise forms.ValidationError("Must have a reorder quantity")

            elif trigger <= 0:
                raise forms.ValidationError("Reorder quantity must be greater than 0")

            return trigger

    def clean_pid(self):
        ptype = self.cleaned_data.get('type')
        pid = self.cleaned_data.get('pid')
        if ptype == 'RentalProduct' or ptype == 'IndividualProduct':

            if pid == "":
                raise forms.ValidationError("Must have a Product ID")

            return pid

    def clean_max_rental_days(self):
        ptype = self.cleaned_data.get('type')
        max_days = self.cleaned_data.get('max_rental_days')
        if ptype == 'RentalProduct':

            if max_days == None:
                raise forms.ValidationError("Must have a maximum rental days")

            elif max_days <= 0:
                raise forms.ValidationError("Max rental days must be greater than 0")

            return max_days

    def clean_retire_date(self):
        ptype = self.cleaned_data.get('type')
        retire = self.cleaned_data.get('retire_date')
        if ptype == 'RentalProduct':

            if retire == None:
                raise forms.ValidationError("Must have a retire date")


            return retire


    def commit(self):

        typ = self.cleaned_data.get('type')

        if typ == 'BulkProduct':
            prod = cmod.BulkProduct()

            prod.quantity = self.cleaned_data.get('quantity')
            prod.reorder_trigger = self.cleaned_data.get('reorder_trigger')
            prod.reorder_quantity = self.cleaned_data.get('reorder_quantity')
            prod.name = self.cleaned_data.get('name')
            prod.description = self.cleaned_data.get('description')
            prod.category = self.cleaned_data.get('category')
            prod.price = self.cleaned_data.get('price')
            prod.save()


        elif typ == 'IndividualProduct':
            prod = cmod.IndividualProduct()
            prod.pid = self.cleaned_data.get('pid')
            prod.name = self.cleaned_data.get('name')
            prod.description = self.cleaned_data.get('description')
            prod.category = self.cleaned_data.get('category')
            prod.price = self.cleaned_data.get('price')
            prod.save()

        elif typ == 'RentalProduct':
            prod = cmod.RentalProduct()
            prod.pid = self.cleaned_data.get('pid')
            prod.max_rental_days = self.cleaned_data.get('max_rental_days')
            prod.retire_date = self.cleaned_data.get('retire_date')
            prod.name = self.cleaned_data.get('name')
            prod.description = self.cleaned_data.get('description')
            prod.category = self.cleaned_data.get('category')
            prod.price = self.cleaned_data.get('price')
            prod.save()
