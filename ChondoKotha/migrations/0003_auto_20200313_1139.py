# Generated by Django 3.0.4 on 2020-03-13 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChondoKotha', '0002_auto_20200313_1136'),
    ]

    operations = [
        migrations.RenameField(
            model_name='district',
            old_name='division',
            new_name='division_id',
        ),
    ]
