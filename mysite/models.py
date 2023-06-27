from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    deployment_url = models.URLField(max_length=255, blank=True)
    github_url = models.URLField(max_length=255, blank=True)
    image = models.ImageField(upload_to='static/images/', blank=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name


class ContactMe(models.Model):
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.email


class SocialLink(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField()

    def __str__(self):
        return self.name


class Education(models.Model):
    title = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    year = models.IntegerField(
        validators=[MinValueValidator(1990), MaxValueValidator(2023)]
    )
    overview = models.TextField()
    certificate = models.URLField()

    def __str__(self):
        return self.title


class WorkExperience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    year_start = models.IntegerField(
        validators=[MinValueValidator(1990), MaxValueValidator(2023)]
    )
    year_end = models.IntegerField(
        validators=[MinValueValidator(1990), MaxValueValidator(2023)]
    )
    overview = models.TextField()

    def __str__(self):
        return self.title


class SecondarySkill(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='static/secondary_skills/')

    def __str__(self):
        return self.name


class PrimarySkill(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='static/primary_skills/')

    def __str__(self):
        return self.name


class AboutMe(models.Model):
    paragraph_top = models.TextField()
    paragraph_bot = models.TextField()
    cv = models.FileField(upload_to='static/cv/')


class Profile(models.Model):
    name = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50, blank=True)
    overview = models.TextField(max_length=500, blank=True)
    nickname = models.CharField(max_length=10, blank=True)
    social_links = models.ManyToManyField(SocialLink)
    bio = models.OneToOneField(AboutMe, on_delete=models.CASCADE)
    primary_skills = models.ManyToManyField(PrimarySkill)
    secondary_skills = models.ManyToManyField(SecondarySkill)
    education = models.ManyToManyField(Education)
    projects = models.ManyToManyField(Project)
    work_experience = models.ManyToManyField(WorkExperience)
    contact = models.OneToOneField(
        ContactMe, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
