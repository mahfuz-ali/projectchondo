# Generated by Django 3.0.4 on 2020-03-13 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChondoKotha', '0005_auto_20200313_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='lat',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='district',
            name='lon',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='district',
            name='url',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='divisions',
            name='url',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
