from mongoengine import Document, StringField, URLField, EmailField, EmbeddedDocumentField, ListField, IntField, ObjectIdField, DateTimeField

from app.models.address import Address


# TODO: Add validations to all fields
class ProducerModel(Document):
    firstName = StringField()
    lastName = StringField()
    phoneNumber = StringField()
    email = EmailField()
    photo = URLField()
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
