from datetime import date
from typing import List
import strawberry

from app.models.reviewForFoodItem import ReviewForFoodItemModel


@strawberry.type
class ReviewForFoodItem:
    id: strawberry.ID
    foodItemId: strawberry.ID
    consumerId: strawberry.ID
    rating: int
    title: str
    description: str
    dateCreated: date
    dateUpdated: date

def allReviewsForFoodItemResolver(foodItemId: strawberry.ID) -> List[ReviewForFoodItem]:
    reviews = ReviewForFoodItemModel.objects(foodItemId=foodItemId)
    listOfReviews = []
    for review in reviews:
        listOfReviews.append(ReviewForFoodItem(
            id=review.id,
            foodItemId=review.foodItemId,
            consumerId=review.consumerId,
            rating=review.rating,
            title=review.title,
            description=review.description,
            dateCreated=review.dateCreated,
            dateUpdated=review.dateUpdated
        ))
    return listOfReviews