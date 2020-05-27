from django.db import models
from random import randint


def random_code():
    d = randint(1000000, 100000000)
    return hex(d)[2:8]


class Institute(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    institute_code = models.CharField(
        max_length=20, default=random_code, unique=True)
    password = models.CharField(max_length=257)
