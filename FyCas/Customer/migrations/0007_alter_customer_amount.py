# Generated by Django 5.0.3 on 2024-03-09 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0006_alter_customer_dni'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='amount',
            field=models.IntegerField(null=True),
        ),
    ]
