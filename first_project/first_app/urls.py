from django.urls import path
from first_app import views

app_name='first_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('help', views.help, name='help'),
    path('temp', views.temp, name='temp'),
    path('formpage',views.form_name_view,name='form'),
    path('register',views.register,name='register'),
    path('login',views.user_login,name='login'),
    
]
