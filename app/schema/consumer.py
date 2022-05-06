from datetime import date
from typing import List
import strawberry

from app.schema.address import Address
from app.models.consumer import ConsumerModel


@strawberry.type
class Consumer:
    id: strawberry.ID
    firstName: str
    lastName: str
    phoneNumber: str
    email: str
    photo: str
    bio: str
    address: Address
    rating: int
    activeOrders: List[strawberry.ID]
    dateCreated: date
    dateUpdated: date

def consumerResolver(id: strawberry.ID) -> Consumer:
    consumer = ConsumerModel.objects(id=id).first()

    address = Address(street=consumer.address["street"],
                      city=consumer.address["city"],
                      state=consumer.address["state"],
                      zipCode=consumer.address["zipCode"],
                     )
    
    return Consumer(id=consumer.id,
                    firstName=consumer.firstName,
                    lastName=consumer.lastName,
                    phoneNumber=consumer.phoneNumber,
                    email=consumer.email,
                    photo=consumer.photo,
                    bio=consumer.bio,
                    address=address,
                    rating=consumer.rating,
                    activeOrders=consumer.activeOrders,
                    dateCreated=consumer.dateCreated,
                    dateUpdated=consumer.dateUpdated
                   )