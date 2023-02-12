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


class BuyItem(View):

    def get(self, request, *args, **kwargs):
        scheme = "https" if request.is_secure() else "http"
        url = f'{scheme}://{request.get_host()}/'
        item = get_object_or_404(
            models.Item.objects.all(),
            pk=self.kwargs["pk"],
        )
        success_url = reverse(
            "items:detail",
            kwargs={
                "pk": self.kwargs["pk"],
            },
        )
        session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': item.name,
                            'description': item.description,
                        },
                        'unit_amount': item.price,
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=url + success_url,
        )
        return JsonResponse(
            {"id": session.id}
        )
