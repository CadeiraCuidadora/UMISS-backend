from django.shortcuts import render
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework import permissions


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    permission_classes = (permissions.AllowAny, permissions.BasePermission)
