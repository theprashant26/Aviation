# Generated by Django 3.2.9 on 2022-03-23 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0016_alter_course_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='Duration',
            field=models.CharField(choices=[('3 mon', '3 MONTH'), ('6 mon', '6 MONTH'), ('1 mon', '1 MONTH')], max_length=100, null=True),
        ),
    ]
