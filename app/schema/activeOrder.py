from datetime import date
from typing import List
import strawberry

from app.models.activeOrder import ActiveOrderModel
from app.schema.orderedFoodItem import OrderedFoodItem
from app.schema.consumer import Consumer, resolveConsumer
from app.schema.producer import Producer, resolveProducer


@strawberry.type
class ActiveOrder:
    id: strawberry.ID
    consumerId: strawberry.ID
    producerId: strawberry.ID
    orderedFoodItems: List[OrderedFoodItem]
    totalPrice: float
    status: str
    mealTime: str
    orderDueDatetime: date
    messageForProducer: str
    dateCreated: date
    dateUpdated: date

    @strawberry.field
    def consumer(self) -> Consumer:
        return resolveConsumer(id=self.consumerId)

    @strawberry.field
    def producer(self) -> Producer:
        return resolveProducer(id=self.producerId)


def resolveActiveOrder(id: strawberry.ID) -> ActiveOrder:
    activeOrder = ActiveOrderModel.objects(id=id).first()
    listOfOrderedFoodItems = []
    for orderedFoodItem in activeOrder.orderedFoodItems:
        listOfOrderedFoodItems.append( OrderedFoodItem( dietPreferences=orderedFoodItem.dietPreferences,
                                                        description=orderedFoodItem.description,
                                                        photo=orderedFoodItem.photo,
                                                        price=orderedFoodItem.price,
                                                        rating=orderedFoodItem.rating,
                                                        name=orderedFoodItem.name,
                                                        portionSize=orderedFoodItem.portionSize,
                                                        spiciness=orderedFoodItem.spiciness,
                                                        allergies=orderedFoodItem.allergies,
                                                        quantity=orderedFoodItem.quantity
                                                      )
                                     )

    return ActiveOrder( id=activeOrder.id,
                        consumerId=activeOrder.consumerId,
                        producerId=activeOrder.producerId,
                        orderedFoodItems=listOfOrderedFoodItems,
                        totalPrice=activeOrder.totalPrice,
                        status=activeOrder.status,
                        mealTime=activeOrder.mealTime,
                        orderDueDatetime=activeOrder.orderDueDatetime,
                        messageForProducer=activeOrder.messageForProducer,
                        dateCreated=activeOrder.dateCreated,
                        dateUpdated=activeOrder.dateUpdated
                      )

# @strawberry.field
# def resolveActiveOrders(producerId: strawberry.ID) -> ActiveOrder:
#     activeOrder = ActiveOrderModel.objects(id=id).first()
#     return ActiveOrder( id=activeOrder.id,
#                         consumerId=activeOrder.consumerId,
#                         producerId=activeOrder.producerId,
#                         items=activeOrder.items,
#                         totalPrice=activeOrder.totalPrice,
#                         status=activeOrder.status,
#                         mealTime=activeOrder.mealTime,
#                         orderDueDatetime=activeOrder.orderDueDatetime,
#                         messageForProducer=activeOrder.messageForProducer,
#                         dateCreated=activeOrder.dateCreated,
#                         dateUpdated=activeOrder.dateUpdated
#                       )