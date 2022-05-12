from mongoengine import EmbeddedDocument, StringField, URLField, ListField, FloatField, IntField


# TODO: Add validations to all fields
class OrderedFoodItemModel(EmbeddedDocument):
    dietPreferences = ListField(StringField()) # TODO: Make this Enum Field
    description = StringField()
    photo = URLField()
    price = FloatField()
    rating = IntField()
    name = StringField()
    portionSize = FloatField()
    spiciness = IntField() # TODO: Make this Enum Field
    allergies = ListField(StringField())
    quantity = IntField()
