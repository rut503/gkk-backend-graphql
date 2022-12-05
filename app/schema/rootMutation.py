from typing import List
from datetime import date, datetime
import strawberry

from app.models.address import Address
from app.models.consumer import ConsumerModel
from app.models.foodItem import FoodItemModel
from app.models.producer import ProducerModel
from app.models.reviewForProducer import ReviewForProducerModel
from app.models.reviewForConsumer import ReviewForConsumerModel
from app.models.reviewForFoodItem import ReviewForFoodItemModel

from app.schema.foodItem import FoodItem
from app.schema.producer import Producer
from app.schema.consumer import Consumer
from app.schema.reviewForConsumer import ReviewForConsumer
from app.schema.reviewForProducer import ReviewForProducer
from app.schema.reviewForFoodItem import ReviewForFoodItem


# TODO: Add validations to all fields
@strawberry.input
class AddressInput:
    street: str
    city: str
    state: str  # TODO: Make this Enum Field
    zipCode: str


@strawberry.input
class UserInput:
    firstName: str
    lastName: str
    phoneNumber: str
    email: str
    photo: str
    bio: str
    address: AddressInput


@strawberry.input
class FoodItemInput:
    producerId: strawberry.ID
    dietPreferences: List[str]  # TODO: Make this Enum Field
    description: str
    photo: str
    price: float
    name: str
    portionSize: float
    spiciness: int  # TODO: Make this Enum Field
    allergies: List[str]


@strawberry.input
class UserReviewInput:
    producerId: strawberry.ID
    consumerId: strawberry.ID
    rating: int
    title: str
    description: str

@strawberry.input
class FoodItemReviewInput:
    foodItemId: strawberry.ID
    consumerId: strawberry.ID
    rating: int
    title: str
    description: str

@strawberry.type
class Mutation:

    @strawberry.mutation
    def createProducer(self, userInput: UserInput) -> Producer:
        newAddress = Address(
            street=userInput.address.street,
            city=userInput.address.city,
            state=userInput.address.state,
            zipCode=userInput.address.zipCode,
        )
        newProducer = ProducerModel(
            firstName=userInput.firstName, 
            lastName=userInput.lastName, 
            phoneNumber=userInput.phoneNumber,
            email=userInput.email,
            photo=userInput.photo,
            bio=userInput.bio,
            address=newAddress,
            foodItemIds=[],
            rating=0,
            activeOrderIds=[],
            dateCreated=datetime.today(),
            dateUpdated=datetime.today()
        )
        newProducer.save()
        return newProducer

    @strawberry.mutation
    def createConsumer(self, userInput: UserInput) -> Consumer:
        newAddress = Address(
            street=userInput.address.street,
            city=userInput.address.city,
            state=userInput.address.state,
            zipCode=userInput.address.zipCode,
        )
        newConsumer = ConsumerModel(
            firstName=userInput.firstName, 
            lastName=userInput.lastName, 
            phoneNumber=userInput.phoneNumber,
            email=userInput.email,
            photo=userInput.photo,
            bio=userInput.bio,
            address=newAddress,
            rating=0,
            activeOrderIds=[],
            dateCreated=datetime.today(),
            dateUpdated=datetime.today()
        )
        newConsumer.save()
        return newConsumer

    @strawberry.mutation
    def createFoodItem(self, foodItemInput: FoodItemInput) -> FoodItem:
        newFoodItem = FoodItemModel(
            producerId=foodItemInput.producerId,
            dietPreferences=foodItemInput.dietPreferences,
            description=foodItemInput.description,
            photo=foodItemInput.photo,
            price=foodItemInput.price,
            rating=0,
            name=foodItemInput.name,
            portionSize=foodItemInput.portionSize,
            spiciness=foodItemInput.spiciness,
            allergies=foodItemInput.allergies,
            dateCreated=datetime.today(),
            dateUpdated=datetime.today(),
        )
        newFoodItem.save()
        return newFoodItem

    @strawberry.mutation
    def createReviewForProducer(self, userReviewInput: UserReviewInput) -> ReviewForProducer:
        newUserReview = ReviewForProducerModel(
            producerId=userReviewInput.producerId,
            consumerId=userReviewInput.consumerId,
            rating=userReviewInput.rating,
            title=userReviewInput.title,
            description=userReviewInput.description,
            dateCreated=datetime.today(),
            dateUpdated=datetime.today()
        )
        newUserReview.save()
        return newUserReview
    
    @strawberry.mutation
    def createReviewForConsumer(self, userReviewInput: UserReviewInput) -> ReviewForConsumer:
        newUserReview = ReviewForConsumerModel(
            consumerId=userReviewInput.consumerId,
            producerId=userReviewInput.producerId,
            rating=userReviewInput.rating,
            title=userReviewInput.title,
            description=userReviewInput.description,
            dateCreated=datetime.today(),
            dateUpdated=datetime.today()
        )
        newUserReview.save()
        return newUserReview

    @strawberry.mutation
    def createReviewForFoodItem(self, foodItemReviewInput: FoodItemReviewInput) -> ReviewForFoodItem:
        newFoodItemReview = ReviewForFoodItemModel(
            foodItemId=foodItemReviewInput.foodItemId,
            consumerId=foodItemReviewInput.consumerId,
            rating=foodItemReviewInput.rating,
            title=foodItemReviewInput.title,
            description=foodItemReviewInput.description,
            dateCreated=datetime.today(),
            dateUpdated=datetime.today()
        )
        newFoodItemReview.save()
        return newFoodItemReview
    
