from .models import Storage
from rest_framework import serializers

class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = ['key', 'value', 'updated_at']