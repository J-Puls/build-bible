# Generated by Django 2.2.7 on 2019-11-28 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_post_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subtitle',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
