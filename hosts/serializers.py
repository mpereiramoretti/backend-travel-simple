from rest_framework import serializers
from .models import Host, Bedroom

class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = ('pk', 'name', 'address', 'city')

class BedroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bedroom
        fields = ('pk', 'name', 'host', 'maximum_guests', 'busy_dates', 'purchased')