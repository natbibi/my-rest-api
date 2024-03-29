from rest_framework import serializers
from .models import Mailing

class MailingSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Mailing
        fields = [
            "id",
            "name",
            "email",
        ]