from mongoengine import EmbeddedDocument, StringField, ListField, FloatField, IntField


class OrderedFoodItemModel(EmbeddedDocument):
    dietPreferences = ListField(StringField())
    description = StringField()
    photo = StringField()
    price = FloatField()
    rating = IntField()
    name = StringField()
    portionSize = FloatField()
    spiciness = IntField()
    allergies = ListField(StringField())
    quantity = IntField()
