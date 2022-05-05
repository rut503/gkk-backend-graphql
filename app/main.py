import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from mongoengine import *

from app.schema.query import Query
from app.schema.mutation import Mutation

connect(alias="gkk", host="mongodb+srv://rutvik:Onepassionate96@sandbox.wncx4.mongodb.net/gkk?retryWrites=true&w=majority")

schema = strawberry.Schema(Query, Mutation)
graphql_router = GraphQLRouter(schema)
app = FastAPI()
app.include_router(graphql_router, prefix="/graphql")