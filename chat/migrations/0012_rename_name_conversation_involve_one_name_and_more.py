# Generated by Django 4.2.5 on 2023-10-11 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0011_alter_conversation_involve_one_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conversation',
            old_name='name',
            new_name='involve_one_name',
        ),
        migrations.RenameField(
            model_name='conversation',
            old_name='profile',
            new_name='profile_one',
        ),
        migrations.AddField(
            model_name='conversation',
            name='involve_two_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='conversation',
            name='profile_two',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
