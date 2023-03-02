# Generated by Django 3.2.9 on 2022-08-31 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0020_auto_20220828_0857'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student_detail',
            old_name='doc_undergraduate',
            new_name='doc_Graduate',
        ),
        migrations.AlterField(
            model_name='student_detail',
            name='Admission_no',
            field=models.CharField(default='EGL/910403', max_length=10),
        ),
        migrations.AlterField(
            model_name='student_detail',
            name='City',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student_detail',
            name='District',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student_detail',
            name='Email',
            field=models.EmailField(max_length=35, null=True),
        ),
    ]