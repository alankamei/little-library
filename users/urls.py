from django.urls import path
from .views import RegisterView, UserDeleteView, home

urlpatterns = [
    path('',home,name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('delete-user/<int:pk>/', UserDeleteView.as_view(), name='user-delete'),
]