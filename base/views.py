from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib import messages

from .models import *
from .forms import *


# ==========================================================
# DEPARTMENT
# ==========================================================

# CREATE
def create_department(request):

    form = DepartmentForm(request.POST or None)

    if form.is_valid():

        form.save()

        messages.success(request, "Department Added Successfully")

        return redirect("department_list")

    return render(
        request,
        "create_department.html",
        {
            "form": form
        }
    )


# READ
def department_list(request):

    data = Department.objects.filter(is_deleted=False)

    return render(
        request,
        "department_list.html",
        {
            "data": data
        }
    )


# UPDATE
def update_department(request, pk):

    data = get_object_or_404(
        Department,
        id=pk
    )

    if request.method == "POST":

        form = DepartmentForm(
            request.POST,
            instance=data
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Department Updated Successfully"
            )

            return redirect(
                "department_list"
            )

    else:

        form = DepartmentForm(
            instance=data
        )

    return render(
        request,
        "update_department.html",
        {
            "form": form
        }
    )


# DELETE
def delete_department(request, pk):

    data = get_object_or_404(
        Department,
        id=pk
    )

    if request.method == "POST":

        data.is_deleted = True

        data.deleted_at = timezone.now()

        data.save()

        messages.success(
            request,
            "Department Deleted Successfully"
        )

        return redirect(
            "department_list"
        )

    return render(
        request,
        "delete_department.html",
        {
            "data": data
        }
    )


# HISTORY
def department_history(request):

    data = Department.objects.filter(
        is_deleted=True
    )

    return render(
        request,
        "department_history.html",
        {
            "data": data
        }
    )


# RESTORE
def restore_department(request, pk):

    data = get_object_or_404(
        Department,
        id=pk,
        is_deleted=True
    )

    data.is_deleted = False

    data.deleted_at = None

    data.save()

    messages.success(
        request,
        "Department Restored Successfully"
    )

    return redirect(
        "department_history"
    )
# ==========================================================
# DOCTOR
# ==========================================================

# CREATE
def create_doctor(request):

    if request.method == "POST":

        form = DoctorForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Doctor Added Successfully"
            )

            return redirect("doctor_list")

    else:

        form = DoctorForm()

    return render(
        request,
        "create_doctor.html",
        {
            "form": form
        }
    )


# READ
def doctor_list(request):

    data = Doctor.objects.filter(
        is_deleted=False
    )

    return render(
        request,
        "doctor_list.html",
        {
            "data": data
        }
    )


# UPDATE
def update_doctor(request, pk):

    data = get_object_or_404(
        Doctor,
        id=pk
    )

    if request.method == "POST":

        form = DoctorForm(
            request.POST,
            request.FILES,
            instance=data
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Doctor Updated Successfully"
            )

            return redirect("doctor_list")

    else:

        form = DoctorForm(
            instance=data
        )

    return render(
        request,
        "update_doctor.html",
        {
            "form": form
        }
    )


# DELETE
def delete_doctor(request, pk):

    data = get_object_or_404(
        Doctor,
        id=pk
    )

    if request.method == "POST":

        data.is_deleted = True

        data.deleted_at = timezone.now()

        data.save()

        messages.success(
            request,
            "Doctor Deleted Successfully"
        )

        return redirect("doctor_list")

    return render(
        request,
        "delete_doctor.html",
        {
            "data": data
        }
    )


# HISTORY
def doctor_history(request):

    data = Doctor.objects.filter(
        is_deleted=True
    )

    return render(
        request,
        "doctor_history.html",
        {
            "data": data
        }
    )


# RESTORE
def restore_doctor(request, pk):

    data = get_object_or_404(
        Doctor,
        id=pk,
        is_deleted=True
    )

    data.is_deleted = False

    data.deleted_at = None

    data.save()

    messages.success(
        request,
        "Doctor Restored Successfully"
    )

    return redirect("doctor_history")
# ==========================================================
# PATIENT
# ==========================================================

# CREATE
def create_patient(request):

    if request.method == "POST":

        form = PatientForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Patient Added Successfully"
            )

            return redirect("patient_list")

    else:

        form = PatientForm()

    return render(
        request,
        "create_patient.html",
        {
            "form": form
        }
    )


# READ
def patient_list(request):

    data = Patient.objects.filter(
        is_deleted=False
    )

    return render(
        request,
        "patient_list.html",
        {
            "data": data
        }
    )


# UPDATE
def update_patient(request, pk):

    data = get_object_or_404(
        Patient,
        id=pk
    )

    if request.method == "POST":

        form = PatientForm(
            request.POST,
            request.FILES,
            instance=data
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Patient Updated Successfully"
            )

            return redirect("patient_list")

    else:

        form = PatientForm(
            instance=data
        )

    return render(
        request,
        "update_patient.html",
        {
            "form": form
        }
    )


# DELETE
def delete_patient(request, pk):

    data = get_object_or_404(
        Patient,
        id=pk
    )

    if request.method == "POST":

        data.is_deleted = True

        data.deleted_at = timezone.now()

        data.save()

        messages.success(
            request,
            "Patient Deleted Successfully"
        )

        return redirect("patient_list")

    return render(
        request,
        "delete_patient.html",
        {
            "data": data
        }
    )


# HISTORY
def patient_history(request):

    data = Patient.objects.filter(
        is_deleted=True
    )

    return render(
        request,
        "patient_history.html",
        {
            "data": data
        }
    )


# RESTORE
def restore_patient(request, pk):

    data = get_object_or_404(
        Patient,
        id=pk,
        is_deleted=True
    )

    data.is_deleted = False

    data.deleted_at = None

    data.save()

    messages.success(
        request,
        "Patient Restored Successfully"
    )

    return redirect("patient_history")
# ==========================================================
# APPOINTMENT
# ==========================================================

# CREATE
def create_appointment(request):

    if request.method == "POST":

        form = AppointmentForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("appointment_list")

        else:

            print(form.errors)   # 👈 Add this line here

    else:

        form = AppointmentForm()

    return render(
        request,
        "create_appointment.html",
        {
            "form": form
        }
    )


# READ
def appointment_list(request):

    data = Appointment.objects.filter(
        is_deleted=False
    )

    return render(
        request,
        "appointment_list.html",
        {
            "data": data
        }
    )


# UPDATE
def update_appointment(request, pk):

    data = get_object_or_404(
        Appointment,
        id=pk
    )

    if request.method == "POST":

        form = AppointmentForm(
            request.POST,
            instance=data
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Appointment Updated Successfully"
            )

            return redirect(
                "appointment_list"
            )

    else:

        form = AppointmentForm(
            instance=data
        )

    return render(
        request,
        "update_appointment.html",
        {
            "form": form
        }
    )


# DELETE
def delete_appointment(request, pk):

    data = get_object_or_404(
        Appointment,
        id=pk
    )

    if request.method == "POST":

        data.is_deleted = True

        data.deleted_at = timezone.now()

        data.save()

        messages.success(
            request,
            "Appointment Deleted Successfully"
        )

        return redirect(
            "appointment_list"
        )

    return render(
        request,
        "delete_appointment.html",
        {
            "data": data
        }
    )


# HISTORY
def appointment_history(request):

    data = Appointment.objects.filter(
        is_deleted=True
    )

    return render(
        request,
        "appointment_history.html",
        {
            "data": data
        }
    )


# RESTORE
def restore_appointment(request, pk):

    data = get_object_or_404(
        Appointment,
        id=pk,
        is_deleted=True
    )

    data.is_deleted = False

    data.deleted_at = None

    data.save()

    messages.success(
        request,
        "Appointment Restored Successfully"
    )

    return redirect(
        "appointment_history"
    )
# ==========================================================
# MEDICAL RECORD
# ==========================================================

# CREATE
def create_record(request):

    if request.method == "POST":

        form = MedicalRecordForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Medical Record Added Successfully"
            )

            return redirect("record_list")

    else:

        form = MedicalRecordForm()

    return render(
        request,
        "create_record.html",
        {
            "form": form
        }
    )


# READ
def record_list(request):

    data = MedicalRecord.objects.filter(
        is_deleted=False
    )

    return render(
        request,
        "record_list.html",
        {
            "data": data
        }
    )


# UPDATE
def update_record(request, pk):

    data = get_object_or_404(
        MedicalRecord,
        id=pk
    )

    if request.method == "POST":

        form = MedicalRecordForm(
            request.POST,
            request.FILES,
            instance=data
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Medical Record Updated Successfully"
            )

            return redirect("record_list")

    else:

        form = MedicalRecordForm(
            instance=data
        )

    return render(
        request,
        "update_record.html",
        {
            "form": form
        }
    )


# DELETE
def delete_record(request, pk):

    data = get_object_or_404(
        MedicalRecord,
        id=pk
    )

    if request.method == "POST":

        data.is_deleted = True

        data.deleted_at = timezone.now()

        data.save()

        messages.success(
            request,
            "Medical Record Deleted Successfully"
        )

        return redirect("record_list")

    return render(
        request,
        "delete_record.html",
        {
            "data": data
        }
    )


# HISTORY
def record_history(request):

    data = MedicalRecord.objects.filter(
        is_deleted=True
    )

    return render(
        request,
        "record_history.html",
        {
            "data": data
        }
    )


# RESTORE
def restore_record(request, pk):

    data = get_object_or_404(
        MedicalRecord,
        id=pk,
        is_deleted=True
    )

    data.is_deleted = False

    data.deleted_at = None

    data.save()

    messages.success(
        request,
        "Medical Record Restored Successfully"
    )

    return redirect("record_history")