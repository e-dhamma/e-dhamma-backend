# Generated by Django 2.0.1 on 2018-01-26 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('term', '0004_auto_20180123_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eng',
            name='term',
        ),
        migrations.RemoveField(
            model_name='est',
            name='term',
        ),
        migrations.RemoveField(
            model_name='pali',
            name='term',
        ),
        migrations.RemoveField(
            model_name='translatorschat',
            name='term',
        ),
        migrations.AddField(
            model_name='meaning',
            name='eng',
            field=models.CharField(default='English', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='meaning',
            name='est',
            field=models.CharField(default='Eesti keeles', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='term',
            name='pali',
            field=models.CharField(default='in Pali', max_length=250),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Eng',
        ),
        migrations.DeleteModel(
            name='Est',
        ),
        migrations.DeleteModel(
            name='Pali',
        ),
        migrations.DeleteModel(
            name='TranslatorsChat',
        ),
    ]