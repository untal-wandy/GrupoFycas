# Generated by Django 5.0.3 on 2024-03-11 12:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0008_alter_customer_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=10000)),
                ('name', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
                ('no_account', models.IntegerField()),
                ('mode_pay', models.BooleanField(default=False)),
                ('day_pay', models.IntegerField(default=30)),
                ('day_pay2', models.IntegerField(default=15)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Customer.customer')),
            ],
        ),
    ]
