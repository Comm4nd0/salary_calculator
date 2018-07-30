from django.db import models

# Create your models here.

class Calc(models.Model):
    # Yearly income
    gross_annual_salary = models.CharField(max_length=15)

