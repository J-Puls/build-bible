# Generated by Django 2.2.7 on 2019-11-27 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='context',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='vehicles.Vehicle'),
        ),
    ]