# Generated by Django 4.0.6 on 2022-08-31 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='biography',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
