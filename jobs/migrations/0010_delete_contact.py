# Generated by Django 3.2.7 on 2021-09-09 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0009_remove_contact_image_bg_contact'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
