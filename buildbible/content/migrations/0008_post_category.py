# Generated by Django 2.2.7 on 2019-11-29 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0007_auto_20191129_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[(1, 'specs'), (2, 'mechanical'), (3, 'interior'), (4, 'exterior'), (5, 'miscellaneous')], default=1, max_length=50),
            preserve_default=False,
        ),
    ]