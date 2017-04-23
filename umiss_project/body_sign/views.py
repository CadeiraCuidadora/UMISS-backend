from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from body_sign.models import BodySignal, HeartBeats, SkinTemperature, GalvanicResistance
from body_sign.permissions import IsOwnerOrReadOnly
from body_sign.serializers import HeartBeatsSerializer, SkinTemperatureSerializer, GalvanicResistanceSerializer
import body_sign.signals


class HeartBeatsViewSet(viewsets.ModelViewSet):
    queryset = HeartBeats.objects.all()
    serializer_class = HeartBeatsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class GalvanicResistanceViewSet(viewsets.ModelViewSet):
    queryset = GalvanicResistance.objects.all()
    serializer_class = GalvanicResistanceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SkinTemperatureViewSet(viewsets.ModelViewSet):
    queryset = SkinTemperature.objects.all()
    serializer_class = SkinTemperatureSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
