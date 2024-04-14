from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Transaction(models.Model):
    user = models.CharField(max_length=100)
    date = models.DateField()
    type = models.CharField(max_length=10)
    amount = models.IntegerField()

    def clean(self):
        super().clean()
        if self.type not in ['DEBIT', 'CREDIT']:
            raise ValidationError('The value of type must be either "DEBIT" or "CREDIT"')