# Generated by Django 3.2.6 on 2022-03-30 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('literature', '0006_alter_place_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='images',
        ),
        migrations.AddField(
            model_name='place',
            name='images',
            field=models.ManyToManyField(to='literature.ImageModel'),
        ),
    ]
