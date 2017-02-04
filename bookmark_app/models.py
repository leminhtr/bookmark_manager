# encoding: utf-8
from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.timezone import now

#Classe Tag : attribut(id, name) id : #pk
@python_2_unicode_compatible
class Tag(models.Model):
	name = models.CharField(max_length=50, unique=True)
	
	class Meta:
		verbose_name='tag'
		verbose_name_plural='tags'
		ordering = ['name']

	def __str__(self):
		return self.name

#Bookmark manager
class PublicBookmarkManager(models.Manager):
	def get_queryset(self):
		qs = super(PublicBookmarkManager, self).get_queryset()
		return qs.filter(is_public=True) # seulement les bookmarks publics



@python_2_unicode_compatible
#Classe Bookmark : attribut (id, url, title, desc, is_public, date_created, date_updated, owner, tags); id : #pk
class Bookmark(models.Model):
	url = models.URLField()
	title = models.CharField('title', max_length=255)
	description = models.TextField('description', blank=True)
	is_public = models.BooleanField('public', default=True)
	date_created = models.DateTimeField('date created')
	date_updated = models.DateTimeField('date updated')
	owner = models.ForeignKey(User, verbose_name='owner',
		related_name='bookmarks')
	tags = models.ManyToManyField(Tag, blank=True)
	#Tags reference class tag
	#Plusieurs tags par Bookmark rel

	# Default manager
	objects = models.Manager()
	#2nd manager : return bookmark public suelement
	public = PublicBookmarkManager()

	class Meta:
		verbose_name='bookmark'
		verbose_name_plural='bookmarks'
		ordering = ['-date_created']

	def __str__(self):
		return '%s (%s)' %(self.title, self.url)

	def save(self, *args, **kwargs):
		if not self.id: #si le bookmark n'est pas dans la BDD
			self.date_created=now() #alors date creation =now
		self.date_updated=now() #sinon il existe deja => update
		super(Bookmark, self).save(*args, **kwargs) #appelle la classe


		
		























