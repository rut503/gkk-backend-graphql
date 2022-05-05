from mongoengine import Document, ObjectIdField, IntField, StringField, DateTimeField


class ReviewForProducerModel(Document):
    producer_id = ObjectIdField()
    consumer_id = ObjectIdField()
    rating = IntField()
    title = StringField()
    description = StringField()
    date_created = DateTimeField()
    date_updated = DateTimeField()

    meta = {
        "db_alias": "gkk",
        "collection": "review_for_producer"
    }