# Generated by Django 3.2.9 on 2022-11-30 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_certificateinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='q_form',
            name='subject',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
