# Generated by Django 3.0 on 2020-02-04 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tba_app', '0004_registration_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=100)),
            ],
        ),
    ]
