from datetime import date
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

def reviewsForFoodItemResolver(foodItemId: strawberry.ID):
    reviews = ReviewForFoodItemModel.objects(food_item_id=foodItemId)
    listOfReviews = []
    for review in reviews:
        listOfReviews.append(ReviewForFoodItem(
            id=review.id,
            foodItemId=review.food_item_id,
            consumerId=review.consumer_id,
            rating=review.rating,
            title=review.title,
            description=review.description,
            dateCreated=review.date_created,
            dateUpdated=review.date_updated
        ))
    return listOfReviews