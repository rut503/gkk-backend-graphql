from mongoengine import Document, IntField, StringField, DateTimeField, ObjectIdField, EmbeddedDocumentField, ListField

from app.models.address import Address


class ConsumerModel(Document):
    firstName = StringField()
    lastName = StringField()
    phoneNumber = StringField()
    email = StringField()
    photo = StringField()
    bio = StringField()
    address = EmbeddedDocumentField(Address)
    rating = IntField()
    activeOrderIds = ListField(ObjectIdField())
    dateCreated = DateTimeField()
    dateUpdated = DateTimeField()

    meta = {
        "db_alias": "gkk",
        "collection": "consumer"
    }