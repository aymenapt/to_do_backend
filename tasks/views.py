
from django.shortcuts import render
from rest_framework.response import Response
from knox.models import AuthToken
from tasks.serializer import TaskSerlialization,RegisterSerializer,UserSerializer
from .models import Task ,User
from rest_framework import generics,permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import login
from knox.views import LoginView as KnoxLoginView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes

# Create your views here.


#get and post
class task_gp(generics.ListCreateAPIView) :
    permission_classes=[IsAuthenticated]
    queryset=Task.objects.all()
    serializer_class=TaskSerlialization    

#get ,delete and update
class task_gdu(generics.RetrieveUpdateDestroyAPIView) :
    permission_classes=[IsAuthenticated]
    queryset=Task.objects.all()
    serializer_class=TaskSerlialization  

#class TaskViewSet(viewsets.ModelViewSet):
 #   serializer_class=TaskSerlialization
  #  queryset = Task.objects.all()
   # permission_classes =(IsAuthenticated,)
class Userlist(generics.ListCreateAPIView) :
    queryset=User.objects.all()
    serializer_class=UserSerializer


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