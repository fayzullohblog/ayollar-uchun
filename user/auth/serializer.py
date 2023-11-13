from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
# from ..models import User
from ..models import User


class RegisterSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password1 = serializers.CharField(write_only=True, required=True,)
    phone_number = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )


    class Meta:
        model=User
        fields=['first_name','last_name','phone_number','password','password1']
        extra_kwargs = {
            'password':{'write_only': True},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password1']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs
    
    
    
    def create(self, validated_data):
        user = User.objects.create_user(
                validated_data['phone_number'],
                password = validated_data['password'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name']
                )
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['first_name','last_name','phone_number','password']