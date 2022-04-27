# Generated by Django 4.0.4 on 2022-04-26 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0005_post_writer'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='liked_users',
            field=models.ManyToManyField(related_name='user_likes', to='landing.tempuser'),
        ),
    ]
