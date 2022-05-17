import strawberry


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_flavour(self, name: str) -> bool:
        print(name)
        return True