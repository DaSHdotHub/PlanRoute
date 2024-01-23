# Generated by Django 3.2 on 2024-01-23 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distance',
            name='depart_at',
            field=models.DateTimeField(blank=True, help_text='Departure time', null=True),
        ),
        migrations.AlterField(
            model_name='distance',
            name='distance_in_km',
            field=models.FloatField(blank=True, help_text='Distance in kilometers', null=True),
        ),
        migrations.AlterField(
            model_name='distance',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='distance',
            name='travel_mode',
            field=models.CharField(default='car', help_text='Mode of travel', max_length=10),
        ),
    ]
