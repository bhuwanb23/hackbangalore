# Generated by Django 4.0.6 on 2024-05-11 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_innovator_date_of_birth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investor',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='project',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='project',
            name='owner',
        ),
    ]
