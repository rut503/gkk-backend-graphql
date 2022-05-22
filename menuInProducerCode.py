# from datetime import date
# import typing
# import strawberry
# from fastapi import FastAPI
# from strawberry.fastapi import GraphQLRouter
# from mongoengine import *

# connect(alias="", host="")

# class ProducerModel(Document):
#     first_name = StringField()
#     last_name = StringField()
#     phone_number = StringField()
#     email_address = StringField()
#     photo = StringField()
#     bio = StringField()
#     address = DictField()
#     food_items = ListField(ObjectIdField())
#     rating = IntField()
#     active_orders = ListField(ObjectIdField())
#     menu = DictField()
#     date_created = DateTimeField()
#     date_updated = DateTimeField()

#     meta = {
#         "db_alias": "gkk",
#         "collection": "producer"
#     }

# @strawberry.type
# class Address:
#     street: str
#     city: str
#     state: str
#     zip_code: str

# @strawberry.type
# class Day:
#     breakfast: typing.List[strawberry.ID]
#     lunch: typing.List[strawberry.ID]
#     dinner: typing.List[strawberry.ID]

# @strawberry.type
# class Menu:
#     sunday: Day
#     monday: Day
#     tuesday: Day
#     wednesday: Day
#     thursday: Day
#     friday: Day
#     saturday: Day

# @strawberry.type
# class Producer:
#     id: strawberry.ID
#     first_name: str
#     last_name: str
#     phone_number: str
#     email_address: str
#     photo: str
#     bio: str
#     address: Address
#     food_items: typing.List[strawberry.ID]
#     rating: int
#     active_orders: typing.List[strawberry.ID]
#     menu: Menu
#     date_created: date
#     date_updated: date

# @strawberry.type
# class Query:
#     @strawberry.field
#     def producer(self, id: strawberry.ID) -> Producer:
#         producer = ProducerModel.objects(id=id)[0]

#         address = Address( street=producer.address["street"],
#                            city=producer.address["city"],
#                            state=producer.address["state"],
#                            zip_code=producer.address["zip_code"] )
#         menu = Menu( sunday=Day(breakfast=producer.menu["sunday"]["breakfast"],lunch=producer.menu["sunday"]["lunch"],dinner=producer.menu["sunday"]["dinner"]),
#                      monday=Day(breakfast=producer.menu["monday"]["breakfast"],lunch=producer.menu["monday"]["lunch"],dinner=producer.menu["monday"]["dinner"]),
#                      tuesday=Day(breakfast=producer.menu["tuesday"]["breakfast"],lunch=producer.menu["tuesday"]["lunch"],dinner=producer.menu["tuesday"]["dinner"]),
#                      wednesday=Day(breakfast=producer.menu["wednesday"]["breakfast"],lunch=producer.menu["wednesday"]["lunch"],dinner=producer.menu["wednesday"]["dinner"]),
#                      thursday=Day(breakfast=producer.menu["thursday"]["breakfast"],lunch=producer.menu["thursday"]["lunch"],dinner=producer.menu["thursday"]["dinner"]),
#                      friday=Day(breakfast=producer.menu["friday"]["breakfast"],lunch=producer.menu["friday"]["lunch"],dinner=producer.menu["friday"]["dinner"]),
#                      saturday=Day(breakfast=producer.menu["saturday"]["breakfast"],lunch=producer.menu["saturday"]["lunch"],dinner=producer.menu["saturday"]["dinner"])
#                    )

#         return Producer(
#             id=producer.id,
#             first_name=producer.first_name,
#             last_name=producer.last_name,
#             phone_number=producer.phone_number,
#             email_address=producer.email_address,
#             photo=producer.photo,
#             bio=producer.bio,
#             address=address,
#             food_items=producer.food_items,
#             rating=producer.rating,
#             active_orders=producer.active_orders,
#             menu=menu,
#             date_created=producer.date_created,
#             date_updated=producer.date_updated
#         )

# @strawberry.type
# class Mutation:
#     @strawberry.mutation
#     def create_flavour(self, name: str) -> bool:
#         print(name)
#         return True


# schema = strawberry.Schema(Query, Mutation)
# graphql_router = GraphQLRouter(schema)
# app = FastAPI()
# app.include_router(graphql_router, prefix="/graphql")
