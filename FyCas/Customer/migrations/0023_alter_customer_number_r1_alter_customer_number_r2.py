# Generated by Django 5.0.3 on 2024-03-29 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0022_alter_customer_lat_alter_customer_lon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='number_r1',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='customer',
            name='number_r2',
            field=models.CharField(default='', max_length=30),
        ),
    ]
