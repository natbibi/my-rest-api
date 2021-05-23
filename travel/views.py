from rest_framework import generics
from .models import Destination
from .serializers import DestinationSerializer

# GET, POST
class DestinationList(generics.ListCreateAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

# PATCH, DELETE
class DestinationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
