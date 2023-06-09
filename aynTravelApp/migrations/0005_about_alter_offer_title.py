# Generated by Django 4.2 on 2023-04-20 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aynTravelApp', '0004_offer_location1'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('info', models.TextField(blank=True)),
                ('photo', models.ImageField(blank=True, upload_to='Photos/%Y/%m/%d')),
            ],
            options={
                'verbose_name': 'информация',
                'verbose_name_plural': 'информации',
            },
        ),
        migrations.AlterField(
            model_name='offer',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Nazvanie tur paketa'),
        ),
    ]
