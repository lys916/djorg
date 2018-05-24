
from django.urls import path
from . import views

urlpatterns = [
	path('', views.bookmarksIndex, name='index')
]

print('xx bookmarks urls.py')