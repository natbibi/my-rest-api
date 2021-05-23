from rest_framework import generics, permissions
from .models import Destination
from .serializers import DestinationSerializer

# GET, POST
class DestinationList(generics.ListCreateAPIView):
    queryset = Destination.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = DestinationSerializer

# PATCH, DELETE
class DestinationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Destination.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = DestinationSerializer
