from mongoengine import Document, StringField, IntField, ObjectIdField, DateTimeField

class ReviewForFoodItemModel(Document):
    food_item_id = ObjectIdField()
    consumer_id = ObjectIdField()
    rating = IntField()
    title = StringField()
    description = StringField()
    date_created = DateTimeField()
    date_updated = DateTimeField()
    
    meta = {
        "db_alias": "gkk",
        "collection": "review_for_food_item"
    }
