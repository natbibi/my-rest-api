from django.urls import path
from . import views

urlpatterns = [
    path('mailinglist/', views.MailingList.as_view()),
]
