from mongoengine import Document, ObjectIdField, IntField, StringField, DateTimeField


# TODO: Add validations to all fields
class ReviewForProducerModel(Document):
    producerId = ObjectIdField()
    consumerId = ObjectIdField()
    rating = IntField()
    title = StringField()
    description = StringField()
    dateCreated = DateTimeField()
    dateUpdated = DateTimeField()

    meta = {
        "db_alias": "gkk",
        "collection": "reviewForProducer"
    }
