# Generated by Django 4.2.5 on 2024-03-12 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RaceApp', '0015_delete_companypayment'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('trackday_date', models.DateField()),
                ('payment_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_status', models.CharField(default='Pending', max_length=20)),
            ],
        ),
    ]
