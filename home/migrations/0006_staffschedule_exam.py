# Generated by Django 3.2.6 on 2022-01-22 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20220122_1126'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffschedule',
            name='exam',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.scheduleexamination'),
            preserve_default=False,
        ),
    ]
