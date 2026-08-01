from django.urls import path
from . import views

urlpatterns = [

    # ==========================
    # HOME
    # ==========================
    path('', views.create_department, name='home'),

    # ==========================
    # DEPARTMENT
    # ==========================
    path('create_department/', views.create_department, name='create_department'),
    path('department_list/', views.department_list, name='department_list'),
    path('update_department/<int:pk>/', views.update_department, name='update_department'),
    path('delete_department/<int:pk>/', views.delete_department, name='delete_department'),
    path('department_history/', views.department_history, name='department_history'),
    path('restore_department/<int:pk>/', views.restore_department, name='restore_department'),

    # ==========================
    # DOCTOR
    # ==========================
    path('create_doctor/', views.create_doctor, name='create_doctor'),
    path('doctor_list/', views.doctor_list, name='doctor_list'),
    path('update_doctor/<int:pk>/', views.update_doctor, name='update_doctor'),
    path('delete_doctor/<int:pk>/', views.delete_doctor, name='delete_doctor'),
    path('doctor_history/', views.doctor_history, name='doctor_history'),
    path('restore_doctor/<int:pk>/', views.restore_doctor, name='restore_doctor'),

    # ==========================
    # PATIENT
    # ==========================
    path('create_patient/', views.create_patient, name='create_patient'),
    path('patient_list/', views.patient_list, name='patient_list'),
    path('update_patient/<int:pk>/', views.update_patient, name='update_patient'),
    path('delete_patient/<int:pk>/', views.delete_patient, name='delete_patient'),
    path('patient_history/', views.patient_history, name='patient_history'),
    path('restore_patient/<int:pk>/', views.restore_patient, name='restore_patient'),

    # ==========================
    # APPOINTMENT
    # ==========================
    path('create_appointment/', views.create_appointment, name='create_appointment'),
    path('appointment_list/', views.appointment_list, name='appointment_list'),
    path('update_appointment/<int:pk>/', views.update_appointment, name='update_appointment'),
    path('delete_appointment/<int:pk>/', views.delete_appointment, name='delete_appointment'),
    path('appointment_history/', views.appointment_history, name='appointment_history'),
    path('restore_appointment/<int:pk>/', views.restore_appointment, name='restore_appointment'),

    # ==========================
    # MEDICAL RECORD
    # ==========================
    path('create_record/', views.create_record, name='create_record'),
    path('record_list/', views.record_list, name='record_list'),
    path('update_record/<int:pk>/', views.update_record, name='update_record'),
    path('delete_record/<int:pk>/', views.delete_record, name='delete_record'),
    path('record_history/', views.record_history, name='record_history'),
    path('restore_record/<int:pk>/', views.restore_record, name='restore_record'),
]