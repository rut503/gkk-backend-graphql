import strawberry


# TODO: Add validations to all fields
@strawberry.type
class Address:
    street: str
    city: str
    state: str # TODO: Make this Enum Field
    zipCode: str