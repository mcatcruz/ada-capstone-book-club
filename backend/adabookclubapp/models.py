from django.db import models

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
	username = models.CharField(max_length=30)

class MemberGroups(models.Model):
	member_id =  models.ForeignKey("Member", on_delete=models.SET_NULL, null=True)
	group_id =  models.ForeignKey("Group", on_delete=models.SET_NULL, null=True)

class Group(models.Model):
	group_name = models.CharField(max_length=30)
	members = models.ManyToManyField('Member', through='MemberGroups', through_fields=('member_id', 'group_id'),)

class Discussion(models.Model):
	messages =  models.ManyToManyField("Message", through='GroupDiscussions', through_fields=('group_id','discussion_id'))  # How do I get a list of messages in here?
	date_created = models.DateField
	group_id = models.ForeignKey("Group", on_delete=models.SET_NULL, null=True)
	book_id = models.ForeighKey('Book', on_delete=models.SET_NULL, null=True)

class Message(models.Model):
	message = models.TextField
	date_posted = models.DateField

class DiscussionMessages(models.Model):
	messages =  models.ForeignKey("Message", on_delete=models.SET_NULL, null=True) # How do I get a list of messages in here?
	discussion_id = models.ForeignKey("Discussion", on_delete=models.SET_NULL, null=True)

class Book(models.Model):
	title = models.CharField(length=100)
	author = models.CharField(length=30)

class BookDiscussions(models.Model):
	book_id =  models.ForeignKey("Book", on_delete=models.SET_NULL, null=True)
	discussion =  models.ForeignKey("Discussion", on_delete=models.SET_NULL, null=True) # How do I get a list of discussions in here?