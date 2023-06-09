# Generated by Django 4.2 on 2023-04-20 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aynTravelApp', '0008_category_alter_offer_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='categor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='offer', to='aynTravelApp.category'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='aynTravelApp.cat'),
        ),
    ]
