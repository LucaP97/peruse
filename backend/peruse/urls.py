from django.urls import path, include
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('profile', views.ProfileViewSet, basename='profile')


urlpatterns = [
    path('', include(router.urls)),
]

