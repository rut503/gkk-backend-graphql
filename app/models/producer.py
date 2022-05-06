from mongoengine import Document, StringField, DictField, ListField, IntField, ObjectIdField, DateTimeField


class ProducerModel(Document):
    firstName = StringField()
    lastName = StringField()
    phoneNumber = StringField()
    email = StringField()
    photo = StringField()
    bio = StringField()
    address = DictField()
    foodItems = ListField(ObjectIdField())
    rating = IntField()
    activeOrders = ListField(ObjectIdField())
    dateCreated = DateTimeField()
    dateUpdated = DateTimeField()

    meta = {
        "db_alias": "gkk",
        "collection": "producer"
    }