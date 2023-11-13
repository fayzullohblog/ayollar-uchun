from .serializer import RegisterSerializer,UserSerializer
from rest_framework.response import Response



from django.shortcuts import render
from rest_framework import generics
# Create your views here.
class RegisterGenericApiView(generics.GenericAPIView):
    serializer_class=RegisterSerializer

    def post(self,request,*args,**kwrags):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response({
            "user": UserSerializer(user,    context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })