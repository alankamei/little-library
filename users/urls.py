from django.urls import path
from .views import RegisterView, UserDeleteView, LoginView, home, LogoutView, MyTokenObtainPairView, MyTokenRefreshView, BookListView


urlpatterns = [
    path('',home,name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('delete-user/<int:pk>/', UserDeleteView.as_view(), name='user-delete'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
    path('api/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', MyTokenRefreshView.as_view(), name='token_refresh'),
    path('books/', BookListView.as_view(), name='book-list'),

]


