from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Project
        fields = [
            "id",
            "name",
            "description",
            "technologies",
            "github",
            "netlify",
            "image",
            "alt",
        ]
        extra_kwargs = {
            "display": {"required": False},
        }
