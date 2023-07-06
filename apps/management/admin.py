from django.contrib import admin
from .models import AcademicSession, AcademicTerm

# Register your models here.
admin.site.register(AcademicSession)
admin.site.register(AcademicTerm)