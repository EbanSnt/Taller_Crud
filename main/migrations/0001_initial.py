# Generated by Django 5.0.1 on 2024-02-12 00:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('telephone_number', models.BigIntegerField()),
                ('telephone_number2', models.BigIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CallHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('description', models.CharField(max_length=300)),
                ('customer_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.customers')),
            ],
        ),
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('ticket_number', models.BigIntegerField()),
                ('product', models.CharField(max_length=30)),
                ('trademark', models.CharField(max_length=30)),
                ('version', models.CharField(max_length=30)),
                ('serial_number', models.CharField(max_length=40)),
                ('failure', models.CharField(max_length=40)),
                ('product_image1', models.ImageField(upload_to='products_images/')),
                ('product_image2', models.ImageField(upload_to='products_images/')),
                ('product_image3', models.ImageField(upload_to='products_images/')),
                ('description', models.CharField(max_length=300)),
                ('local', models.BooleanField(default=True)),
                ('customer_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.customers')),
            ],
        ),
        migrations.CreateModel(
            name='DeliveredProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('invoice', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('ticket_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.tickets')),
            ],
        ),
        migrations.CreateModel(
            name='WarrantyProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('description', models.CharField(max_length=300)),
                ('local', models.BooleanField(default=True)),
                ('ticket_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.tickets')),
            ],
        ),
    ]
