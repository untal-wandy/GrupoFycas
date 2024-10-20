# Generated by Django 5.0 on 2024-10-20 13:10

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0059_credit_estado'),
    ]

    operations = [
        migrations.CreateModel(
            name='CashControl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('opening_balance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('closing_balance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_income', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_expenses', models.DecimalField(decimal_places=2, max_digits=10)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='cuota',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cuota',
            name='start_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
