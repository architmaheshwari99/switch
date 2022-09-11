from django.db import models
from company.models import Company

# from user_profile.models import Skills
# Create your models here.

SALARY_CHOICE = ((1, '0L-5L'), (2, '5L-10L'), (3,'10L-20L'), (4, '20L-30L'), (5, '30L-40L'), (6, '40L+'),)
YOE_CHOICES = ((1, '< 1year'), (2,'1year-2year'), (3, '2year-3year'), (4, '3year-4year'), (5, '4year-6year'), (6, '6year+'),)
SECTOR_CHOICES = (('Engineering', 'Engineering'), ('Accounting', 'Accounting'),)

class Role(models.Model):
    position = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    sector = models.CharField(max_length=50, choices=SECTOR_CHOICES)


class City(models.Model):
    city = models.CharField(max_length=50, unique=True)
    state = models.CharField(max_length=50, blank=True, unique=True)
    country = models.CharField(max_length=50, blank=True, unique=True)

    def __str__(self):
        return self.cityP


class Job(models.Model):
    posted_by = models.ForeignKey("user_profile.Profile", on_delete=models.DO_NOTHING)
    vacancy = models.IntegerField(default=10)
    role = models.ForeignKey(Role, on_delete=models.DO_NOTHING)
    immediate_joiner_required = models.BooleanField(default=False)
    expected_salary = models.IntegerField(choices=SALARY_CHOICE)
    is_active = models.BooleanField(default=False)
    YOE = models.IntegerField(choices=YOE_CHOICES)
    perks_and_benefits = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField()
    rsu_provided = models.BooleanField(default= False)
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING, blank=True, null=True)
    city = models.ManyToManyField(City)
    skills = models.ManyToManyField("user_profile.Skills")

    def __str__(self):
        return self.role.position + " by " + self.posted_by.user.email

