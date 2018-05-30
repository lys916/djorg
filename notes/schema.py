from django.conf import settings
from graphene_django import DjangoObjectType
import graphene
from .models import Note as NoteModel

# this class will map or mirror database
# expose record schema
class Note(DjangoObjectType):
	class Meta:
		model = NoteModel

		# Tell what each record looks like
		interfaces = (graphene.relay.Node, )

# what field to expose in each document
class Query(graphene.ObjectType):
	# this connects to Note model
	notes = graphene.List(Note)

	def resole_notes(self, info):
		# grabbing user from info
		user = info.context.user
		# decide which notes to return
		if settings.DEBUG:
			return NoteModel.objects.all()
		if user.is_anonymous:
			return NoteModel.objects.none()
		else:
			return NoteModel.filter(user=user)

# Add a shema and attach the query
schema = graphene.Schema(query=Query)