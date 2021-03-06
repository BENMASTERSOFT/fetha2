# Generated by Django 3.2.8 on 2022-01-13 06:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0038_remove_suppliers_reps_supplier'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchases_Temp',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.IntegerField(default=0)),
                ('cost_price', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('total_cost', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('selling_price', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('invoice', models.CharField(max_length=255)),
                ('invoice_date', models.DateField()),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cooperative.suppliers_branches')),
                ('processed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cooperative.stock')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Purchases',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.IntegerField(default=0)),
                ('cost_price', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('total_cost', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('selling_price', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('invoice', models.CharField(max_length=255)),
                ('invoice_date', models.DateField()),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cooperative.suppliers_branches')),
                ('processed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cooperative.stock')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cooperative.transactionstatus')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
