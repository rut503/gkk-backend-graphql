from mongoengine import Document, IntField, StringField, DateTimeField, ObjectIdField, ListField, FloatField


class FoodItemModel(Document):
    producerId = ObjectIdField()
    dietPreferences = ListField(StringField())
    description = StringField()
    photo = StringField()
    price = FloatField()
    rating = IntField()
    name = StringField()
    portionSize = FloatField()
    spiciness = IntField()
    allergies = ListField(StringField())
    dateCreated = DateTimeField()
    dateUpdated = DateTimeField()

    meta = {
        "db_alias": "gkk",
        "collection": "foodItem"
    }