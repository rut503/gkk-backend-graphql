from datetime import date
from typing import List
import strawberry

from app.models.reviewForConsumer import ReviewForConsumerModel
from app.schema.producer import Producer, resolveProducer


# TODO: Add validations to all fields
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

    @strawberry.field
    def producer(self) -> Producer:
        return resolveProducer(id=self.producerId)

def resolveReviewForConsumer(id: strawberry.ID) -> ReviewForConsumer:
    review = ReviewForConsumerModel.objects(id=id).first()
    return ReviewForConsumer( id=review.id,
                              consumerId=review.consumerId,
                              producerId=review.producerId,
                              rating=review.rating,
                              title=review.title,
                              description=review.description,
                              dateCreated=review.dateCreated,
                              dateUpdated=review.dateUpdated
                            )

def resolveReviewsForConsumer(consumerId: strawberry.ID) -> List[ReviewForConsumer]:
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