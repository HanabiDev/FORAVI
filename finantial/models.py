from django.db import models
from backend.models import SiteUser

class FinantialProduct(models.Model):
    name = models.CharField(max_length=50)

class SavingLine(FinantialProduct):
    quota_base = models.DecimalField(decimal_places=2, max_digits=2)

class CreditLine(FinantialProduct):
    interest_rate = models.DecimalField(decimal_places=1, max_digits=3)

class ClientSavingProduct(models.Model):
    saving_line = models.ForeignKey(SavingLine)
    client = models.ForeignKey(SiteUser)
    savings_total = models.DecimalField(decimal_places=2, max_digits=9)
    quota = models.DecimalField(decimal_places=2, max_digits=8)

class ClientCreditProduct(models.Model):
    credit_line = models.ForeignKey(CreditLine)
    client = models.ForeignKey(SiteUser)
    promisory_note = models.CharField(max_length=30)
    quota = models.DecimalField(decimal_places=2, max_digits=8)
    amount = models.DecimalField(decimal_places=2, max_digits=9)
    amortized_amount = models.DecimalField(decimal_places=2, max_digits=9)
    amortized_percent = models.DecimalField(decimal_places=2, max_digits=3)
    start_date = models.DateField()
    end_date = models.DateField()