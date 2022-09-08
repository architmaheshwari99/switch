from django.db import models

from user_profile.models import Profile
# Create your models here.

SALARY_CHOICE = (('0L-5L', 1), ('5L-10L', 2), ('10L-20L', 3), ('20L-30L',4), ('30L-40L', 5), ('40L+', 6),)
YOE_CHOICES = (('< 1year', 1), ('1year-2year', 2), ('2year-3year', 3), ('3year-4year', 4), ('4year-6year', 5), ('6year+', 6),)
SECTOR_CHOICES = (('Engineering', 'Engineering'), ('Accounting', 'Accounting'),)

class Role(models.Model):
    position = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    sector = models.CharField(max_length=50, choices=SECTOR_CHOICES)


class Job(models.Model):
    posted_by = models.ForeignKey(Profile, on_delete=models.CASCADE)
    vacancy = models.IntegerField(default=10)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    immediate_joiner_required = models.BooleanField(default=False)
    expected_salary = models.CharField(max_length=10, choices=SALARY_CHOICE)
    is_active = models.BooleanField(default=False)
    YOE = models.CharField(max_length=10, choices=YOE_CHOICES)
    perks_and_benefits = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.role.position + " by " + self.posted_by.user.email


class City(models.Model):
    name = models.CharField(max_length=50, unique=True)
    jobs = models.ManyToManyField(Job)