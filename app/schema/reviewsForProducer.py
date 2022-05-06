from datetime import date
from typing import List
import strawberry
from app.models.reviewForProducer import ReviewForProducerModel

@strawberry.type
class ReviewForProducer:
    id: strawberry.ID
    producerId: strawberry.ID
    consumerId: strawberry.ID
    rating: int
    title: str
    description: str
    dateCreated: date
    dateUpdated: date

def allReviewsForProducerResolver(producerId: strawberry.ID) -> List[ReviewForProducer]:
    reviews = ReviewForProducerModel.objects(producerId=producerId)
    listOfReviews = []
    for review in reviews:
        listOfReviews.append( ReviewForProducer(id=review.id,
                                                producerId=review.producerId,
                                                consumerId=review.consumerId,
                                                rating=review.rating,
                                                title=review.title,
                                                description=review.description,
                                                dateCreated=review.dateCreated,
                                                dateUpdated=review.dateUpdated
                                               )
                            )
    return listOfReviews