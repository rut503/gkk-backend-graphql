from datetime import date
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

def reviewsForProducerResolver(producerId: strawberry.ID):
    reviews = ReviewForProducerModel.objects(producer_id=producerId)
    listOfReviews = []
    for review in reviews:
        listOfReviews.append( ReviewForProducer(id=review.id,
                                                producerId=review.producer_id,
                                                consumerId=review.consumer_id,
                                                rating=review.rating,
                                                title=review.title,
                                                description=review.description,
                                                dateCreated=review.date_created,
                                                dateUpdated=review.date_updated
                                               )
                            )
    return listOfReviews