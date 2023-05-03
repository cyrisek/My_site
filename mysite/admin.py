from django.contrib import admin
from .models import Project, Contact, SocialLink, Education, WorkExperience, PrimarySkill, SecondarySkill, AboutMe, Profile, ContactMe

# Register your models here.

admin.site.register(Project)
admin.site.register(Contact)
admin.site.register(ContactMe)
admin.site.register(SocialLink)
admin.site.register(Education)
admin.site.register(WorkExperience)
admin.site.register(PrimarySkill)
admin.site.register(SecondarySkill)
admin.site.register(AboutMe)
admin.site.register(Profile)
