from django.db import models
from django.contrib.auth.models import User

class MedicRecord(models.Model):
    full_name = models.CharField(max_length=120,null=True, blank=True)
    home_address = models.CharField(max_length=120, null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    occupation = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=15, null=True, blank=True)
    date_of_birth = models.DateField(max_length=8, auto_now_add=True, null=True, blank=True)

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)

    zip_code = models.IntegerField(null=True, blank=True)
    state = models.CharField(max_length=15, null=True, blank=True)


    def __str__(self):
        return self.first_name + '' + self.last_name