from fastapi import FastAPI
import graphene
from starlette.graphql import GraphQLApp


#initiate the application.
app = FastAPI()

#create a query class for graphql
class Query(graphene.ObjectType):
	hello = graphene.String(name = graphene.String(default_value="hello There"))

	def resolve_test(self, info, name):
		return "hey there" + test

app.add_route("/", GraphQLApp(schema=graphene.Schema(query=Query)))



