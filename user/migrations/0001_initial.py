# Generated by Django 2.0.2 on 2018-03-07 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('product_name', models.CharField(max_length=1000)),
                ('seller_name', models.CharField(max_length=100)),
                ('seller_phone', models.CharField(max_length=20)),
                ('seller_email', models.CharField(max_length=50)),
                ('seller_block', models.CharField(max_length=20)),
                ('seller_room', models.CharField(max_length=20)),
                ('time_period', models.CharField(max_length=10)),
                ('product_price', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('password', models.CharField(blank=True, max_length=250, null=True)),
                ('email_id', models.CharField(max_length=50, unique=True)),
                ('phone_number', models.IntegerField(blank=True, null=True, unique=True)),
            ],
        ),
    ]