from django.core.management.base import BaseCommand

from publications.models import Publication
from accounts.models import User

import string
import random


class Command(BaseCommand):
    def handle(self, *args, **options):
        for i in range(1000):
            Publication.objects.create(title="Title" + "".join([random.choice(string.digits) for i in range(5)]),
                                       body="".join([random.choice(string.ascii_letters) for i in range(255)]),
                                       image="",
                                       author=User.objects.get(pk=1))
            print(i)
