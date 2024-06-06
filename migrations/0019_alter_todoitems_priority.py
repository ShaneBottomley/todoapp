# Generated by Django 5.0.3 on 2024-04-05 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0018_alter_todoitems_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitems',
            name='priority',
            field=models.CharField(choices=[('Low', 'Low Priority'), ('High', 'High Priority')], default='No', null=True, verbose_name='Priority'),
        ),
    ]
