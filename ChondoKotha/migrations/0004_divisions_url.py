# Generated by Django 3.0.4 on 2020-03-13 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChondoKotha', '0003_auto_20200313_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='divisions',
            name='url',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
