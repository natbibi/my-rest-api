from django.urls import path
from . import views

urlpatterns = [
    path('eatout/', views.OutList.as_view()),
    path('eatout/<int:pk>', views.OutDetail.as_view()),
    path('eatin/', views.InList.as_view()),
    path('eatin/<int:pk>', views.InDetail.as_view())
]
