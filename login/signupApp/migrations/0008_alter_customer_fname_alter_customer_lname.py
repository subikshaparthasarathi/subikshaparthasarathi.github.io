# Generated by Django 4.0.2 on 2022-03-01 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signupApp', '0007_alter_customer_fname_alter_customer_lname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='fname',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='lname',
            field=models.CharField(default='', max_length=50),
        ),
    ]
