from django.db import models

from account.models import Account
from job.models import Role

DegreeChoices = (
    ('NA','NA'),
    ('BTECH', 'BTECH'),
    ('MTECH', 'MTECH'),
)

# Create your models here.
class Profile(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(Account, on_delete=models.DO_NOTHING)
    bio = models.CharField(max_length=255, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    phone_no = models.CharField(max_length=10, blank=True, null=True)
    achievements = models.CharField(max_length=256, blank=True, null=True)
    profile_photo = models.ImageField(upload_to='profile/', blank=True)
    daily_credit = models.IntegerField(default=10)
    company_email_address = models.EmailField(max_length=255, blank=True, null=True)
    resume = models.FileField(upload_to='profile/')
    is_recruiter = models.BooleanField(default=False)
    skills = models.ManyToManyField('Skills', through='ProfileSkillProciency')

    def __str__(self):
        return self.user.email 

    
class Education(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    profile = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    college = models.CharField(max_length=50, null=True)
    branch = models.CharField(max_length=30, null=True)
    graduation_year = models.IntegerField()
    cgpa = models.FloatField()
    #TODO: Think of a better default
    degree = models.CharField(max_length=20, choices= DegreeChoices, default='NA')

    def __str__(self):
        return str(self.profile.user.email) + " " + str(self.college)



class ProfessionalExperience(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    profile = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    company_name = models.CharField(max_length=50)
    years_of_experience = models.FloatField()
    role = models.ForeignKey(Role, on_delete=models.DO_NOTHING, default=True, blank=True) 

    def __str__(self):
        return self.profile.user.email + " " + self.company_name

class Skills(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    skill_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.skill_name

class ProfileSkillProciency(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    skill = models.ForeignKey(Skills, on_delete=models.DO_NOTHING)
    proficiency = models.IntegerField()
    profile = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    is_active = models.BooleanField(default=True)