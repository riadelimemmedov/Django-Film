# Generated by Django 4.0 on 2022-02-22 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0012_relatedmoviemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='relatedmoviemodel',
            name='idvalue_relatedmovie',
            field=models.CharField(default=0, max_length=100, unique=True),
        ),
    ]