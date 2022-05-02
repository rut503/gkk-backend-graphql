import strawberry

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello Rutvik"

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_flavour(self, name: str) -> bool:
        print(name)
        return True


schema = strawberry.Schema(Query, Mutation)
graphql_router = GraphQLRouter(schema)
app = FastAPI()
app.include_router(graphql_router, prefix="/graphql")