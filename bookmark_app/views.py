from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect

from .forms import BookmarkForm
from .models import Bookmark

# Create your views here.

# View for all public bookmarks
def bookmark_list(request):
	#bookmarks : query public bookmark
	bookmarks = Bookmark.public.all()
	#store in context dictionary
	context = {'bookmarks': bookmarks}
	#generate view
	return render(request, 'bookmark_app/bookmark_list.html', context)

#View for specific public user's bookmarks
def bookmark_user(request, username):
	#if user not found in DB => 404 error
	user = get_object_or_404(User, username=username)
	if request.user == user:
		bookmarks = user.bookmarks.all()
	else:
		bookmarks = Bookmark.public.filter(owner__username=username)
	context = {'bookmarks': bookmarks, 'owner': user}
	return render(request, 'bookmark_app/bookmark_user.html', context)

@login_required
def bookmark_create(request):
	if request.method == 'POST':
		form = BookmarkForm(data=request.POST)
		if form.is_valid():
			bookmark = form.save(commit=False)
			bookmark.owner = request.user
			bookmark.save()
			form.save_m2m()
			return redirect('bookmark_manager_user',
				username=request.user.username)
	else:
		form = BookmarkForm()
	context = {'form': form, 'create': True}
	return render(request, 'bookmark_app/form.html', context)

@login_required
def bookmark_edit(request, pk):
	bookmark = get_object_or_404(Bookmark, pk=pk)
	if bookmark.owner != request.user and not request.user.is_superuser:
		raise PermissionDenied
	if request.method == 'POST':
		form = BookmarkForm(instance=bookmark, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('bookmark_manager_user', username=request.user.username)
	else:
		form = BookmarkForm(instance=bookmark)
	context = {'form': form, 'create': False}
	return render(request, 'bookmark_app/form.html', context)


