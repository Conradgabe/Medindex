# Generated by Django 4.0.2 on 2022-04-17 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicrecord',
            name='blood_group',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='medicrecord',
            name='first_name',
            field=models.CharField(max_length=120),
        ),
    ]