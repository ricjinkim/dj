# Generated by Django 4.2.6 on 2023-10-31 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('sal', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
