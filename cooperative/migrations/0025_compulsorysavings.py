# Generated by Django 3.2.8 on 2022-01-10 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0024_alter_cooperativeshopledger_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompulsorySavings',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('transaction', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cooperative.transactiontypes')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
