# Generated by Django 5.0.3 on 2024-03-28 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_todoitems_datedue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitems',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
