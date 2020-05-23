from django.db import models


class Student(models.Model):
    register_number = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=257)

    def __str__(self):
        return self.register_number

    def name(self):
        return self.first_name + ' ' + self.last_name
