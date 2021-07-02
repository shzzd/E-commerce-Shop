from django.contrib import admin
from .models import Products, Offer, NewProducts


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class NewProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


# Register your models here.
admin.site.register(NewProducts, NewProductAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(Products, ProductAdmin)
