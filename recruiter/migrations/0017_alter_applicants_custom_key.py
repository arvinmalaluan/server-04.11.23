# Generated by Django 4.2.5 on 2023-10-15 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0016_applicants_custom_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicants',
            name='custom_key',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
    ]
