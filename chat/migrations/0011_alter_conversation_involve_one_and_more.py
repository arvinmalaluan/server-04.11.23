# Generated by Django 4.2.5 on 2023-10-11 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seekerFolder', '0028_alter_allprofile_account'),
        ('chat', '0010_alter_conversation_involve_one_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='involve_one',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='conversations_one', to='seekerFolder.allprofile'),
        ),
        migrations.AlterField(
            model_name='conversation',
            name='involve_two',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='conversations_two', to='seekerFolder.allprofile'),
        ),
    ]
