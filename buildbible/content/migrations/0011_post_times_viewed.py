# Generated by Django 2.2.7 on 2019-12-06 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0010_auto_20191203_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='times_viewed',
            field=models.IntegerField(default=0),
        ),
    ]
