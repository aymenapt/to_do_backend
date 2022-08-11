
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet,RegisterUser

router = DefaultRouter()
router.register('your tasks', TaskViewSet)

urlpatterns = [
    path('',include(router.urls)),
   
]