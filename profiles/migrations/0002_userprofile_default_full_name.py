# Generated by Django 3.1.3 on 2020-12-15 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='default_full_name',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
    ]
