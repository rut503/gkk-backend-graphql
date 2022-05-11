from datetime import date
from typing import List
import strawberry

from app.models.reviewForProducer import ReviewForProducerModel
from app.schema.consumer import Consumer, resolveConsumer

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

    @strawberry.field
    def consumer(self) -> Consumer:
        return resolveConsumer(id=self.consumerId)

def resolveReviewForProducer(id: strawberry.ID) -> ReviewForProducer:
    review = ReviewForProducerModel.objects(id=id).first()
    return ReviewForProducer(id=review.id,
                             producerId=review.producerId,
                             consumerId=review.consumerId,
                             rating=review.rating,
                             title=review.title,
                             description=review.description,
                             dateCreated=review.dateCreated,
                             dateUpdated=review.dateUpdated,
                            )

def resolveReviewsForProducer(producerId: strawberry.ID) -> List[ReviewForProducer]:
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