# Generated by Django 4.0 on 2022-02-22 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0014_alter_relatedmoviemodel_image_relatedmovie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relatedmoviemodel',
            name='slug_relatedmovie',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
