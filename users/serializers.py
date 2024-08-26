from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)


    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password', 'password_confirm', 'user_type')

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError("Passwords do not match.")
        return data 
       
    def create(self, validated_data):
        validated_data.pop('password_confirm')  # Remove password_confirm before creating the user
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            user_type=validated_data['user_type'],
        )
        return user
    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
        @classmethod
        def get_token(cls, user):
            token = super().get_token(user)
        # Add custom claims here if needed
            token['user_type'] = user.user_type
            return token

        def validate(self, attrs):
        # Update the validation to check email instead of username
            credentials = {
                'email': attrs.get('email'),
                'password': attrs.get('password')
                }
            user = authenticate(**credentials)
            if user and user.is_active:
                refresh = self.get_token(user)
                return {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'user_type': user.user_type,
                }
            raise serializers.ValidationError("Invalid credentials")

    