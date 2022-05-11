from mongoengine import EmbeddedDocument, StringField


class Address(EmbeddedDocument):
    street = StringField()
    city = StringField()
    state = StringField()
    zipCode = StringField()