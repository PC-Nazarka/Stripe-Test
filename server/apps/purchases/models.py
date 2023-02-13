from django.db import models


class Item(models.Model):
    name = models.CharField(
        max_length=128,
        verbose_name="Название товара",
    )
    description = models.TextField(
        verbose_name="Описание товара",
    )
    price = models.PositiveIntegerField(
        verbose_name="Цена товара",
    )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Order(models.Model):
    items = models.ManyToManyField(
        Item,
        verbose_name="Товары заказа"
    )

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
