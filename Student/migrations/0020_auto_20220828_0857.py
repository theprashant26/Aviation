# Generated by Django 3.2.9 on 2022-08-28 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0019_auto_20220828_0855'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student_detail',
            old_name='doc_10',
            new_name='doc_10th',
        ),
        migrations.RenameField(
            model_name='student_detail',
            old_name='doc_12',
            new_name='doc_12th',
        ),
        migrations.AlterField(
            model_name='student_detail',
            name='Admission_no',
            field=models.CharField(default='EGL/827913', max_length=10),
        ),
    ]
