# Generated by Django 4.2.5 on 2023-09-30 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_alter_conversation_custom_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='custom_key',
            field=models.CharField(default=2419, max_length=20),
            preserve_default=False,
        ),
    ]
