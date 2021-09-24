import csv
import os
from io import StringIO

from django.dispatch import receiver
from django.db.models.signals import post_delete, post_save

from apps.departments.models import Stud_Class

from .models import Student, StudentBulkUpload


@receiver(post_save, sender=StudentBulkUpload)
def create_bulk_student(sender, created, instance, *args, **kwargs):
    if created:
        opened = StringIO(instance.csv_file.read().decode())
        reading = csv.DictReader(opened, delimiter=",")
        students = []
        for row in reading:
            if "registration_number" in row and row["registation_number"]:
                reg = row["registation_number"]
                first_name = row["first_name"] if "first_name" in row and row["first_name"] else ""
                surname =  row["surname"] if "surname" in row and row["surname"] else ""
                last_name = row["last_name"] if 'last_name' in row and row["last_name"] else ""
                gender = (row["gender"]).lower() if "gender" in row and row["gender"] else ""
                student_mobile = row["student_phone"] if "student_phone" in row and row["student_phone"] else ""
                parent_mobile = row["parent_phone"] if "parent_phone" in row and row["parent_phone"] else ""
                address = row["address"] if "address" in row and row["address"] else ""
                current_class = row["current_class"] if "current_class" in row and row["current_class"] else ""
                if current_class:
                    theclass, kind = Stud_Class.objects.get_or_create(name=current_class)
                
                check = Student.objects.filter(registration_number=reg).exists()
                if not check:
                    students.append(
                        Student(
                            registration_number=reg,
                            first_name=first_name,
                            surname=surname,
                            last_name=last_name,
                            gender=gender,
                            student_mobile=student_mobile,
                            parent_mobile=parent_mobile,
                            address=address,
                            current_status="active"
                        )
                    )

        Student.objects.bulk_create(students)
        instance.csv_file.close()
        instance.delete()


def _delete_file(path):
    """Deletes file from filesystem"""
    if os.path.isfile(path):
        os.remove(path)


@receiver(post_delete, sender=StudentBulkUpload)
def delete_csv_file(sender, instance, *args, **kwargs):
    if instance.csv_file:
        _delete_file(instance.csv_file.path)


@receiver(post_delete, sender=Student)
def delete_passport_on_delete(sender, instance, *args, **kwargs):
    if instance.passport:
        _delete_file(instance.passport.path)
