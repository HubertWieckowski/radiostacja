from rest_framework import serializers
from .models import Artist, Hit

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'first_name', 'last_name', 'created_at']

class HitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hit
        fields = ['id', 'title', 'artist', 'title_url', 'created_at', 'updated_at']
        read_only_fields = ['title_url', 'created_at', 'updated_at']

    def create(self, validated_data):
        hit = Hit.objects.create(**validated_data)
        return hit
