import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','protwo.settings')

import django
django.setup()

from apptwo.models import user
from faker import Faker
fakegen=Faker()

def populate(N=5):
    for i in range(N):
        fake_name=fakegen.name().split()
        fake_first=fake_name[0]
        fake_second=fake_name[1]
        fake_email=fakegen.email()


        user1=user.objects.get_or_create(first_name=fake_first,last_name=fake_second,email=fake_email)[0]
if __name__ == '__main__':
    print('populating')
    populate(20)
    print('populated')
