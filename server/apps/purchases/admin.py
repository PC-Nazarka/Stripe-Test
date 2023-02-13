from django.contrib import admin

from apps.purchases.models import Item, Order


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "description",
        "price",
    )
    list_filter = (
        "name",
        "description",
        "price",
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        "id",
    )
