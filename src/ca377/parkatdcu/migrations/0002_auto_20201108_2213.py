# Generated by Django 3.1.1 on 2020-11-08 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parkatdcu', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carpark',
            old_name='carpark_id',
            new_name='id',
        ),
    ]
