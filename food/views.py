from rest_framework import generics, permissions
from .models import Out, In
from .serializers import OutSerializer, InSerializer

# GET, POST
class OutList(generics.ListCreateAPIView):
    queryset = Out.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = OutSerializer

# PATCH, DELETE
class OutDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Out.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = OutSerializer

# GET, POST
class InList(generics.ListCreateAPIView):
    queryset = In.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = InSerializer

# PATCH, DELETE
class InDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = In.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = InSerializer
