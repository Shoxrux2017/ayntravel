# Generated by Django 4.2 on 2023-04-21 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aynTravelApp', '0013_alter_cat_options_alter_offer_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to='Photos/%Y/%m/%d', verbose_name='фотография турпакета'),
        ),
    ]
