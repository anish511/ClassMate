# Generated by Django 4.0.1 on 2022-04-08 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_alter_message_options_alter_message_date_added'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
    ]
