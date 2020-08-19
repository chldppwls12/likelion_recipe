# Generated by Django 3.0.7 on 2020-08-18 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_customer_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_nm', models.CharField(max_length=1000)),
                ('calorie', models.CharField(max_length=1000)),
                ('nation_nm', models.CharField(max_length=1000)),
                ('cooking_time', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_nm_ko', models.CharField(max_length=1000)),
                ('cooking_dc', models.CharField(max_length=100000)),
                ('irdnt_nm', models.CharField(max_length=10000)),
                ('stre_step_image_url', models.CharField(max_length=100000)),
            ],
        ),
    ]