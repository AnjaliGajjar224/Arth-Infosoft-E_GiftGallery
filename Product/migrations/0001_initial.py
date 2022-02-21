# Generated by Django 4.0.2 on 2022-02-16 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('product_price', models.IntegerField()),
                ('product_description', models.TextField()),
                ('product_qty', models.IntegerField()),
            ],
        ),
    ]
