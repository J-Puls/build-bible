# Generated by Django 2.2.7 on 2019-11-28 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_post_context'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]