from typing import List
import strawberry

from app.schema.producer import Producer, resolveProducer
from app.schema.consumer import Consumer, resolveConsumer
from app.schema.foodItem import FoodItem, resolveFoodItem, resolveFoodItems
from app.schema.reviewForProducer import ReviewForProducer, resolveReviewForProducer, resolveReviewsForProducer
from app.schema.reviewForConsumer import ReviewForConsumer, resolveReviewForConsumer, resolveReviewsForConsumer
from app.schema.reviewForFoodItem import ReviewForFoodItem, resolveReviewForFoodItem, resolveReviewsForFoodItem
from app.schema.activeOrder import ActiveOrder, resolveActiveOrder, resolveActiveOrders


@strawberry.type
class Query:
    producer: Producer = strawberry.field(resolver=resolveProducer)

    consumer: Consumer = strawberry.field(resolver=resolveConsumer)
    
    foodItem: FoodItem = strawberry.field(resolver=resolveFoodItem)
    foodItems: List[FoodItem] = strawberry.field(resolver=resolveFoodItems)

    reviewForProducer: ReviewForProducer = strawberry.field(resolver=resolveReviewForProducer)
    reviewsForProducer: List[ReviewForProducer] = strawberry.field(resolver=resolveReviewsForProducer)
    
    reviewForConsumer: ReviewForConsumer = strawberry.field(resolver=resolveReviewForConsumer)
    reviewsForConsumer: List[ReviewForConsumer] = strawberry.field(resolver=resolveReviewsForConsumer)
    
    reviewForFoodItem: ReviewForFoodItem = strawberry.field(resolver=resolveReviewForFoodItem)
    reviewsForFoodItem: List[ReviewForFoodItem] = strawberry.field(resolver=resolveReviewsForFoodItem)

    activeOrder: ActiveOrder = strawberry.field(resolver=resolveActiveOrder)
    activeOrders: List[ActiveOrder] = strawberry.field(resolver=resolveActiveOrders)
