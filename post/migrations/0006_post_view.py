# Generated by Django 2.2.6 on 2020-02-27 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_delete_postlike'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='view',
            field=models.IntegerField(default=0),
        ),
    ]
