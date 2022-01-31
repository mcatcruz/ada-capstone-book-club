from django.shortcuts import render
from .serializers import MemberSerializer, MemberGroupsSerializer, GroupSerializer, DiscussionSerializer, MessageSerializer, BookSerializer, BookDiscussionSerializer
from rest_framework import viewsets      
from .models import Member, MemberGroups, Group, Discussion, Message, Book, BookDiscussions            

# Create your views here.

class MemberView(viewsets.ModelViewSet):  
    serializer_class = MemberSerializer   
    queryset = Member.objects.all()   

class MemberGroupsView(viewsets.ModelViewSet):  
    serializer_class = MemberGroupsSerializer   
    queryset = MemberGroups.objects.all()

class GroupView(viewsets.ModelViewSet):
	serializer_class = GroupSerializer
	queryset = Group.objects.all()

class DiscussionSerializerView(viewsets.ModelViewSet):
	serializer_class = DiscussionSerializer
	queryset = Discussion.objects.all()

class MessageSerializerView(viewsets.ModelViewSet):
	serializer_class = MessageSerializer
	queryset = Message.objects.all()

class BookSerializerView(viewsets.ModelViewSet):
	serializer_class = BookSerializer
	queryset = Book.objects.all()

class BookDiscussionSerializerView(viewsets.ModelViewSet):
	serializer_class = BookDiscussionSerializer
	queryset = BookDiscussions.objects.all()
