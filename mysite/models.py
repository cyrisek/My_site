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
