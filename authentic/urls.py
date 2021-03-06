from django.urls import path, include
from . import views

urlpatterns = [

    #todowork
    path('', views.index, name="home"),
    path('currenttodo/',views.currenttodo,name="currenttodo"),
    path('createtodo/',views.createtodo,name="createtodo"),
    path('todo/<int:todo_pk>',views.viewtodo,name="viewtodo"),
    path('todo/<int:todo_pk>/complete',views.completetodo,name="completetodo"),
    path('todo/<int:todo_pk>/delete',views.deletetodo,name="deletetodo"),


    # auth
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('login/', views.loginuser, name='loginuser')
]
