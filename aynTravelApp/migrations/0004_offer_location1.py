# Generated by Django 4.2 on 2023-04-19 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aynTravelApp', '0003_remove_offer_location1'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='location1',
            field=models.CharField(max_length=100, null=True, verbose_name='Lokatsiya'),
        ),
    ]
