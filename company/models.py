from django.db import models

# Create your models here.

class Sector(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    sector_name = models.CharField(max_length=255)

    def __str__(self):
        return self.sector_name



class Company(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    company_name = models.CharField(max_length=255, unique=True)
    sector = models.ForeignKey(Sector, on_delete=models.DO_NOTHING)
    valuation = models.CharField(max_length=5, blank=True, null=True)
    glassdoor = models.FloatField(blank=True, null=True)
    no_of_employees = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.company_name