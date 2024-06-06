# Generated by Django 5.0.3 on 2024-04-04 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0017_alter_todoitems_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitems',
            name='priority',
            field=models.CharField(choices=[('0', 'Low Priority'), ('1', 'High Priority')], default='No', null=True, verbose_name='Priority'),
        ),
    ]