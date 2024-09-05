from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializer import UserSerializer, GetFollowerSerializer,GetFollowingSerializer,CreateFollowSerializer
from .models import User, Follow

class UserViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [SearchFilter]
    search_fields = ["first_name", "last_name", "username"]

class FollowingViewSet(ModelViewSet):
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["first_name", "last_name", "username"]
    ordering_fields = ["follow_date"]
    def get_queryset(self):
        if self.request.method == "PUT":
            return Follow.objects.filter(follwer_id = self.request.user.id)
        elif self.request.method == "PATCH":
            return Follow.objects.filter(follwer_id = self.request.user.id)
        elif self.request.method == "DELETE":
            return Follow.objects.filter(follower_id = self.request.user.id)
        else:
            return Follow.objects.filter(follower_id = self.kwargs["user_pk"])
    def get_serializer_class(self):
        if self.request.method == "GET":
            return GetFollowingSerializer
        return CreateFollowSerializer
    
    def get_serializer_context(self):
        return {"follow_id": self.kwargs["user_pk"],
                "follower_id": self.request.user.id 
                }
    
class FollowerViewSet(ModelViewSet):
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["first_name", "last_name", "username"]
    ordering_fields = ["follow_date"]
    def get_queryset(self):
        if self.request.method == "PUT":
            return Follow.objects.filter(follwer_id = self.request.user.id)
        elif self.request.method == "PATCH":
            return Follow.objects.filter(follwer_id = self.request.user.id)
        elif self.request.method == "DELETE":
            return Follow.objects.filter(follower_id = self.request.user.id)
        else:
            return Follow.objects.filter(follow_id = self.kwargs["user_pk"])
    def get_serializer_class(self):
        if self.request.method == "GET":
            return GetFollowerSerializer
        return CreateFollowSerializer
    
    def get_serializer_context(self):
        return {"follow_id": self.kwargs["user_pk"],
                "follower_id": self.request.user.id 
                }

class CurrentFollowing(RetrieveModelMixin, ListModelMixin,GenericViewSet):
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["first_name", "last_name", "username"]
    ordering_fields = ["follow_date"]
    def get_queryset(self):
        return Follow.objects.filter(follower_id = self.request.user.id)
    serializer_class = GetFollowingSerializer

class CurrentFollowers(RetrieveModelMixin, ListModelMixin,GenericViewSet):
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["first_name", "last_name", "username"]
    ordering_fields = ["follow_date"]
    def get_queryset(self):
        return Follow.objects.filter(follow_id = self.request.user.id)
    serializer_class = GetFollowerSerializer