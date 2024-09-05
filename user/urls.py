from django.urls import path,include
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register("user", views.UserViewSet, basename="user")
router.register("following", views.CurrentFollowing, basename= "following")
router.register("followers", views.CurrentFollowers, basename= "followers")

user_routers = routers.NestedDefaultRouter(router, "user", lookup = "user")
user_routers.register("following", views.FollowingViewSet, basename= "user-following")
user_routers.register("followers", views.FollowerViewSet, basename= "user-followers")
urlpatterns = [
    path("",include(router.urls)),
    path("", include(user_routers.urls)),
]