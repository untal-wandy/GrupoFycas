# Generated by Django 5.0.3 on 2024-03-07 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='dni',
            field=models.IntegerField(default=0),
        ),
    ]
