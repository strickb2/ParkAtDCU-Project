# Generated by Django 3.1.1 on 2020-11-08 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parkatdcu', '0003_auto_20201108_2214'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carpark',
            fields=[
                ('carpark_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('spaces', models.IntegerField()),
                ('disabled_spaces', models.IntegerField()),
                ('campus_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parkatdcu.campus')),
            ],
        ),
        migrations.DeleteModel(
            name='Car',
        ),
    ]
