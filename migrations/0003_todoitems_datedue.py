# Generated by Django 5.0.3 on 2024-03-28 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_todoitems_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitems',
            name='datedue',
            field=models.DateField(blank=True, null=True, verbose_name='Due Date'),
        ),
    ]
