
from django.contrib import admin
from django.urls import path,include
from tasks.views import RegisterUser,LoginAPI, Userlist,task_gp,task_gdu


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/',task_gp.as_view()),
    path('register/', RegisterUser.as_view()),
    path('login/', LoginAPI.as_view()),
    path('users/', Userlist.as_view()),
    path('tasks/<int:pk>/',task_gdu.as_view()),
    #path('gettask/', views.gettasks),
]
