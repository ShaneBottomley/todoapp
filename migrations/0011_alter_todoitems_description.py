# Generated by Django 5.0.3 on 2024-04-04 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0010_alter_todoitems_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitems',
            name='description',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
    ]