import strawberry

@strawberry.type
class Address:
    street: str
    city: str
    state: str
    zipCode: str