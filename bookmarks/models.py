from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

class Bookmark(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
	url = models.URLField('URL', unique=True)
	name = models.CharField(max_length=200)
	notes = models.TextField(blank=True)

class PersonalBookmark(Bookmark):
	user = models.ForeignKey(User, on_delete=models.CASCADE)