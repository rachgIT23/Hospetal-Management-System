from django.db import models


# -----------------------------
# Department Model
# -----------------------------
class Department(models.Model):

    department_name = models.CharField(max_length=100)
    description = models.TextField()

    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.department_name


# -----------------------------
# Doctor Model
# -----------------------------
class Doctor(models.Model):

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    doctor_name = models.CharField(max_length=100)

    specialization = models.CharField(max_length=100)

    experience = models.PositiveIntegerField()

    phone = models.CharField(max_length=10)

    email = models.EmailField()

    doctor_image = models.ImageField(
        upload_to="doctor_images",
        null=True,
        blank=True
    )

    is_deleted = models.BooleanField(default=False)

    deleted_at = models.DateTimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.doctor_name


# -----------------------------
# Patient Model
# -----------------------------
class Patient(models.Model):

    patient_name = models.CharField(max_length=100)

    age = models.PositiveIntegerField()

    gender = models.CharField(
        max_length=20
    )

    phone = models.CharField(
        max_length=10
    )

    email = models.EmailField()

    address = models.TextField()

    patient_image = models.ImageField(
        upload_to="patient_images",
        null=True,
        blank=True
    )

    is_deleted = models.BooleanField(
        default=False
    )

    deleted_at = models.DateTimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.patient_name


# -----------------------------
# Appointment Model
# -----------------------------
class Appointment(models.Model):

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE
    )

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE
    )

    appointment_date = models.DateField()

    appointment_time = models.TimeField()

    status = models.CharField(
        max_length=50,
        choices=[
            ("Pending", "Pending"),
            ("Completed", "Completed"),
            ("Cancelled", "Cancelled")
        ],
        default="Pending"
    )

    is_deleted = models.BooleanField(
        default=False
    )

    deleted_at = models.DateTimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.patient} - {self.doctor}"


# -----------------------------
# Medical Record Model
# -----------------------------
class MedicalRecord(models.Model):

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE
    )

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE
    )

    diagnosis = models.TextField()

    prescription = models.TextField()

    report = models.FileField(
        upload_to="medical_reports",
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    is_deleted = models.BooleanField(
        default=False
    )

    deleted_at = models.DateTimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.patient.patient_name