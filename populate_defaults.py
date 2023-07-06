import random
import django
import os
# must be in top of django.setup()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()
from faker import Faker
# must come after django.setup()
from apps.management.models import AcademicSession, AcademicTerm



fakegen = Faker()

def generate_session_and_term():

        try:
            session , _ = AcademicSession.objects.get_or_create(
                name='2019/2020',)
        except:
            pass

        try:
            term , _ = AcademicTerm.objects.get_or_create(
                name='First Term',)
        except:
            pass


if __name__ == "__main__":
    print('Creating Default data....')
    generate_session_and_term()
    print('data are created.')
    
