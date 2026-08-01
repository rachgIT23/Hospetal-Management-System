from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from base.models import *
from .serializers import *


# =====================================================
# DEPARTMENT API
# =====================================================

@api_view(['GET', 'POST'])
def department_create_read(request):

    if request.method == "GET":

        data = Department.objects.filter(is_deleted=False)
        serializer = DepartmentSerializer(data, many=True)
        return Response(serializer.data)

    elif request.method == "POST":

        serializer = DepartmentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def department_update_delete(request, pk):

    try:
        data = Department.objects.get(id=pk)

    except Department.DoesNotExist:

        return Response(
            {"error": "Department Not Found"},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == "GET":

        serializer = DepartmentSerializer(data)
        return Response(serializer.data)

    elif request.method == "PUT":

        serializer = DepartmentSerializer(
            data,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":

        data.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


# =====================================================
# DOCTOR API
# =====================================================

@api_view(['GET', 'POST'])
def doctor_create_read(request):

    if request.method == "GET":

        data = Doctor.objects.filter(is_deleted=False)
        serializer = DoctorSerializer(data, many=True)
        return Response(serializer.data)

    elif request.method == "POST":

        serializer = DoctorSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def doctor_update_delete(request, pk):

    try:
        data = Doctor.objects.get(id=pk)

    except Doctor.DoesNotExist:

        return Response(
            {"error": "Doctor Not Found"},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == "GET":

        serializer = DoctorSerializer(data)
        return Response(serializer.data)

    elif request.method == "PUT":

        serializer = DoctorSerializer(
            data,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":

        data.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


# =====================================================
# PATIENT API
# =====================================================

@api_view(['GET', 'POST'])
def patient_create_read(request):

    if request.method == "GET":

        data = Patient.objects.filter(is_deleted=False)
        serializer = PatientSerializer(data, many=True)
        return Response(serializer.data)

    elif request.method == "POST":

        serializer = PatientSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def patient_update_delete(request, pk):

    try:
        data = Patient.objects.get(id=pk)

    except Patient.DoesNotExist:

        return Response(
            {"error": "Patient Not Found"},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == "GET":

        serializer = PatientSerializer(data)
        return Response(serializer.data)

    elif request.method == "PUT":

        serializer = PatientSerializer(
            data,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":

        data.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


# =====================================================
# APPOINTMENT API
# =====================================================

@api_view(['GET', 'POST'])
def appointment_create_read(request):

    if request.method == "GET":

        data = Appointment.objects.filter(is_deleted=False)
        serializer = AppointmentSerializer(data, many=True)
        return Response(serializer.data)

    elif request.method == "POST":

        serializer = AppointmentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def appointment_update_delete(request, pk):

    try:
        data = Appointment.objects.get(id=pk)

    except Appointment.DoesNotExist:

        return Response(
            {"error": "Appointment Not Found"},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == "GET":

        serializer = AppointmentSerializer(data)
        return Response(serializer.data)

    elif request.method == "PUT":

        serializer = AppointmentSerializer(
            data,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":

        data.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


# =====================================================
# MEDICAL RECORD API
# =====================================================

@api_view(['GET', 'POST'])
def record_create_read(request):

    if request.method == "GET":

        data = MedicalRecord.objects.filter(is_deleted=False)
        serializer = MedicalRecordSerializer(data, many=True)
        return Response(serializer.data)

    elif request.method == "POST":

        serializer = MedicalRecordSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def record_update_delete(request, pk):

    try:
        data = MedicalRecord.objects.get(id=pk)

    except MedicalRecord.DoesNotExist:

        return Response(
            {"error": "Medical Record Not Found"},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == "GET":

        serializer = MedicalRecordSerializer(data)
        return Response(serializer.data)

    elif request.method == "PUT":

        serializer = MedicalRecordSerializer(
            data,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":

        data.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)