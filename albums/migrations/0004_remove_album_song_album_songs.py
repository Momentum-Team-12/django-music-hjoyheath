# Generated by Django 4.0.4 on 2022-05-06 00:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0003_album_song'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='song',
        ),
        migrations.AddField(
            model_name='album',
            name='songs',
            field=models.TextField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
    ]
