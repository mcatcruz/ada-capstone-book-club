from rest_framework import serializers
from .models import Member, MemberGroup, Group, Discussion, Message, Book, BookDiscussion


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('id' ,'username', 'groups')

class MemberGroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberGroup
        fields = ('member', 'group')

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'group_name', 'members')

class DiscussionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Discussion
		fields = ('id', 'messages', 'date_created')

class MessageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Message
		fields = ('message', 'date_posted', 'discussion_id')

class BookSerializer(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields = ('id', 'title', 'author')

class BookDiscussionSerializer(serializers.ModelSerializer):
	class Meta:
		model = BookDiscussion
		fields = ('book_id', 'discussion_id')