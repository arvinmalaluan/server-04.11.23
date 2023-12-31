# Generated by Django 4.2.5 on 2023-10-09 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seekerFolder', '0015_remove_comments_profile_engagement_engager_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allprofile',
            name='bio',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='allprofile',
            name='comp_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='allprofile',
            name='comp_overview',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='allprofile',
            name='emp_count',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='allprofile',
            name='location',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='allprofile',
            name='site_link',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='allprofile',
            name='subsidiaries_count',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
