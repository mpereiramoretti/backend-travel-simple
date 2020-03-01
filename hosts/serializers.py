from rest_framework import serializers
from .models import Host

class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = ('pk', 'name', 'address', 'bedroom_name', 'city', 'available_places', 'busy_dates', 'purchased')