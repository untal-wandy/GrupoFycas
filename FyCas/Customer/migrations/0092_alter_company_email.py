# Generated by Django 5.0 on 2024-11-17 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0091_alter_company_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='email',
            field=models.CharField(blank=True, max_length=233, null=True),
        ),
    ]
