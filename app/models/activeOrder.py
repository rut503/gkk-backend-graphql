from mongoengine import Document, ObjectIdField, StringField, FloatField, DateTimeField, EmbeddedDocumentListField

from app.models.orderedFoodItem import OrderedFoodItemModel


# TODO: Add validations to all fields
class ActiveOrderModel(Document):
    consumerId = ObjectIdField()
    producerId = ObjectIdField()
    orderedFoodItems = EmbeddedDocumentListField(OrderedFoodItemModel)
    totalPrice = FloatField()
    status = StringField()  # TODO: Make this Enum Field
    mealTime = StringField()  # TODO: Make this Enum Field
    orderDueDatetime = DateTimeField()
    messageForProducer = StringField()
    dateCreated = DateTimeField()
    dateUpdated = DateTimeField()

    meta = {
        "db_alias": "gkk",
        "collection": "activeOrder",
    }
