# Generated by Django 3.2.6 on 2021-08-17 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('literature', '0002_auto_20210817_1159'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Про нас',
                'verbose_name_plural': 'Про нас',
            },
        ),
    ]
