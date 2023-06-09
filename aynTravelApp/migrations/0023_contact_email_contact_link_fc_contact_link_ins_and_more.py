# Generated by Django 4.2 on 2023-04-23 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aynTravelApp', '0022_alter_operator_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.URLField(null=True, verbose_name='Почта администратора'),
        ),
        migrations.AddField(
            model_name='contact',
            name='link_fc',
            field=models.URLField(blank=True, verbose_name='ссылка на facebook'),
        ),
        migrations.AddField(
            model_name='contact',
            name='link_ins',
            field=models.URLField(blank=True, verbose_name='ссылка на instagram'),
        ),
        migrations.AddField(
            model_name='contact',
            name='link_tg',
            field=models.URLField(blank=True, verbose_name='ссылка на telegram'),
        ),
    ]
