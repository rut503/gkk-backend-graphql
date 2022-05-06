from mongoengine import Document, IntField, StringField, DateTimeField, ObjectIdField, DictField, ListField


class ConsumerModel(Document):
    firstName = StringField()
    lastName = StringField()
    phoneNumber = StringField()
    email = StringField()
    photo = StringField()
    bio = StringField()
    address = DictField()
    rating = IntField()
    activeOrders = ListField(ObjectIdField)
    dateCreated = DateTimeField()
    dateUpdated = DateTimeField()

    meta = {
        "db_alias": "gkk",
        "collection": "consumer"
    }