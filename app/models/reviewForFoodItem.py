from mongoengine import Document, StringField, IntField, ObjectIdField, DateTimeField

class ReviewForFoodItemModel(Document):
    foodItemId = ObjectIdField()
    consumerId = ObjectIdField()
    rating = IntField()
    title = StringField()
    description = StringField()
    dateCreated = DateTimeField()
    dateUpdated = DateTimeField()
    
    meta = {
        "db_alias": "gkk",
        "collection": "reviewForFoodItem"
    }
