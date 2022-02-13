from rest_framework import generics, permissions, filters
from .models import Out, In
from .serializers import OutSerializer, InSerializer
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from django.db.models import Count

# GET, POST
class OutList(generics.ListCreateAPIView):
    """
    🍤 Returns a list of my Ste's dining experiences at restaurants. Find his food blog at: https://stesfood.netlify.app/
    """   
    queryset = Out.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = OutSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, filters.SearchFilter)
    ordering_fields = ['id', 'date']
    ordering = ['id', 'date']
    filterset_fields = ['recommend']
    search_fields = ['restaurant_name', 'description']

# PATCH, DELETE
class OutDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Out.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = OutSerializer

# GET, POST
class InList(generics.ListCreateAPIView):
    """
    🍤 Returns a list of my Ste's home cooking. Find his food blog at: https://stesfood.netlify.app/
    """   
    queryset = In.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = InSerializer

# PATCH, DELETE
class InDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = In.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = InSerializer
