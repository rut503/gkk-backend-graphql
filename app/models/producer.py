from mongoengine import Document, StringField, EmbeddedDocumentField, ListField, IntField, ObjectIdField, DateTimeField

from app.models.address import Address

class ProducerModel(Document):
    firstName = StringField()
    lastName = StringField()
    phoneNumber = StringField()
    email = StringField()
    photo = StringField()
    bio = StringField()
    address = EmbeddedDocumentField(Address)
    foodItemIds = ListField(ObjectIdField())
    rating = IntField()
    activeOrderIds = ListField(ObjectIdField())
    dateCreated = DateTimeField()
    dateUpdated = DateTimeField()

    meta = {
        "db_alias": "gkk",
        "collection": "producer"
    }