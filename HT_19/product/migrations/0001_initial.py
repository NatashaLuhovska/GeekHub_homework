# Generated by Django 4.1.5 on 2023-01-15 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(default='', max_length=20)),
                ('title', models.CharField(default='Default title', max_length=200)),
                ('old_price', models.DecimalField(blank=True, decimal_places=2, default='0.00', max_digits=10)),
                ('current_price', models.DecimalField(decimal_places=2, default='0.00', max_digits=10)),
                ('href_product', models.CharField(blank=True, default='', max_length=256)),
                ('brand', models.CharField(default='', max_length=120)),
                ('category', models.CharField(default='', max_length=40)),
                ('description', models.TextField(blank=True, default='')),
            ],
        ),
    ]