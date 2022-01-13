# Generated by Django 3.2.8 on 2022-01-13 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summoner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameRecord',
            fields=[
                ('summoner_name', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Summoner',
            fields=[
                ('summoner_name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('summoner_level', models.IntegerField()),
                ('summoner_rank', models.IntegerField()),
                ('summoner_icon', models.IntegerField()),
            ],
        ),
    ]
