from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    annual_income = models.DecimalField(max_digits=15, decimal_places=2)
    aadhar_id = models.CharField(max_length=12, unique=True)
    credit_score = models.IntegerField(default=0)

    def __str__(self):
        return self.name
