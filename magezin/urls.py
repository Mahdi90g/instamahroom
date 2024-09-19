from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home , name='home'),
    path('new/',views.new.as_view() , name='new'),
    path('<pk>/edit/',views.edit.as_view() , name='edit'),
    path('<pk>/delt/',views.delt.as_view() , name='delt'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('signup/',views.signup_u , name='signup'),
    path('<pk>/profile/',views.profile.as_view() , name='profile'),
    path('mypost/',views.myposti.as_view() , name='mypost'),
    path('control/',views.control.as_view() , name='control'),
    path('allpost/',views.allpost.as_view() , name='allpost'),
    path('<pk>/editadmin/',views.editadmin.as_view(), name='editadmin'),
    path('password_change_form/',views.changepass.as_view(),name='changepass'),
    path('password_change_form/done/',views.done.as_view(),name='done'),

    path('password_reset/', views.passreset.as_view(), name='password_reset'),
    path('password_reset/done/', views.passdone.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.passconf.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.passend.as_view(), name='password_reset_complete'),

    
]