# Generated by Django 4.1.4 on 2023-01-17 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0007_alter_blog_blog_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_date',
            field=models.DateTimeField(),
        ),
    ]
