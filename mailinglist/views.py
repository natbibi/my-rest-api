from rest_framework import generics, permissions
from .models import Mailing
from .serializers import MailingSerializer

# GET, POST
class MailingList(generics.ListCreateAPIView):
    queryset = Mailing.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = MailingSerializer

# PATCH, DELETE
class MailingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mailing.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = MailingSerializer

