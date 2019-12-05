# Generated by Django 2.2.7 on 2019-11-27 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.TextField()),
                ('model_name', models.TextField()),
                ('chassis_code', models.TextField()),
                ('prod_start', models.IntegerField()),
                ('prod_end', models.IntegerField()),
                ('image', models.ImageField(default='default_vehicle.png', upload_to='vehicle_pics')),
            ],
        ),
    ]
