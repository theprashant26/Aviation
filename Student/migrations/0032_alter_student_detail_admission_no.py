# Generated by Django 4.1.4 on 2023-01-17 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0031_alter_student_detail_admission_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_detail',
            name='Admission_no',
            field=models.CharField(default='BRD/251557', max_length=10),
        ),
    ]
