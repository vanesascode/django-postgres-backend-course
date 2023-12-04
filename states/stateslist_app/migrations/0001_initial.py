# Generated by Django 4.2.8 on 2023-12-04 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('image', models.CharField(max_length=900)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
