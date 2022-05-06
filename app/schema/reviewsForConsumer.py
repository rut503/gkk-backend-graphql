from datetime import date
from typing import List
import strawberry

from app.models.reviewForConsumer import ReviewForConsumerModel


@strawberry.type
class ReviewForConsumer:
    id: strawberry.ID
    consumerId: strawberry.ID
    producerId: strawberry.ID
    rating: int
    title: str
    description: str
    dateCreated: date
    dateUpdated: date

def allReviewsForConsumerResolver(consumerId: strawberry.ID) -> List[ReviewForConsumer]:
    reviews = ReviewForConsumerModel.objects(consumerId=consumerId)
    listOfReviews = []
    for review in reviews:
        listOfReviews.append( ReviewForConsumer( id=review.id,
                                                 consumerId=review.consumerId,
                                                 producerId=review.producerId,
                                                 rating=review.rating,
                                                 title=review.title,
                                                 description=review.description,
                                                 dateCreated=review.dateCreated,
                                                 dateUpdated=review.dateUpdated
                                               )
                            )
        return listOfReviews