from factory import Faker, django

from apps.purchases.models import Item


class ItemFactory(django.DjangoModelFactory):
    name = Faker(
        "pystr",
        min_chars=5,
        max_chars=10,
    )
    description = Faker(
        "pystr",
        min_chars=10,
        max_chars=20,
    )
    price = Faker(
        "pyint",
    )

    class Meta:
        model = Item
        django_get_or_create = ["name"]
