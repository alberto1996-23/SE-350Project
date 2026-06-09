from backend.src.factory.breakfast_factory import BreakfastFactory
from backend.src.factory.lunch_factory import LunchFactory
from backend.src.factory.dinner_factory import DinnerFactory
from backend.src.factory.dessert_factory import DessertFactory
from backend.src.menu_item import MenuItem

def test_breakfast_factory_creates_breakfast_items():
    """I use this to confirm the breakfast factory returns breakfast menu items."""
    factory = BreakfastFactory()
    items = factory.create_items()

    assert len(items) > 0
    assert all(isinstance(item, MenuItem) for item in items)
    assert all(item.category == "Breakfast" for item in items)

def test_lunch_factory_creates_lunch_items():
    """I use this to confirm the lunch factory returns lunch menu items."""
    factory = LunchFactory()
    items = factory.create_items()

    assert len(items) > 0
    assert all(item.category == "Lunch" for item in items)