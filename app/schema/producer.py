from datetime import date
import typing
import strawberry

from app.models.producer import ProducerModel


@strawberry.type
class Address:
    street: str
    city: str
    state: str
    zip_code: str

@strawberry.type
class Producer:
    id: strawberry.ID
    first_name: str
    last_name: str
    phone_number: str
    email_address: str
    photo: str
    bio: str
    address: Address
    food_items: typing.List[strawberry.ID]
    rating: int
    active_orders: typing.List[strawberry.ID]
    date_created: date
    date_updated: date

def producerResolver(id: strawberry.ID) -> Producer:
        producer = ProducerModel.objects(id=id)[0]

        address = Address( street=producer.address["street"],
                           city=producer.address["city"],
                           state=producer.address["state"],
                           zip_code=producer.address["zip_code"] )
        
        return Producer(
            id=producer.id,
            first_name=producer.first_name,
            last_name=producer.last_name,
            phone_number=producer.phone_number,
            email_address=producer.email_address,
            photo=producer.photo,
            bio=producer.bio,
            address=address,
            food_items=producer.food_items,
            rating=producer.rating,
            active_orders=producer.active_orders,
            date_created=producer.date_created,
            date_updated=producer.date_updated
        )