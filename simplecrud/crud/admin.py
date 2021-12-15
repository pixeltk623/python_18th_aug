from django.contrib import admin

from .models import Person, Product
# Register your models here.


@admin.register(Person, Product)
class PersonProduct(admin.ModelAdmin):
    pass


