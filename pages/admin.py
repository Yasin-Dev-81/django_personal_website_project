from django.contrib import admin
from . import models


@admin.register(models.AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'website']


@admin.register(models.WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ['job_title', 'company_name', ]


@admin.register(models.Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['education_title', 'college_name', ]


@admin.register(models.MyProject)
class MyProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', ]
