# Generated by Django 4.1.1 on 2022-11-30 00:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainerPicker', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupclass',
            name='participants',
        ),
    ]