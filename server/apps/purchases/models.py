from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models


class Item(models.Model):
    name = models.CharField(
        max_length=128,
        verbose_name="Название объекта",
    )
    description = models.TextField(
        verbose_name="Описание объекта",
    )
    price = models.PositiveIntegerField(
        verbose_name="Цена объекта",
    )

    class Meta:
        verbose_name = "Объект"
        verbose_name_plural = "Объекты"
