from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name="home"),
    path ('signup/',views.signup,name='signup'),
    path('logout/',views.logout,name='logout'),
    path('login/',views.loginuser,name='loginuser')
]