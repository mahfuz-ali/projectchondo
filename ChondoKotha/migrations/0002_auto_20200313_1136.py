# Generated by Django 3.0.4 on 2020-03-13 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChondoKotha', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='district',
            name='lat',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='district',
            name='lon',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='district',
            name='url',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
