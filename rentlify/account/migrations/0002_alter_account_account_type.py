# Generated by Django 5.0.6 on 2024-05-29 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_type',
            field=models.CharField(choices=[('seller', 'Seller'), ('buyer', 'Buyer'), ('admin', 'Admin'), ('staff', 'Staff'), ('basic', 'Basic')], default='basic', max_length=10),
        ),
    ]
