# Generated by Django 4.1.4 on 2023-03-01 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0036_alter_student_detail_admission_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_detail',
            name='Admission_no',
            field=models.CharField(default='BRD/273938', max_length=10),
        ),
    ]