# Generated by Django 4.2 on 2023-04-23 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aynTravelApp', '0026_alter_operator_author_alter_operator_author_en_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='offer',
            old_name='is_published',
            new_name='available',
        ),
        migrations.AddField(
            model_name='cat',
            name='available',
            field=models.BooleanField(default=True, verbose_name='Доступность'),
        ),
    ]
