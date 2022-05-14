from email.policy import default
from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=30, verbose_name='Назва')
    contact = models.CharField(
        max_length=64, unique=True, verbose_name='Контакт')

    class Meta:
        verbose_name_plural = 'Контакти'
        verbose_name = 'Контакт'
        ordering = ['name']


class Place(models.Model):
    name = models.CharField(max_length=255, verbose_name='Назва')
    image = models.ImageField(upload_to='uploads/',
                              verbose_name='Зображення', default=None)
    about = models.TextField(verbose_name='Про місце')
    address = models.TextField(verbose_name='Адреса', blank=True)
    links = models.TextField(verbose_name='Посилання', blank=True)
    x = models.FloatField(verbose_name='Координата Х', default=0)
    y = models.FloatField(verbose_name='Координата У', default=0)

    class Meta:
        verbose_name_plural = 'Місця'
        verbose_name = 'Місце'

    def __str__(self) -> str:
        return self.name
