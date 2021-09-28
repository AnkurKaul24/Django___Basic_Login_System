from django.urls import path

from . import views

app_name = 'account'

urlpatterns = [
    path('users/register/',views.registration,name='register'),
    path('user-profile/',views.userProfile,name='user-profile'),
    path('user-profile-update/',views.userUpdate,name='user-profile-update')
]
