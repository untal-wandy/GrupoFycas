# Generated by Django 5.0.3 on 2024-03-13 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0015_remove_credit_number_credit_dni_credit_price_feed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='credit',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
