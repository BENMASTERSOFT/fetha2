# Generated by Django 3.2.8 on 2021-12-14 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0011_alter_memberscashdeposits_member'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memberscashdeposits',
            name='account_number',
        ),
        migrations.RemoveField(
            model_name='memberscashdeposits',
            name='transaction',
        ),
        migrations.AddField(
            model_name='memberscashdeposits',
            name='receipt',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
