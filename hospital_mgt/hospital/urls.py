
from django.urls import path
from .views import Home,About,Contact,Login,Logout_admin,Index,View_Doctor,Delete_Doctor,Add_Doctor,View_Patient,Delete_Patient,Add_Patient,View_Appointment,Add_Appointment,Delete_Appointment

urlpatterns = [
    path('', Home,name='home'),
    path('about/',About,name='about'),
    path('contact/',Contact,name='contact'),

    path('admin_login/',Login,name='login'),
    path('logout/',Logout_admin,name='logout_admin'),

    path('index/',Index,name='dashboard'),

    path('view_doctor/',View_Doctor,name='view_doctor'),
    path('view_patient/',View_Patient,name='view_patient'),
    path('view_appointment/',View_Appointment,name='view_appointment'),


    path('add_doctor',Add_Doctor,name='add_doctor'),
    path('add_patient',Add_Patient,name='add_patient'),
    path('add_appointment',Add_Appointment,name='add_appointment'),


    path('delete_doctor/<int:pid>/', Delete_Doctor, name='delete_doctor'),
    path('delete_patient/<int:pid>/', Delete_Patient, name='delete_patient'),
    path('delete_appointment/<int:pid>/', Delete_Appointment, name='delete_appointment'),
]