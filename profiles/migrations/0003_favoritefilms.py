# Generated by Django 4.0 on 2022-03-12 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0017_remove_relatedmoviemodel_slug_relatedmovie'),
        ('profiles', '0002_alter_profile_avatar_alter_profile_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteFilms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('films', models.ManyToManyField(blank=True, related_name='films_list', to='movie.Movie')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
            ],
        ),
    ]