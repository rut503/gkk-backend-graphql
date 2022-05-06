from typing import List
import strawberry

from app.schema.consumer import Consumer, consumerResolver
from app.schema.producer import Producer, producerResolver
from app.schema.reviewsForConsumer import ReviewForConsumer, allReviewsForConsumerResolver
from app.schema.reviewsForProducer import ReviewForProducer, allReviewsForProducerResolver
from app.schema.reviewsForFoodItem import ReviewForFoodItem, allReviewsForFoodItemResolver


@strawberry.type
class Query:
    producer: Producer = strawberry.field(resolver=producerResolver)
    consumer: Consumer = strawberry.field(resolver=consumerResolver)
    allReviewsForProducer: List[ReviewForProducer] = strawberry.field(resolver=allReviewsForProducerResolver)
    allReviewsForFoodItem: List[ReviewForFoodItem] = strawberry.field(resolver=allReviewsForFoodItemResolver)
    allReviewsForConsumer: List[ReviewForConsumer] = strawberry.field(resolver=allReviewsForConsumerResolver)