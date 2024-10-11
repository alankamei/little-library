from rest_framework import serializers
from .models import CustomUser


from rest_framework import serializers
from .models import CustomUser


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(**validated_data)
        user.set_password(validated_data['password'])  # Ensure the password is hashed
        user.save()
        return user



class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        # Check if the user exists
        user = CustomUser.objects.filter(email=email).first()
        if user is None:
            raise serializers.ValidationError("User with this email does not exist.")

        # Check if the password is correct
        if not user.check_password(password):
            raise serializers.ValidationError("Invalid password.")

        return attrs  # Return the validated attributes
    
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'genre', 'description', 'cover_image']
