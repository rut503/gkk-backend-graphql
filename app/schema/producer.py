from datetime import date
from typing import List
import strawberry

from app.schema.address import Address
from app.models.producer import ProducerModel


@strawberry.type
class Producer:
    id: strawberry.ID
    firstName: str
    lastName: str
    phoneNumber: str
    email: str
    photo: str
    bio: str
    address: Address
    foodItemIds: List[strawberry.ID]
    rating: int
    activeOrderIds: List[strawberry.ID]
    dateCreated: date
    dateUpdated: date

def resolveProducer(id: strawberry.ID) -> Producer:
        producer = ProducerModel.objects(id=id).first()

        address = Address( street=producer.address["street"],
                           city=producer.address["city"],
                           state=producer.address["state"],
                           zipCode=producer.address["zipCode"] )
        
        return Producer(
            id=producer.id,
            firstName=producer.firstName,
            lastName=producer.lastName,
            phoneNumber=producer.phoneNumber,
            email=producer.email,
            photo=producer.photo,
            bio=producer.bio,
            address=address,
            foodItemIds=producer.foodItemIds,
            rating=producer.rating,
            activeOrderIds=producer.activeOrderIds,
            dateCreated=producer.dateCreated,
            dateUpdated=producer.dateUpdated
        )