# Generated by Django 3.2.9 on 2022-03-21 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_q_form'),
    ]

    operations = [
        migrations.CreateModel(
            name='email_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, null=True)),
            ],
        ),
    ]
