# Generated by Django 2.2.7 on 2019-12-06 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0011_post_times_viewed'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicemanual',
            name='times_downloaded',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='post',
            name='subtitle',
            field=models.CharField(blank=True, default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=60),
        ),
    ]
