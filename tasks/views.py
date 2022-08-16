from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from knox.models import AuthToken
from tasks.serializer import TaskSerlialization,RegisterSerializer,UserSerializer
from .models import Task
from rest_framework import generics,permissions
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import login
from knox.views import LoginView as KnoxLoginView
from rest_framework import status
from rest_framework.response import Response


# Create your views here.

class genric_list(generics.ListCreateAPIView) :
    queryset=Task.objects.all()
    serializer_class=TaskSerlialization
    permission_classes=[IsAuthenticated]

#class TaskViewSet(viewsets.ModelViewSet):
 #   serializer_class=TaskSerlialization
  #  queryset = Task.objects.all()
   # permission_classes =(IsAuthenticated,)


class RegisterUser(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny,)
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)