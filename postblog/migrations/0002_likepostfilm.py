# Generated by Django 4.0 on 2022-04-02 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0012_alter_profile_user'),
        ('postblog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikePostFilm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_liked', models.CharField(choices=[('Like', 'Like'), ('Unlike', 'Unlike')], default='Like', max_length=50)),
                ('updated_time_like', models.DateTimeField(auto_now=True)),
                ('created_time_like', models.DateTimeField(auto_now_add=True)),
                ('post_liked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postblog.postfilm')),
                ('profile_liked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
            ],
        ),
    ]
