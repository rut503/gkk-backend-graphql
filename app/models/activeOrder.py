from mongoengine import Document, ObjectIdField, StringField, FloatField, DateTimeField, EmbeddedDocumentListField

from app.models.orderedFoodItem import OrderedFoodItemModel


class ActiveOrderModel(Document):
    consumerId = ObjectIdField()
    producerId = ObjectIdField()
    orderedFoodItems = EmbeddedDocumentListField(OrderedFoodItemModel)
    totalPrice = FloatField()
    status = StringField()
    mealTime = StringField()
    orderDueDatetime = DateTimeField()
    messageForProducer = StringField()
    dateCreated = DateTimeField()
    dateUpdated = DateTimeField()

    meta = {
        "db_alias": "gkk",
        "collection": "activeOrder",
    }