# Generated by Django 5.0 on 2023-12-15 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviesApp', '0005_alter_movie_data_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie_data',
            name='release_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
