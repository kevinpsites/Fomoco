from django.contrib import admin
from catalog import models as cmod

# Register your models here.
admin.site.register(cmod.Product)
admin.site.register(cmod.BulkProduct)
admin.site.register(cmod.IndividualProduct)
admin.site.register(cmod.RentalProduct)
admin.site.register(cmod.Category)
admin.site.register(cmod.Order)
admin.site.register(cmod.OrderItem)
admin.site.register(cmod.Payment)
admin.site.register(cmod.ProductImage)
