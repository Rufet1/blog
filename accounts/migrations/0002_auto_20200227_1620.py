# Generated by Django 2.2.6 on 2020-02-27 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='born',
            name='date',
            field=models.DateField(default='2020-02-20'),
        ),
    ]
