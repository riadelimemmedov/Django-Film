# Generated by Django 4.0 on 2022-04-03 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('postblog', '0004_alter_postfilm_image_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postfilm',
            name='category_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categorypost', to='postblog.category'),
        ),
    ]