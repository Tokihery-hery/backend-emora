from django.contrib import admin

# Register your models here.
from .models import UsersEmora, ProductsEmora

admin.site.register([ProductsEmora, UsersEmora])
