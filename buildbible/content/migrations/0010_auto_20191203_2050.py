# Generated by Django 2.2.7 on 2019-12-03 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0009_auto_20191129_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.IntegerField(blank=True, choices=[(1, 'Specs'), (2, 'Mechanical'), (3, 'Interior'), (4, 'Exterior'), (5, 'Miscellaneous')], null=True),
        ),
    ]
