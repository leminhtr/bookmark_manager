from django.contrib import admin

from .models import Bookmark, Tag
# Register your models here.


class BookmarkAdmin(admin.ModelAdmin):
	#champ visible
	list_display = ('url', 'title', 'owner', 'is_public', 'date_updated')
	#champ modifiable
	list_editable = ('is_public',)
	#champ filtrable (par requete bdd)
	list_filter =('is_public', 'owner__username')
	#champ recherchable
	search_fields =['url', 'title', 'description']
	#champ non modifiable
	readonly_fields= ('date_created', 'date_updated')

#Register modele Bookmark et Tag	
admin.site.register(Bookmark,BookmarkAdmin)
admin.site.register(Tag)

	
	
	
	
	
	
	
	
	
	
	
