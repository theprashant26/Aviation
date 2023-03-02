# Generated by Django 4.1.4 on 2023-03-01 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0030_alter_course_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='Duration',
            field=models.CharField(choices=[('1 mon', '1 MONTH'), ('3 mon', '3 MONTH'), ('6 mon', '6 MONTH')], max_length=100, null=True),
        ),
    ]
