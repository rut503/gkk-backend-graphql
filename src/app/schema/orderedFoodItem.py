from typing import List
import strawberry


# TODO: Add validations to all fields
@strawberry.type
class OrderedFoodItem:
    dietPreferences: List[str]  # TODO: Make this Enum Field
    description: str
    photo: str
    price: float
    rating: int
    name: str
    portionSize: float
    spiciness: int  # TODO: Make this Enum Field
    allergies: List[str]
    quantity: int
