# Generated by Django 3.2.8 on 2022-01-14 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0049_auto_20220114_0105'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase_header',
            name='certification_status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cooperative.certificationstatus'),
        ),
    ]