# Generated by Django 5.0 on 2024-10-30 12:30

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0061_credit_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuota',
            name='last_pay',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
