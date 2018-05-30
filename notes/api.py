from rest_framework import serializers, viewsets
from .models import Note

class NoteSerializer(serializers.HyperlinkedModelSerializer):
	def create(self, validated_data):
		user = self.context['request'].user
		note = Note.objects.create(user=user, **validated_data)
		return note
	#  which field we want from the record
	class Meta:
		model = Note
		fields = ('title', 'content')

#  which record we want
class NoteViewSet(viewsets.ModelViewSet):

	serializer_class = NoteSerializer
	# queryset attribute must exist in viewsets
	queryset = Note.objects.all()

	# get method.. when user hit api/notes url.. return notes
	def get_queryset(self):
		user = self.request.user

		if user.is_anonymous:
			return Note.objects.all()
			# return Note.objects.none()
		else:
			return Note.objects.filter(user=user)

		# print(self.request.method)