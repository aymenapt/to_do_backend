
from django.contrib import admin
from django.urls import path,include

from tasks.views import RegisterUser,LoginAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task/', include('tasks.task_url')),
    path('register/', RegisterUser.as_view()),
    path('login/', LoginAPI.as_view()),
]
