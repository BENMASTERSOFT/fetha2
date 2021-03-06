# Generated by Django 3.2.8 on 2021-12-15 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0016_auto_20211215_0608'),
    ]

    operations = [
        migrations.AddField(
            model_name='memberscashwithdrawalsapplication',
            name='certification_comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='memberscashwithdrawalsapplication',
            name='certification_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='memberscashwithdrawalsapplication',
            name='certification_officer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cooperative.certificationofficers'),
        ),
    ]
