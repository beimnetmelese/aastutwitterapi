from django.contrib import admin
from .models import Tweet,Comment,CommentLike,CommentReply,Save,Like

class TweetAdmin(admin.ModelAdmin):
    list_display = ["user", "tweet", "date_posted"]

class CommentAdmin(admin.ModelAdmin):
    list_display = ["user", "tweet", "comment", "comment_date"]

class CommentLikeAdmin(admin.ModelAdmin):
    list_display = ["user", "comment", "liked_date"]

class LikeAdmin(admin.ModelAdmin):
    list_display = ["user", "tweet", "liked_date"]

class CommentReplyAdmin(admin.ModelAdmin):
    list_display = ["user","comment","reply", "reply_date"]

class SaveAdmin(admin.ModelAdmin):
    list_display = ["user", "tweet", "saved_date"]


admin.site.register(Tweet, TweetAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(CommentLike, CommentLikeAdmin)
admin.site.register(CommentReply, CommentReplyAdmin)
admin.site.register(Save, SaveAdmin)
admin.site.register(Like, LikeAdmin)
