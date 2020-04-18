from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.PostListAPIView.as_view()),
    path('<int:pk>/',views.PostDetailAPIView.as_view()),
]