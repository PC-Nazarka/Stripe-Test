import os

import stripe
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic.detail import DetailView

from . import models

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")


class DetailItem(DetailView):
    template_name = "item/detail_item.html"
    context_object_name = "item"
    queryset = models.Item.objects.all()


class DetailOrder(DetailView):
    template_name = "order/detail_order.html"
    context_object_name = "order"

    def get_object(self, queryset=None):
        return get_object_or_404(
            models.Order.objects.prefetch_related("items"),
            pk=self.kwargs["pk"]
        )


def format_item(item: models.Item, quantity: int = 1) -> dict:
    data = {
        'currency': 'usd',
        'product_data': {
            'name': item.name,
            'description': item.description,
        },
        'unit_amount_decimal': item.price,
    }
    return {
        "price_data": data,
        'quantity': quantity,
    }


class BuyItem(View):

    def get(self, request, *args, **kwargs):
        scheme = "https" if request.is_secure() else "http"
        host = f'{scheme}://{request.get_host()}/'
        item = get_object_or_404(
            models.Item,
            pk=self.kwargs["pk"],
        )
        success_url = reverse(
            "items:detail-item",
            kwargs={
                "pk": self.kwargs["pk"],
            },
        )
        session = stripe.checkout.Session.create(
            line_items=[
                format_item(item),
            ],
            mode='payment',
            success_url=host + success_url,
        )
        return JsonResponse({
            "id": session.id,
        })


class BuyOrder(View):

    def get(self, request, *args, **kwargs):
        scheme = "https" if request.is_secure() else "http"
        host = f'{scheme}://{request.get_host()}/'
        order = get_object_or_404(
            models.Order.objects.prefetch_related("items"),
            pk=self.kwargs["pk"],
        )
        success_url = reverse(
            "items:detail-order",
            kwargs={
                "pk": self.kwargs["pk"],
            },
        )
        session = stripe.checkout.Session.create(
            line_items=[
                format_item(order_item)
                for order_item in order.items.all()
            ],
            mode='payment',
            success_url=host + success_url,
        )
        return JsonResponse({
            "id": session.id,
        })
