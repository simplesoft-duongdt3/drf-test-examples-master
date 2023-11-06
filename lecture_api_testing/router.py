from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CityViewSet, SchoolViewSet, StudentViewSet, UserViewSet, User2ViewSet, User3ViewSet

router = DefaultRouter(trailing_slash=True)

router.register(r"cities", CityViewSet)
router.register(r"schools", SchoolViewSet)
router.register(r"students", StudentViewSet)
router.register("users", UserViewSet, basename='user')
router.register("users2", User2ViewSet, basename='user2')
router.register("users3", User3ViewSet, basename='user3')

