import os
import random

import django

# must be on top of django.setup()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()
from faker import Faker

# must come after django setup()
from apps.staff.models import Designation, Staff

fakegen = Faker()


def create_designations():
    designations = [
        "Head",
        "Deputy",
        "H.O.D",
        "Senior Teacher",
        "Counsellor",
        "Director",
        "Driver",
        "Surbodinate",
    ]
    for des in designations:
        Designation.objects.get_or_create(title=des)


create_designations()

# designations
designations = []
for i in range(1, 6):
    des = Designation.objects.get(id=i)
    designations.append(des)


def generate_staff():
    for entry in range(10):
        first_name = fakegen.first_name()
        name = fakegen.last_name_nonbinary()
        last_name = fakegen.last_name()
        des = random.choice(designations)
        mobile = fakegen.phone_number()
        email = fakegen.email()
        address = fakegen.address()

        try:
            staff = Staff.objects.get_or_create(
                first_name=first_name,
                surname=name,
                last_name=last_name,
                designation=des,
                mobile_number=mobile,
                email=email,
                address=address,
            )
        except:
            continue


if __name__ == "__main__":
    print("Creating Fake Staff....")
    generate_staff()
    print("Members of staff created successfully.")
