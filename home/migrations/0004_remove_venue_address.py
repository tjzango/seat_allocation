# Generated by Django 3.2.6 on 2022-01-20 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20220120_1151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venue',
            name='address',
        ),
    ]
