from rest_framework import generics, permissions
from .models import Destination
from .serializers import DestinationSerializer
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


# GET, POST
class DestinationList(generics.ListCreateAPIView):
    """
    🌍 Returns a list of all travel destinations that I have visited. Check out my [travel blog][ref]!

    [ref]: https://nat-travels.netlify.app/
    """    
    queryset = Destination.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = DestinationSerializer

# PATCH, DELETE
class DestinationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Destination.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = DestinationSerializer
