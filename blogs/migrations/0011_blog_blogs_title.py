# Generated by Django 3.2.7 on 2021-09-04 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0010_team_bg_image_temas'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blogs_title',
            field=models.CharField(blank=True, default='', max_length=300),
        ),
    ]
