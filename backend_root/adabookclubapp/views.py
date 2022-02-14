from django.shortcuts import render
from .serializers import MemberSerializer, GroupSerializer, DiscussionSerializer, MessageSerializer, BookSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Member, Group, Discussion, Message, Book        

# Create your views here.

class MemberView(viewsets.ModelViewSet):  
    serializer_class = MemberSerializer   
    queryset = Member.objects.all()   

class GroupView(viewsets.ModelViewSet):
	serializer_class = GroupSerializer
	queryset = Group.objects.all()

class DiscussionView(viewsets.ModelViewSet):
	serializer_class = DiscussionSerializer
	queryset = Discussion.objects.all()

class MessageView(viewsets.ModelViewSet):
	serializer_class = MessageSerializer
	queryset = Message.objects.all()

# class BookView(viewsets.ModelViewSet):
# 	serializer_class = BookSerializer
# 	queryset = Book.objects.all()
