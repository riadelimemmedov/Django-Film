# Generated by Django 4.0 on 2022-04-16 02:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0012_alter_profile_user'),
        ('postblog', '0010_alter_postfilm_slug_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=400)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('liked_comment', models.ManyToManyField(blank=True, related_name='likedcomment', to='profiles.Profile')),
                ('post_film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentsblogfilm', to='postblog.postfilm')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
