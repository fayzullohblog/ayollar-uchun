from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import User, Job
from .serailizer import UserSerializer, JobSerailzier


class JobListView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerailzier
    pagination_class = None
    permission_classes = [IsAuthenticated]


class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
