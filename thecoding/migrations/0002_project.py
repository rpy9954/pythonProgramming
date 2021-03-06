# Generated by Django 2.2.6 on 2020-01-21 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thecoding', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('ProId', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('projectName', models.CharField(max_length=100)),
                ('projectType', models.TextField()),
                ('NoOfTower', models.PositiveIntegerField()),
                ('SiteArea', models.FloatField()),
                ('Floors', models.PositiveIntegerField()),
                ('SaleRate', models.FloatField()),
                ('RentalRate', models.FloatField()),
                ('Status', models.BooleanField()),
                ('CompletionYear', models.PositiveIntegerField()),
                ('Powerbackup', models.PositiveIntegerField()),
            ],
        ),
    ]
