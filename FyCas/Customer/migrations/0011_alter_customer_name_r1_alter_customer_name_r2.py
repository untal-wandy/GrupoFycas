# Generated by Django 5.0.3 on 2024-03-11 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0010_customer_name_r1_customer_name_r2_customer_number_r1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='name_r1',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name_r2',
            field=models.CharField(max_length=255),
        ),
    ]