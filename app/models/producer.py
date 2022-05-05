from mongoengine import Document, StringField, DictField, ListField, IntField, ObjectIdField, DateTimeField

class ProducerModel(Document):
    first_name = StringField()
    last_name = StringField()
    phone_number = StringField()
    email_address = StringField()
    photo = StringField()
    bio = StringField()
    address = DictField()
    food_items = ListField(ObjectIdField())
    rating = IntField()
    active_orders = ListField(ObjectIdField())
    menu = DictField()
    date_created = DateTimeField()
    date_updated = DateTimeField()

    meta = {
        "db_alias": "gkk",
        "collection": "producer"
    }