# Generated by Django 2.2.7 on 2019-11-27 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0003_auto_20191127_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='prod_end',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='prod_start',
            field=models.IntegerField(),
        ),
    ]
