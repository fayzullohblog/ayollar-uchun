from rest_framework import serializers

from .models import User, Job


class JobSerailzier(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['id', 'title']


class UserSerializer(serializers.ModelSerializer):
    phone_number = serializers.ReadOnlyField()
    job = JobSerailzier()

    class Meta:
        model = User
        fields = [
            "phone_number",
            'first_name',
            'last_name',
            'gender',
            'birth_day',
            'email',
            'country',
            'region',
            'postcode',
            'address',
            'instagram',
            'imkon_uz',
            'linkedin',
            'workplace',
            'job',
            'about',
        ]
