from django.shortcuts import render
from .models import Bookmark, PersonalBookmark
# Create your views here.
def bookmarksIndex(request):
	# Bookmark is the model, it has method to do crude 
	# operation to bookmarks table
	bookmarksArray = Bookmark.objects.all()
	
	context = {
		'bookmarks': Bookmark.objects.all()
	}

	if request.user.is_anonymous:
		context['personalBookmarks'] = PersonalBookmark.objects.none()
	else:
		context['personalBookmarks'] = PersonalBookmark.objects.filter(user=request.user)


	return render(request, 'bookmarks/index.html', context)
