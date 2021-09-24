from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.core.validators import RegexValidator

# from apps.management.models import Stud_Class


class Student(models.Model):
    STATUS_CHOICES = [("active", "Active"), ("inactive", "Inactive")]

    GENDER_CHOICES = [("male", "Male"), ("female", "Female")]

    current_status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="active")
    registration_number = models.CharField(max_length=200, unique=True)
    first_name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default="male")
    date_of_birth = models.DateField(default=timezone.now)
    current_class = models.ForeignKey(to="management.Stud_Class", on_delete=models.SET_NULL, blank=True, null=True)
    date_of_admission = models.DateField(default=timezone.now)

    mobile_num_regex = RegexValidator(
        regex="^[0-9]{10,15}$", message="Enter a valid phone number")
    student_mobile = models.CharField(
        validators=[mobile_num_regex], max_length=14, blank=False)
    student_email = models.EmailField(null=True)
    parent_mobile = models.CharField(
        validators=[mobile_num_regex], max_length=14, blank=True)
    parent_email = models.EmailField(null=True)

    address = models.TextField(blank=True)
    passport = models.ImageField(blank=True, upload_to="students/passports/")

    class Meta:
        ordering = ["last_name", "surname", "first_name"]

    def __str__(self):
        return f"{self.last_name} {self.surname} {self.first_name}  ({self.registration_number})"

    def get_absolute_url(self):
        return reverse("student-detail", kwargs={"pk": self.pk})


class StudentBulkUpload(models.Model):
    date_uploaded = models.DateTimeField(auto_now=True)
    csv_file = models.FileField(upload_to="students/bulkupload/")
