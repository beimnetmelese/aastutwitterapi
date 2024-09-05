from rest_framework import serializers
from .models import Tweet,Like,Comment,Save,CommentLike,CommentReply,Share
from user.models import User
from django.db.models.aggregates import Count

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "profile"]

class CreateTweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ["id", "tweet","image","date_posted"]
    
    def create(self, validated_data):
        user_id = self.context["user_id"]
        return Tweet.objects.create(user_id = user_id, **validated_data)

class GetTweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ["id","user", "tweet", "image", "date_posted", "like", "comment"]
    user = UserSerializer()
    like = serializers.SerializerMethodField(method_name= 'like_count')
    comment = serializers.SerializerMethodField(method_name= "comment_count")

    def like_count(self, tweet: Tweet):
        count = Like.objects.filter(tweet_id = tweet.id).aggregate(count = Count("id"))
        return count["count"]
    
    def comment_count(self, tweet):
        count = Comment.objects.filter(tweet_id = tweet.id).aggregate(count = Count("id"))
        return count["count"]


class CreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id","comment", "comment_date"]
    
    def create(self, validated_data):
        user_id = self.context["user_id"]
        tweet_id = self.context["tweet_id"]
        return Comment.objects.create(user_id = user_id, tweet_id = tweet_id, **validated_data)

class GetCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "user","comment", "comment_date", "like", "reply"]
    user = UserSerializer()
    like = serializers.SerializerMethodField(method_name="like_count")
    reply = serializers.SerializerMethodField(method_name= "reply_count")

    def like_count(self, comment):
        count = CommentLike.objects.filter(comment_id = comment.id).aggregate(count = Count("id"))
        return count["count"]
    def reply_count(self, comment):
        count = CommentReply.objects.filter(comment_id = comment.id).aggregate(count = Count("id"))
        return count["count"]

class CreateLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ["id","liked_date"]
    
    def create(self, validated_data):
        user_id = self.context["user_id"]
        tweet_id = self.context["tweet_id"]
        return Like.objects.create(user_id= user_id, tweet_id=tweet_id, **validated_data)

class GetLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ["id", "user","liked_date"]
    user = UserSerializer()

class CreateSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Save
        fields = ["id", "saved_date"] 
    
    def create(self, validated_data):
        user_id = self.context["user_id"]
        tweet_id = self.context["tweet_id"]
        return Save.objects.create(user_id= user_id, tweet_id= tweet_id, **validated_data)

class GetSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Save
        fields = ["id", "user", "tweet", "saved_date"]
    
    user = UserSerializer()
    tweet = GetTweetSerializer()

class CreateCommentReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentReply
        fields = ["id", "reply", "reply_date"]
    
    def create(self, validated_data):
        user_id = self.context["user_id"]
        comment_id = self.context["comment_id"]
        return CommentReply.objects.create(user_id= user_id, comment_id= comment_id, **validated_data)

class GetCommentReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentReply
        fields = ["id", "user", "comment", "reply", "reply_date"]
    
    user = UserSerializer()
    comment = GetCommentSerializer()

class CreateCommentLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentLike
        fields = ["id", "liked_date"]

    def create(self, validated_data):
        user_id = self.context["user_id"]
        comment_id  = self.context["comment_id"]
        return CommentLike.objects.create(user_id =user_id, comment_id= comment_id, **validated_data)

class GetCommentLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentLike
        fields = ["id", "user", "liked_date"]
    user = UserSerializer()