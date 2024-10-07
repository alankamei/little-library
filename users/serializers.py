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

            