# Generated by Django 3.1.3 on 2021-01-14 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0012_auto_20210114_0403'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlineitem',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]