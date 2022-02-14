from rest_framework import serializers
from .models import Member, Group, Discussion, Message

class MessageSerializer(serializers.ModelSerializer):
	class Meta:
		ordering = ['-date_posted']     
		model = Message
		fields = ('__all__')

class DiscussionSerializer(serializers.ModelSerializer):
	messages = MessageSerializer(read_only=True, many=True)
	class Meta:
		ordering = ['-date_created']
		model = Discussion
		fields = ('__all__')

# class BookSerializer(serializers.ModelSerializer):
# 	discussions = DiscussionSerializer(read_only=True, many=True)
# 	class Meta:
# 		model = Book
# 		fields = ('__all__')

class GroupSerializer(serializers.ModelSerializer):
	discussions = DiscussionSerializer(read_only=True, many=True)
	class Meta:
		ordering = ['group_name']
		model = Group
		fields = ('__all__')

class MemberSerializer(serializers.ModelSerializer):
	groups = GroupSerializer(read_only=True, many=True)
	messages = MessageSerializer(read_only=True, many=True)
	class Meta:
		model = Member
		fields = ('__all__')

