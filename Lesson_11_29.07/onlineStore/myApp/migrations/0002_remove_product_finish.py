# Generated by Django 4.2.3 on 2023-07-29 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='finish',
        ),
    ]