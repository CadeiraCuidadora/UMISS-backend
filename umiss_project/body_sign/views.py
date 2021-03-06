from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from body_sign.models import BodySignal, HeartBeats, SkinTemperature, GalvanicResistance, FellChair
from body_sign.permissions import IsOwnerOrReadOnly
from body_sign.serializers import HeartBeatsSerializer, SkinTemperatureSerializer, GalvanicResistanceSerializer, FellChairSerializer
from umiss_auth.models import Monitor
import body_sign.signals
import sys

class FellChairViewSet(viewsets.ModelViewSet):
    queryset = FellChair.objects.all()
    serializer_class = FellChairSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        monitor_id = self.request.user.id
        monitor = Monitor.objects.get(id=monitor_id)
        patient = monitor.monitor_user
        return FellChair.objects.filter(owner=patient)


class HeartBeatsViewSet(viewsets.ModelViewSet):
    queryset = HeartBeats.objects.all()
    serializer_class = HeartBeatsSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        monitor_id = self.request.user.id
        monitor = Monitor.objects.get(id=monitor_id)
        patient = monitor.monitor_user
        return HeartBeats.objects.order_by('-id').filter(owner=patient)


class GalvanicResistanceViewSet(viewsets.ModelViewSet):
    queryset = GalvanicResistance.objects.all()
    serializer_class = GalvanicResistanceSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        monitor_id = self.request.user.id
        monitor = Monitor.objects.get(id=monitor_id)
        patient = monitor.monitor_user
        return GalvanicResistance.objects.order_by('-id').filter(owner=patient)


class SkinTemperatureViewSet(viewsets.ModelViewSet):
    queryset = SkinTemperature.objects.all()
    serializer_class = SkinTemperatureSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        monitor_id = self.request.user.id
        monitor = Monitor.objects.get(id=monitor_id)
        patient = monitor.monitor_user
        return SkinTemperature.objects.order_by('-id').filter(owner=patient)
