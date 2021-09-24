from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
from django.core.validators import RegexValidator

class Designation(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.title)


class Staff(models.Model):
    STATUS_CHOICES = [("contract", "Contract"), ("permanent", "Permanent"), ("terminated", "Terminated")]

    GENDER_CHOICES = [("male", "Male"), ("female", "Female")]

    current_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="permanent")
    first_name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default="male")
    date_of_birth = models.DateField(default=timezone.now)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    expertise = models.CharField(max_length=250, blank=True)
    date_of_admission = models.DateField(default=timezone.now)
    
    mobile_num_regex = RegexValidator(regex="^[0-9]{10,15}$", message="Enter a valid phone number")
    mobile_number = models.CharField(validators=[mobile_num_regex], max_length=14, blank=False)
    email = models.EmailField(null=True)

    address = models.TextField(blank=False)
    others = models.TextField(blank=True)

    passport = models.ImageField(blank=True, upload_to="staff/passports/")

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return f"{self.last_name} {self.surname} {self.first_name} {self.designation}"

    def get_absolute_url(self):
        return reverse("staff-detail", kwargs={"pk": self.pk})
