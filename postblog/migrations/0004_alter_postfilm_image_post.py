# Generated by Django 4.0 on 2022-04-03 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postblog', '0003_imagepost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postfilm',
            name='image_post',
            field=models.ImageField(blank=True, upload_to='postimages'),
        ),
    ]
