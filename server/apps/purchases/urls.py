from django.urls import path

from . import views

app_name = "items"
urlpatterns = [
    path("item/<int:pk>/", views.DetailItem.as_view(), name="detail"),
    path("buy/<int:pk>/", views.BuyItem.as_view(), name="buy"),
]
