# Generated by Django 3.0 on 2019-12-06 21:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20191206_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='transaction_datetime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
