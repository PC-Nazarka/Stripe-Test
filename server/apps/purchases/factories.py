from factory import Faker, django, post_generation

from apps.purchases.models import Item, Order

COUNT_ITEMS = 5


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


class OrderFactory(django.DjangoModelFactory):

    @post_generation
    def items(self, create, extracted, **kwargs):
        if not create:
            return
        items = extracted if extracted is not None else (
            ItemFactory() for _ in range(COUNT_ITEMS)
        )
        self.items.add(*items)

    class Meta:
        model = Order
