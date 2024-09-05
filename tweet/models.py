from django.db import models
from user.models import User

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name="tweet")
    tweet = models.TextField()
    image = models.ImageField(upload_to="tweet/images", blank=True, null= True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.tweet

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete= models.PROTECT)
    tweet = models.ForeignKey(Tweet, on_delete= models.CASCADE)
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.comment

class CommentReply(models.Model):
    user = models.ForeignKey(User, on_delete= models.PROTECT)
    comment = models.ForeignKey(Comment, on_delete= models.CASCADE)
    reply = models.TextField()
    reply_date = models.DateTimeField(auto_now_add= True)

    def __str__(self) -> str:
        return self.reply

class Save(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete= models.CASCADE)
    saved_date = models.DateTimeField(auto_now_add= True)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete= models.PROTECT)
    tweet = models.ForeignKey(Tweet, on_delete= models.CASCADE)
    liked_date = models.DateTimeField(auto_now_add= True)

class CommentLike(models.Model):
    user = models.ForeignKey(User, on_delete= models.PROTECT)
    comment = models.ForeignKey(Comment, on_delete= models.CASCADE)
    liked_date = models.DateTimeField(auto_now_add= True)

class Share(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete= models.CASCADE)
    note = models.TextField()
    shared_date = models.DateTimeField(auto_now_add= True)

