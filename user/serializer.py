from rest_framework import serializers
from .models import User, Follow
from djoser.serializers import UserCreateSerializer, UserSerializer as DjoserUserSerializer
from tweet.models import Tweet
from django.db.models.aggregates import Count

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username"]

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ["id", "tweet", "image","date_posted"]

class RegisterUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ["id", "first_name", "last_name", "username","email", "sex","profile","bio", "password"] 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username", "email", "sex", "profile", "bio","tweet", "followers", "following", "tweets"]
    
    tweet = TweetSerializer(many = True)
    followers = serializers.SerializerMethodField(method_name= "followers_count")
    following = serializers.SerializerMethodField(method_name= "following_count")
    tweets = serializers.SerializerMethodField(method_name= "tweets_count")

    def followers_count(self, user):
        count = Follow.objects.filter(follow_id= user.id).aggregate(count = Count("id"))
        return count["count"]
    def following_count(self, user):
        count = Follow.objects.filter(follower_id= user.id).aggregate(count = Count("id"))
        return count["count"]
    def tweets_count(self, user):
        count = Tweet.objects.filter(user_id= user.id).aggregate(count = Count("id"))
        return count["count"]
    

class CreateFollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ["id", "follow_date"]
    
    def create(self, validated_data):
        follower_id = self.context["follower_id"]
        follow_id = self.context["follow_id"]
        return Follow.objects.create(follow_id = follow_id, follower_id = follower_id, **validated_data)

class GetFollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ["id", "follow", "follow_date"]
    
    follow = UserSerializers()

class GetFollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ["id", "follower", "follow_date"]
    
    follower = UserSerializers()
