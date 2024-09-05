from django.urls import path,include
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register("tweet", views.TweetViewset, basename="tweet")

tweet_routers = routers.NestedDefaultRouter(router, "tweet", lookup = "tweet")
tweet_routers.register("comment", views.CommentViewset, basename="tweet-comment")
tweet_routers.register("like", views.LikeViewset, basename="like-comment")
tweet_routers.register("save", views.SaveViewSet, basename= "save-tweet")

comment_routers = routers.NestedDefaultRouter(tweet_routers, "comment", lookup = "comment")
comment_routers.register("reply", views.CommentReplyViewset, basename= "comment-reply")
comment_routers.register("like", views.CommentLikeviewset,basename= "comment-like")
urlpatterns = [
    path("", include(router.urls)),
    path("", include(tweet_routers.urls)),
    path("", include(comment_routers.urls)),
]