from django.db import models
from backend.models import SiteUser

class FinantialProduct(models.Model):
    name = models.CharField(max_length=50, unique=True)

class SavingLine(FinantialProduct):
    class Meta:
        proxy = True

class CreditLine(FinantialProduct):
    interest_rate = models.DecimalField(decimal_places=1, max_digits=4)

class ClientSavingProduct(models.Model):
    saving_line = models.ForeignKey(SavingLine)
    client = models.ForeignKey(SiteUser)
    savings_total = models.DecimalField(decimal_places=2, max_digits=11)
    quota = models.DecimalField(decimal_places=2, max_digits=10)
    salary_percent = models.DecimalField(decimal_places=2, max_digits=5)

class ClientCreditProduct(models.Model):
    credit_line = models.ForeignKey(CreditLine)
    client = models.ForeignKey(SiteUser)
    promisory_note = models.CharField(max_length=30)
    quota = models.DecimalField(decimal_places=2, max_digits=10)
    amount = models.DecimalField(decimal_places=2, max_digits=11)
    remaining_amount = models.DecimalField(decimal_places=2, max_digits=11)
    amortized_percent = models.DecimalField(decimal_places=2, max_digits=5)
    remaining_payments = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()