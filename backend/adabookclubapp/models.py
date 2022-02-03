from tkinter import TRUE
from django.db import models
from django.urls import reverse 


# Create your models here.
# Relationships
	# A group can have many members
	# A member can have many groups

	# A group can have many discussions
	# A discussion can have ONE group
	
	# A message can have ONE discussion
	# A discussion can have many messages

	# A book can have many discussions
	# A discussion can have ONE book

	# Group and Book are connected through Discussion (implicit relationship - to figure out what groups belong to a book: GET group_id FROM discussion WHERE book_id IS ___)
		# In Django ORM: discussion.objects.filter(group_id=___)
			# This returns an array (query list) of discussions
		# Fine for now since we have a small scale web app.

class Member(models.Model):
	username = models.CharField(max_length=30, help_text='Enter a username', unique=True)

	def __str__(self):
		return self.username

class Group(models.Model):
	group_name = models.CharField(max_length=100, help_text='Enter a group name', unique=True)
	members = models.ManyToManyField('Member', related_name='groups')

	def __str__(self):
		return self.group_name

	@property # a decorator that lets you use the method as a property
	def discussions(self):
		return Discussion.objects.filter(group_id=self.id)

class Discussion(models.Model):
	subject = models.CharField(max_length=100, blank=False, help_text='Enter a subject for discussion', unique=True)
	messages =  models.ForeignKey("Message", on_delete=models.SET_NULL, null=True)
	date_created = models.DateField(auto_now=True)
	group_id = models.ForeignKey("Group", on_delete=models.CASCADE)
	# book_id = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return self.subject
	
class Message(models.Model):
	message = models.TextField
	date_posted = models.DateField
	discussion_id = models.ForeignKey('Discussion', on_delete=models.SET_NULL, null=True)
	

class Book(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=30)

	def __str__(self):
		return self.title

class BookDiscussion(models.Model):
	book_id =  models.ForeignKey("Book", on_delete=models.SET_NULL, null=True)
	discussion_id =  models.ForeignKey("Discussion", on_delete=models.SET_NULL, null=True) # How do I get a list of discussions in here?