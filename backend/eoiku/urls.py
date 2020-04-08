
from django.urls import path,include
from . import views

urlpatterns = [
    path('post/',views.PostListView.as_view()),
    path('post/<int:pk>/',views.PostDetailView.as_view()),
    path('user/',views.UserListView.as_view()),
    path('user/<pk>/',views.UserDetailView.as_view()),
    path('coupon/',views.CouponListView.as_view()),
    path('coupon/<int:pk>/',views.CouponDetailView().as_view()),
]





