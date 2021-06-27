from rest_framework import serializers
from .models import Out, OutImage, In

class OutSerializer(serializers.ModelSerializer):
    more_images = serializers.StringRelatedField(many=True)

    class Meta: 
        model = Out
        fields = [
            "id",
            "title",
            "restaurant_name",
            "location",
            "value",
            "taste",
            "atmosphere",
            "service",
            "date",
            "description",
            "image",
            "more_images",
            "recommend",
        ]

class InSerializer(serializers.ModelSerializer):
    class Meta: 
        model = In
        fields = [
            "id",
            "title",
            "dish_name",
            "date",
            "description",
            "image",
        ]