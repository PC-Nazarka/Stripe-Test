from django.contrib import admin

from apps.purchases.models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "description",
        "price",
    )
    list_filter = (
        "name",
        "description",
        "price",
    )
