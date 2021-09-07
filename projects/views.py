from rest_framework import generics, permissions
from .models import Project
from .serializers import ProjectSerializer
from drf_spectacular.utils import extend_schema
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet


# GET, POST
class ProjectList(generics.ListCreateAPIView):
    """
    👩🏻‍💻 Returns a list of my best coding projects. Check out my portfolio at: https://nat-portfolio.netlify.app/
    """    
    queryset = Project.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ProjectSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering_fields = ['id']
    ordering = ['id']

# PATCH, DELETE
class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ProjectSerializer
