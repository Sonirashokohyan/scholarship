# Generated by Django 4.1.11 on 2023-10-31 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_projects_delete_yourmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='language_requirement',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='projects',
            name='last_date',
            field=models.DateField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='projects',
            name='organization',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]