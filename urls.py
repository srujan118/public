from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
   path('images/',views.images),
   path('user/',views.user),
   path('task/',views.task)
]