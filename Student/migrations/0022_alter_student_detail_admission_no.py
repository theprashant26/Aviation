# Generated by Django 3.2.9 on 2022-09-09 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0021_auto_20220831_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_detail',
            name='Admission_no',
            field=models.CharField(default='EGL/431262', max_length=10),
        ),
    ]
