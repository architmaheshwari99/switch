from django.contrib import admin

from user_profile.models import Profile, ProfessionalExperience, Education
# Register your models here.
admin.site.register(Profile)
admin.site.register(ProfessionalExperience)
admin.site.register(Education)