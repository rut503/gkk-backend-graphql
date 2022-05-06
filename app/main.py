import os
from dotenv import load_dotenv
import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from mongoengine import *

from app.schema.query import Query
from app.schema.mutation import Mutation

load_dotenv()
MONGODB_URL = os.getenv('MONGODB_URL')
connect(alias="gkk", host=MONGODB_URL)

schema = strawberry.Schema(Query, Mutation)
graphql_router = GraphQLRouter(schema)
app = FastAPI()
app.include_router(graphql_router, prefix="/graphql")