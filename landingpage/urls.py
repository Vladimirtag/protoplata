from django.contrib import admin
from django.urls import path, include
from . import views



app_name = 'landingpage'

urlpatterns = [
	
    path('home/', views.JoinForm.as_view(), name='main'),
    # path('publication/', views.send_form, name='toppublications'),

    path('index/', views.index, name='index'),

]