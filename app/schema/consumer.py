from datetime import date
from typing import List
import strawberry

from app.models.consumer import ConsumerModel
from app.schema.address import Address


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
    activeOrderIds: List[strawberry.ID]
    dateCreated: date
    dateUpdated: date

def resolveConsumer(id: strawberry.ID) -> Consumer:
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
                    activeOrderIds=consumer.activeOrderIds,
                    dateCreated=consumer.dateCreated,
                    dateUpdated=consumer.dateUpdated
                   )