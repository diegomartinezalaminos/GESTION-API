from django.contrib import admin
from django.urls import path, include
from .views import UserProfileView

from rest_framework import routers

router = routers.DefaultRouter()
router.register("user_profile", UserProfileView)

urlpatterns = [
    path("", include(router.urls)),
]
