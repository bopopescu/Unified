# Generated by Django 2.1.3 on 2018-11-14 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tube', '0002_employee_workinghours'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='experience',
            field=models.IntegerField(default=2),
        ),
    ]
