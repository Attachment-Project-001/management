from apps.students.models import Student
from apps.staff.models import Staff
from django.db import models
from django.utils import timezone
from django.conf import settings


class SiteConfig(models.Model):
    """Site Configurations"""

    key = models.SlugField()
    value = models.CharField(max_length=250)

    def __str__(self):
        return self.key


class Department(models.Model):
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=50, unique=True)
    head = models.ForeignKey(Staff, on_delete=models.CASCADE, blank=True, null=True)
    establish_date = models.DateField(default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True)

    def dept_code(self):
        if not self.code:
            return ""
        return self.code

    def __str__(self):
        return str(self.name)


class AcademicSession(models.Model):
    '''Academic Session'''
    name = models.CharField(max_length=200, unique=True)
    current = models.BooleanField(default=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True)    

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class AcademicTerm(models.Model):
    '''Academic Term'''
    name = models.CharField(max_length=20, unique=True)
    guide = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True, default=None)
    current = models.BooleanField(default=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Subject(models.Model):
    '''Subject'''
    name = models.CharField(max_length=150, unique=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class SubjectAssignToTeacher(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING, null=True)
    teacher = models.ManyToManyField(Staff)
    assign_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True)

    def __int__(self):
        return self.id


class SubjectAssignToStudent(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING, null=True)
    student = models.ManyToManyField(Student)
    assigned_by = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True)

    def __int__(self):
        return self.id


class Stud_Class(models.Model):
    name = models.CharField(max_length=200, unique=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True)

    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"
        ordering = ['name']

    def __str__(self):
        return self.name


class DailyAttendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    teacher = models.ForeignKey(Staff, on_delete=models.DO_NOTHING)
    is_present = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)