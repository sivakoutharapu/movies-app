# Generated by Django 5.0 on 2023-12-15 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviesApp', '0011_alter_moviedata_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviedata',
            name='release_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]