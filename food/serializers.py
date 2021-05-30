from rest_framework import serializers
from .models import Out, In

class OutSerializer(serializers.ModelSerializer):
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