# Generated by Django 4.1.2 on 2022-10-10 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='telegram_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
