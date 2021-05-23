from rest_framework import generics, permissions
from .models import Project
from .serializers import ProjectSerializer

# GET, POST
class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ProjectSerializer

# PATCH, DELETE
class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ProjectSerializer
