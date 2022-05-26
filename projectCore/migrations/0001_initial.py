# Generated by Django 4.0.4 on 2022-05-26 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_razao_social', models.CharField(max_length=100)),
                ('customer_cnpj', models.CharField(max_length=18)),
                ('customer_fantasy_name', models.CharField(max_length=100)),
                ('customer_contact_name', models.CharField(blank=True, max_length=50)),
                ('customer_contact_email', models.EmailField(blank=True, max_length=300)),
            ],
        ),
    ]
