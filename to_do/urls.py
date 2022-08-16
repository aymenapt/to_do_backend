
from django.contrib import admin
from django.urls import path,include

from tasks.views import RegisterUser,LoginAPI,genric_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/',genric_list.as_view()),
    path('register/', RegisterUser.as_view()),
    path('login/', LoginAPI.as_view()),
]
