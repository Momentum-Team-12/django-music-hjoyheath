# Generated by Django 4.0.4 on 2022-05-05 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='image',
        ),
    ]
