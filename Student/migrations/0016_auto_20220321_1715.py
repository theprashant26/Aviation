# Generated by Django 3.2.9 on 2022-03-21 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0015_auto_20220321_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_detail',
            name='Admission_no',
            field=models.CharField(default='BRD/153576', max_length=10),
        ),
        migrations.AlterField(
            model_name='student_detail',
            name='paid_amount',
            field=models.BigIntegerField(default=0),
        ),
    ]