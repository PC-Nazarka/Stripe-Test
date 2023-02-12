from apps.purchases.factories import ItemFactory

COUNT_ITEMS = 3


def run():
    """Generate example data."""
    ItemFactory.create_batch(size=COUNT_ITEMS)
