# Generated by Django 3.2.9 on 2022-03-15 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0008_auto_20220315_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_detail',
            name='Admission_no',
            field=models.CharField(default='29090R', max_length=10),
        ),
    ]
