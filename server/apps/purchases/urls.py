from django.urls import path

from . import views

app_name = "items"
urlpatterns = [
    path("item/<int:pk>/", views.DetailItem.as_view(), name="detail-item"),
    path("buy/item/<int:pk>/", views.BuyItem.as_view(), name="buy-item"),
    path("order/<int:pk>/", views.DetailOrder.as_view(), name="detail-order"),
    path("buy/order/<int:pk>/", views.BuyOrder.as_view(), name="buy-order"),
]
