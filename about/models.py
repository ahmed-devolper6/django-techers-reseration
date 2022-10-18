from django.db import models

# Create your models here.
class info(models.Model):
    company_number = models.IntegerField()
    company_country = models.CharField(max_length=15)
    company_city = models.CharField(max_length=15)
    company_email = models.IntegerField()
