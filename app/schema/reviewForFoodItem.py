from datetime import date
from typing import List
import strawberry

from app.models.reviewForFoodItem import ReviewForFoodItemModel
from app.schema.consumer import Consumer, resolveConsumer


# TODO: Add validations to all fields
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

    @strawberry.field
    def consumer(self) -> Consumer:
        return resolveConsumer(id=self.consumerId)


def resolveReviewForFoodItem(id: strawberry.ID) -> ReviewForFoodItem:
    review = ReviewForFoodItemModel.objects(id=id).first()
    return ReviewForFoodItem(
        id=review.id,
        foodItemId=review.foodItemId,
        consumerId=review.consumerId,
        rating=review.rating,
        title=review.title,
        description=review.description,
        dateCreated=review.dateCreated,
        dateUpdated=review.dateUpdated
    )


def resolveReviewsForFoodItem(foodItemId: strawberry.ID) -> List[ReviewForFoodItem]:
    reviews = ReviewForFoodItemModel.objects(foodItemId=foodItemId)
    listOfReviews = []
    for review in reviews:
        listOfReviews.append(
            ReviewForFoodItem(
                id=review.id,
                foodItemId=review.foodItemId,
                consumerId=review.consumerId,
                rating=review.rating,
                title=review.title,
                description=review.description,
                dateCreated=review.dateCreated,
                dateUpdated=review.dateUpdated
            )
        )
    return listOfReviews
