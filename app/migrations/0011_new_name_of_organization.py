# Generated by Django 4.1.11 on 2023-11-09 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_new_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='name_of_organization',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
