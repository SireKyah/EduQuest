# Generated by Django 5.0.1 on 2024-02-05 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_quest_badge_image_url_delete_badge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quest',
            name='badge_image_url',
            field=models.URLField(),
        ),
    ]