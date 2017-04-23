from rest_framework import serializers
from body_sign.models import HeartBeats, BodySignal, GalvanicResistance, SkinTemperature
from django.contrib.auth.models import User


class HeartBeatsSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = HeartBeats
        fields = ('owner', 'created', 'beats')


class GalvanicResistanceSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = GalvanicResistance
        fields = ('owner', 'created', 'resistance')


class SkinTemperatureSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = SkinTemperature
        fields = ('owner', 'created', 'temperature')
