from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class AboutUs(models.Model):
    # information's
    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    website = models.URLField(max_length=200, blank=True)
    address = models.TextField(blank=True, null=True)
    description = models.TextField()
    # urls
    twitter_url = models.URLField(max_length=200, blank=True, null=True)
    facebook_url = models.URLField(max_length=200, blank=True, null=True)
    instagram_url = models.URLField(max_length=200, blank=True, null=True)
    github_url = models.URLField(max_length=200, blank=True, null=True)
    linkedin_url = models.URLField(max_length=200, blank=True, null=True)
    telegram_url = models.URLField(max_length=200, blank=True, null=True)

    cover = models.ImageField(upload_to='my_picture/', blank=True)

    def get_absolute_url(self):
        return reverse('home_url')


class WorkExperience(models.Model):
    job_title = models.CharField(max_length=150)
    company_name = models.CharField(max_length=150)

    start_work_time = models.CharField(max_length=150)
    end_work_time = models.CharField(max_length=150)

    description = models.TextField()

    def get_absolute_url(self):
        return reverse('home_url')


class Education(models.Model):
    education_title = models.CharField(max_length=150)
    college_name = models.CharField(max_length=150)

    start_work_time = models.CharField(max_length=150)
    end_work_time = models.CharField(max_length=150)

    description = models.TextField()

    def get_absolute_url(self):
        return reverse('home_url')


class MyProject(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    url = models.URLField(max_length=200, blank=True, null=True)

    cover = models.ImageField(upload_to='projects_covers/', blank=True)

    def get_absolute_url(self):
        return reverse('home_url')


class Contact(models.Model):
    author = models.ForeignKey(get_user_model(), models.CASCADE)
    text = models.TextField(verbose_name='Contact text:')

    def get_absolute_url(self):
        return reverse('home_url')

    def __str__(self):
        return "%s [%s]" % (self.text, self.author, )
