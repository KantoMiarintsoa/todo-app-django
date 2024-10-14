from django.urls import path
from .views import index,login_view, add_task,complete_task

urlpatterns=[
    path("",index, name="home"),
    path("login",login_view,name="login"),
    path("task/add",add_task,name="add-task"),
    path("task/<id:int>/complete",complete_task,name="complete-task")
]