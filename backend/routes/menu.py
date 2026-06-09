# This file should expose the menu to React.

# It should:

# read the menu from repository.py
# convert your MenuItem objects into JSON-safe dictionaries / schema objects
# return grouped menu data for the frontend

# This route should probably back:

# GET /api/menu
from fastapi import APIRouter

from backend.repository import get_menu
from backend.schemas import MenuCategoryResponse, MenuItemResponse


router = APIRouter(prefix="/api/menu", tags=["menu"])


@router.get("", response_model=list[MenuCategoryResponse])
def read_menu() -> list[MenuCategoryResponse]:
    """I use this to turn the menu object into grouped API data for React."""
    menu = get_menu()
    categories_response: list[MenuCategoryResponse] = []

    for category in menu.get_categories():
        menu_items = menu.get_items_by_category(category)

        item_responses: list[MenuItemResponse] = []

        for item in menu_items:
            item_responses.append(
                MenuItemResponse(
                    name=item.name,
                    description=item.description,
                    category=item.category,
                    price=item.get_price(),
                )
            )

        categories_response.append(
            MenuCategoryResponse(
                category=category,
                items=item_responses,
            )
        )

    return categories_response