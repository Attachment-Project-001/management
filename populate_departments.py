import django
import os
# must be in top of django.setup()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()
# must come after django.setup()
from faker import Faker

from apps.management.models import Department
from apps.staff.models import Staff
import random

fakegen = Faker()


names = [
    'Computer', 'Mathematics', 'Science', 'Sports',
    'Languages', 'Social and Religious Education',
    'Guidance and Counselling', 'Agriculture'
]


def generate_departments(n=10):
    for entry in range(n):
        name = random.choice(names)
        code = fakegen.random_int(min=10000, max=99999, step=1)
        lead = random.choices(Staff)

        try:
            department = Department.objects.get_or_create(
                name=name,
                code=code,
                head=lead)
        except:
            continue


if __name__ == "__main__":
    print('Creating departments....')
    print('Departments created successfully!')