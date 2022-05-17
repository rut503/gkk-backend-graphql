from mongoengine import EmbeddedDocument, StringField


# TODO: Add validations to all fields
class Address(EmbeddedDocument):
    street = StringField()
    city = StringField()
    state = StringField() # TODO: Make this Enum Field
    zipCode = StringField()