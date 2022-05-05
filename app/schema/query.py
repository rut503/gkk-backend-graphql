from typing import List
import strawberry

from app.schema.producer import Producer, producerResolver
from app.schema.reviewsForProducer import ReviewForProducer, reviewsForProducerResolver
from app.schema.reviewsForFoodItem import ReviewForFoodItem, reviewsForFoodItemResolver


@strawberry.type
class Query:
    producer: Producer = strawberry.field(resolver=producerResolver)
    reviewsForProducer: List[ReviewForProducer] = strawberry.field(resolver=reviewsForProducerResolver)
    reviewsForFoodItem: List[ReviewForFoodItem] = strawberry.field(resolver=reviewsForFoodItemResolver)