from django.contrib import admin
from account import models as amod
from django.contrib.auth.models import Permission
# Register your models here.

admin.site.register(amod.User)
admin.site.register(Permission)