# Generated by Django 3.1.5 on 2021-01-18 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_auto_20210114_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='todo_deadline',
            field=models.DateTimeField(blank=True),
        ),
    ]