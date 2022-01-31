from rest_framework import serializers
from .models import Member, MemberGroups, Group, Discussion, Message, Book, BookDiscussions


class MemberSerializer(serializers.ModelSerializer):
    class MemberMeta:
        model = Member
        fields = ('id' ,'username', 'groups')

class MemberGroupsSerializer(serializers.ModelSerializer):
    class MemberGroupsMeta:
        model = MemberGroups
        fields = ('member', 'group')

class GroupSerializer(serializers.ModelSerializer):
    class GroupMeta:
        model = Group
        fields = ('group_name', 'members')

class DiscussionSerializer(serializers.ModelSerializer):
	class DiscussionMeta:
		model = Discussion
		fields = ('messages', 'date_posted', 'discussion_id')

class MessageSerializer(serializers.ModelSerializer):
	class MessageMeta:
		model = Message
		fields = ('message', 'date_posted', 'discussion_id')

class BookSerializer(serializers.ModelSerializer):
	class BookMeta:
		model = Book
		fields = ('title', 'author')

class BookDiscussionSerializer(serializers.ModelSerializer):
	class BookDiscussionMeta:
		model = BookDiscussions
		fields = ('book_id', 'discussion_id')