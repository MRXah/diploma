# Generated by Django 3.2.6 on 2022-05-14 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('literature', '0008_auto_20220513_1634'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinklModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.TextField(verbose_name='посилання')),
            ],
            options={
                'verbose_name': 'Посилання',
                'verbose_name_plural': 'Посилання',
            },
        ),
        migrations.AddField(
            model_name='place',
            name='address',
            field=models.TextField(blank=True, verbose_name='Адреса'),
        ),
        migrations.AlterField(
            model_name='place',
            name='images',
            field=models.ManyToManyField(to='literature.ImageModel', verbose_name='Зображення'),
        ),
        migrations.AddField(
            model_name='place',
            name='links',
            field=models.ManyToManyField(blank=True, to='literature.LinklModel', verbose_name='Посилання'),
        ),
    ]
