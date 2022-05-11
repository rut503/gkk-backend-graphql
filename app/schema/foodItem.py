from datetime import date
from typing import List
import strawberry

from app.models.foodItem import FoodItemModel


@strawberry.type
class FoodItem:
    id: strawberry.ID
    producerId: strawberry.ID
    dietPreferences: List[str]
    description: str
    photo: str
    price: float
    rating: int
    name: str
    portionSize: float
    spiciness: int
    allergies: List[str]
    dateCreated: date
    dateUpdated: date

def resolveFoodItem(id: strawberry.ID) -> FoodItem:
    foodItem = FoodItemModel.objects(id=id).first()
    return FoodItem( id=foodItem.id,
                     producerId=foodItem.producerId,
                     dietPreferences=foodItem.dietPreferences,
                     description=foodItem.description,
                     photo=foodItem.photo,
                     price=foodItem.price,
                     rating=foodItem.rating,
                     name=foodItem.name,
                     portionSize=foodItem.portionSize,
                     spiciness=foodItem.spiciness,
                     allergies=foodItem.allergies,
                     dateCreated=foodItem.dateCreated,
                     dateUpdated=foodItem.dateUpdated
                   )

def resolveFoodItems(producerId: strawberry.ID) -> List[FoodItem]:
    foodItems = FoodItemModel.objects(producerId=producerId)
    listOfFoodItems = []
    for foodItem in foodItems:
        listOfFoodItems.append( FoodItem( id=foodItem.id,
                                          producerId=foodItem.producerId,
                                          dietPreferences=foodItem.dietPreferences,
                                          description=foodItem.description,
                                          photo=foodItem.photo,
                                          price=foodItem.price,
                                          rating=foodItem.rating,
                                          name=foodItem.name,
                                          portionSize=foodItem.portionSize,
                                          spiciness=foodItem.spiciness,
                                          allergies=foodItem.allergies,
                                          dateCreated=foodItem.dateCreated,
                                          dateUpdated=foodItem.dateUpdated
                                        )
                              )
    return listOfFoodItems