from mongoengine import Document, IntField, StringField, EmailField, URLField, DateTimeField, ObjectIdField, EmbeddedDocumentField, ListField

from app.models.address import Address


# TODO: Add validations to all fields
class ConsumerModel(Document):
    firstName = StringField()
    lastName = StringField()
    phoneNumber = StringField()
    email = EmailField()
    photo = URLField()
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