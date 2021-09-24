from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.core.validators import RegexValidator



class Staff(models.Model):
    STATUS_CHOICES = [("active", "Active"), ("inactive", "Inactive")]

    GENDER_CHOICES = [("male", "Male"), ("female", "Female")]

    current_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="active")
    first_name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField(default=timezone.now)
    date_of_admission = models.DateField(default=timezone.now)
    
    mobile_num_regex = RegexValidator(regex="^[0-9]{10,15}$", message="Enter a valid phone number")
    mobile_number = models.CharField(validators=[mobile_num_regex], max_length=14, blank=False)

    address = models.TextField(blank=False)
    others = models.TextField(blank=True)

    def __str__(self):
        return f"{self.last_name} {self.surname} {self.first_name}"

    def get_absolute_url(self):
        return reverse("staff-details", kwargs={"pk": self.pk})
