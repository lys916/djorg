from rest_framework import serializers
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
	queryset = Note.objects.all()