from mongoengine import Document, IntField, StringField, URLField, DateTimeField, ObjectIdField, ListField, FloatField


# TODO: Add validations to all fields
class FoodItemModel(Document):
    producerId = ObjectIdField()
    dietPreferences = ListField(StringField()) # TODO: Make this Enum Field
    description = StringField()
    photo = URLField()
    price = FloatField()
    rating = IntField()
    name = StringField()
    portionSize = FloatField()
    spiciness = IntField() # TODO: Make this Enum Field
    allergies = ListField(StringField())
    dateCreated = DateTimeField()
    dateUpdated = DateTimeField()

    meta = {
        "db_alias": "gkk",
        "collection": "foodItem"
    }