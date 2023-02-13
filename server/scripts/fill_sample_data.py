from apps.purchases.factories import OrderFactory

COUNT_ORDERS = 3


def run():
    OrderFactory.create_batch(size=COUNT_ORDERS)
