
from django.contrib import admin
from django.urls import path,include

from tasks.views import RegisterUser,LoginAPI,TaskViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/',TaskViewSet.as_view({'get': 'list'})),
    path('register/', RegisterUser.as_view()),
    path('login/', LoginAPI.as_view()),
]
