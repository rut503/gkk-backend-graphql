from datetime import date
import typing
import strawberry

from app.models.producer import ProducerModel
from app.schema.address import Address

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
    foodItems: typing.List[strawberry.ID]
    rating: int
    activeOrders: typing.List[strawberry.ID]
    dateCreated: date
    dateUpdated: date

def producerResolver(id: strawberry.ID) -> Producer:
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
            foodItems=producer.foodItems,
            rating=producer.rating,
            activeOrders=producer.activeOrders,
            dateCreated=producer.dateCreated,
            dateUpdated=producer.dateUpdated
        )