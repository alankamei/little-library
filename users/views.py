from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import CustomUser
from .serializers import UserRegisterSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegisterSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "Registration successful"}, status =status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
def home(request):
    return render(request, 'home.html')




from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DeleteView
from django.urls import reverse_lazy
User = get_user_model()
class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    template_name = 'user_confirm_delete.html'  # Create this template for confirmation
    success_url = reverse_lazy('user-list')  # Redirect after deletion
    def test_func(self):
        return self.request.user.is_superuser
    