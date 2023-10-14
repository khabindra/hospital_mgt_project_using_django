
from django.urls import path
from .views import Home,About,Contact

urlpatterns = [
    path('', Home,name='home'),
    path('about/',About,name='about'),
    path('contact/',Contact,name='contact'),

    

]