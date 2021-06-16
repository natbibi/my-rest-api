from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('destinations/', views.DestinationList.as_view()),
    path('destinations/<int:pk>', views.DestinationDetail.as_view())
]