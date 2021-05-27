from django.urls import path
from . import views

urlpatterns = [
    path('mailinglist/', views.MailingList.as_view()),
    path('mailinglist/<int:pk>', views.MailingDetail.as_view())
]
