from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Tweet,Like,Comment,CommentLike,CommentReply,Save
from . import serializer


class TweetViewset(ModelViewSet):
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["tweet"]
    ordering_fields = ["date_posted"]
    def get_queryset(self):
        if self.request.method == "PUT":
            return Tweet.objects.filter(user_id = self.request.user.id)
        elif self.request.method == "DELETE":
            return Tweet.objects.filter(user_id = self.request.user.id)
        elif self.request.method == "PATCH":
            return Tweet.objects.filter(user_id = self.request.user.id)
        else:
            return Tweet.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == "GET":
            return serializer.GetTweetSerializer
        return serializer.CreateTweetSerializer
    
    def get_serializer_context(self):
        return {"user_id": self.request.user.id}
    
    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]
    
class CommentViewset(ModelViewSet):
    def get_queryset(self):
        if self.request.method == "PUT":
            return Comment.objects.filter(user_id = self.request.user.id)
        elif self.request.method == "PATCH":
            return Comment.objects.filter(user_id = self.request.user.id)
        elif self.request.method == "DELETE":
            return Comment.objects.filter(user_id = self.request.user.id)
        else:
            return Comment.objects.filter(tweet_id = self.kwargs["tweet_pk"])
    
    def get_serializer_class(self):
        if self.request.method == "GET":
            return serializer.GetCommentSerializer
        return serializer.CreateCommentSerializer
    
    def get_serializer_context(self):
        return {"user_id": self.request.user.id,
                "tweet_id": self.kwargs["tweet_pk"]
                }

class LikeViewset(ModelViewSet):
    def get_queryset(self):
        if self.request.method == "PUT":
            return Like.objects.filter(user_id = self.request.user.id)
        elif self.request.method == "PATCH":
            return Like.objects.filter(user_id = self.request.user.id)
        elif self.request.method == "DELETE":
            return Like.objects.filter(user_id = self.request.user.id)
        else:
            return Like.objects.filter(tweet_id = self.kwargs["tweet_pk"])
    
    def get_serializer_class(self):
        if self.request.method == "GET":
            return serializer.GetLikeSerializer
        return serializer.CreateLikeSerializer
    
    def get_serializer_context(self):
        return { 
            "tweet_id": self.kwargs["tweet_pk"],
            "user_id": self.request.user.id
        }

class SaveViewSet(ModelViewSet):
    def get_queryset(self):
        return Save.objects.filter(user_id = self.request.user.id)
    def get_serializer_class(self):
        if self.request.method == "GET":
            return serializer.GetSaveSerializer
        return serializer.CreateSaveSerializer
    def get_serializer_context(self):
        return { 
            "tweet_id": self.kwargs["tweet_pk"],
            "user_id": self.request.user.id
        }

class CommentReplyViewset(ModelViewSet):
    def get_queryset(self):
        if self.request.method == "PUT":
            return CommentReply.objects.filter(user_id = self.request.user.id)
        elif self.request.method == "PATCH":
            return CommentReply.objects.filter(user_id = self.request.user.id)
        elif self.request.method == "DELETE":
            return CommentReply.objects.filter(user_id = self.request.user.id)
        else:
            return CommentReply.objects.filter(comment_id = self.kwargs["comment_pk"])
    
    def get_serializer_class(self):
        if self.request.method == "GET":
            return serializer.GetCommentReplySerializer
        return serializer.CreateCommentReplySerializer
    
    def get_serializer_context(self):
        return { 
            "comment_id": self.kwargs["comment_pk"],
            "user_id": self.request.user.id
        }

class CommentLikeviewset(ModelViewSet):
    def get_queryset(self):
        if self.request.method == "PUT":
            return CommentLike.objects.filter(user_id = self.request.user.id)
        elif self.request.method == "PATCH":
            return CommentLike.objects.filter(user_id = self.request.user.id)
        elif self.request.method == "DELETE":
            return CommentLike.objects.filter(user_id = self.request.user.id)
        else:
            return CommentLike.objects.filter(comment_id = self.kwargs["comment_pk"])
    
    def get_serializer_class(self):
        if self.request.method == "GET":
            return serializer.GetCommentLikeSerializer
        return serializer.CreateCommentLikeSerializer
    
    def get_serializer_context(self):
        return { 
            "comment_id": self.kwargs["comment_pk"],
            "user_id": self.request.user.id
        }
