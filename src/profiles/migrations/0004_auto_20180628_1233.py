# Generated by Django 2.0 on 2018-06-28 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_profile_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='department',
            field=models.CharField(max_length=120),
        ),
    ]
