# Generated by Django 2.0.1 on 2018-02-01 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('term', '0007_auto_20180201_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]