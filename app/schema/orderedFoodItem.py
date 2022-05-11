from typing import List
import strawberry


@strawberry.type
class OrderedFoodItem:
    dietPreferences: List[str]
    description: str
    photo: str
    price: float
    rating: int
    name: str
    portionSize: float
    spiciness: int
    allergies: List[str]
    quantity: int
