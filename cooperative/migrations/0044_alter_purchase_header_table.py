# Generated by Django 3.2.8 on 2022-01-13 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0043_suppliers_prefix'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='purchase_header',
            table='purchaseheader',
        ),
    ]
