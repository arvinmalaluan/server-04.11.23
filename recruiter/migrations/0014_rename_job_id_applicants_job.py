# Generated by Django 4.2.5 on 2023-10-15 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0013_remove_applicants_applicount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applicants',
            old_name='job_id',
            new_name='job',
        ),
    ]
