from django.urls import path
from . import views

urlpatterns = [

    # ==========================
    # Department
    # ==========================

    path(
        'departments/',
        views.department_create_read,
        name='department_create_read'
    ),

    path(
        'departments/<int:pk>/',
        views.department_update_delete,
        name='department_update_delete'
    ),

    # ==========================
    # Doctor
    # ==========================

    path(
        'doctors/',
        views.doctor_create_read,
        name='doctor_create_read'
    ),

    path(
        'doctors/<int:pk>/',
        views.doctor_update_delete,
        name='doctor_update_delete'
    ),

    # ==========================
    # Patient
    # ==========================

    path(
        'patients/',
        views.patient_create_read,
        name='patient_create_read'
    ),

    path(
        'patients/<int:pk>/',
        views.patient_update_delete,
        name='patient_update_delete'
    ),

    # ==========================
    # Appointment
    # ==========================

    path(
        'appointments/',
        views.appointment_create_read,
        name='appointment_create_read'
    ),

    path(
        'appointments/<int:pk>/',
        views.appointment_update_delete,
        name='appointment_update_delete'
    ),

    # ==========================
    # Medical Record
    # ==========================

    path(
        'records/',
        views.record_create_read,
        name='record_create_read'
    ),

    path(
        'records/<int:pk>/',
        views.record_update_delete,
        name='record_update_delete'
    ),

]