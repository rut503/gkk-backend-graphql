from mongoengine import Document, IntField, StringField, ObjectIdField, DateTimeField

class ReviewForConsumerModel(Document):
    consumerId = ObjectIdField()
    producerId = ObjectIdField()
    rating = IntField()
    title = StringField()
    description = StringField()
    dateCreated = DateTimeField()
    dateUpdated = DateTimeField()

    meta = {
        "db_alias": "gkk",
        "collection": "reviewForConsumer"
    }