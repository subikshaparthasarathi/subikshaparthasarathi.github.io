# Generated by Django 4.0.2 on 2022-03-01 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signupApp', '0009_alter_customer_fname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='lname',
            field=models.CharField(default='lname', max_length=50),
        ),
    ]
