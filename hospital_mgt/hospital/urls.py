
from django.urls import path
from .views import Home,About

urlpatterns = [
    path('', Home,name='home'),
    path('about/',About,name='about'),

    

]