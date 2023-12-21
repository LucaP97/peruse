from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .permissions import *
from .models import *
from .serializers import *


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'POST' and not self.request.user.is_authenticated:
            return ProfileRegistrationSerializer
        return ProfileSerializer
    
    def get_permissions(self):
        if self.request.method in ['POST']:
            return [IsAnonymous()]
        return [IsAuthenticated()]
