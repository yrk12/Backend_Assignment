from django.db import models

# Create your models here.
class Loan(models.Model):
    unique_user_id = models.IntegerField(editable=False, unique=True)
    loan_type = models.CharField(max_length=20, default='CREDIT')
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    term_period = models.IntegerField()
    disbursement_date = models.DateField()


class Dues(models.Model):
    loan_id = models.IntegerField()
    date = models.DateField(null=True)
    paid = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    month_number = models.IntegerField()