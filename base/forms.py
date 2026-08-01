from django import forms
from .models import *


# ---------------- Department ----------------

class DepartmentForm(forms.ModelForm):

    class Meta:
        model = Department
        fields = "__all__"
        exclude = ['is_deleted', 'deleted_at']


# ---------------- Doctor ----------------

class DoctorForm(forms.ModelForm):

    class Meta:
        model = Doctor
        fields = "__all__"
        exclude = ['is_deleted', 'deleted_at']


# ---------------- Patient ----------------

class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = "__all__"
        exclude = ['is_deleted', 'deleted_at']


# ---------------- Appointment ----------------



class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        exclude = ['is_deleted', 'deleted_at']

        widgets = {
            'appointment_date': forms.DateInput(
                attrs={'type': 'date'}
            ),
            'appointment_time': forms.TimeInput(
                attrs={'type': 'time'}
            ),
        }

# ---------------- Medical Record ----------------

class MedicalRecordForm(forms.ModelForm):

    class Meta:
        model = MedicalRecord
        fields = "__all__"
        exclude = ['is_deleted', 'deleted_at']