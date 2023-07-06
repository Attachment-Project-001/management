import random
import django
import os
# must be in top of django.setup()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()
from faker import Faker
# must come after django.setup()
from apps.students.models import Student


fakegen = Faker()

def generate_students():
    for entry in range(10):
        first_name = fakegen.first_name()
        name = fakegen.last_name_nonbinary()
        last_name = fakegen.last_name()
        regi = fakegen.random_int(min=10000, max=99999, step=1)
        mobile = fakegen.phone_number()
        guardian = fakegen.phone_number()

        try:
            student = Student.objects.get_or_create(
                first_name=first_name,
                surname=name,
                last_name=last_name,
                registration_number=regi,
                student_mobile=mobile,
                parent_mobile=guardian)
        except:
            continue


if __name__ == "__main__":
    print('Creating Fake Students....')
    generate_students()
    print('students are created.')
    
