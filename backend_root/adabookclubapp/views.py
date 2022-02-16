from django.shortcuts import render
from .serializers import MemberSerializer, GroupSerializer, DiscussionSerializer, MessageSerializer, MemberEmailSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Member, Group, Discussion, Message        

# Create your views here.

class MemberView(viewsets.ModelViewSet):  
	serializer_class = MemberSerializer   
	queryset = Member.objects.all()

	@action(detail=False, methods=["get"])
	def get_member_by_email(self, request):
		serializer = MemberEmailSerializer(data=request.GET)
		serializer.is_valid(raise_exception=True)
		m = Member.objects.filter(email=serializer.data['email']).first()
		member_serializer = MemberSerializer(instance=m)
		print(member_serializer)
		print(member_serializer.data)
		return Response(member_serializer.data, status=status.HTTP_200_OK)


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
