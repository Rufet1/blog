# Generated by Django 2.2.6 on 2020-04-19 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0013_homeimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeimage',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]
