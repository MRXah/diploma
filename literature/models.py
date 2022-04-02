from django.db import models

# Create your models here.


class ImageModel(models.Model):
    img = models.ImageField(verbose_name='Зображення')

    def __str__(self) -> str:
        return self.img

    class Meta:
        verbose_name_plural = 'Зображення'
        verbose_name = 'Зображення'


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
    images = models.ManyToManyField(ImageModel)
    about = models.TextField(verbose_name='Про місце')

    class Meta:
        verbose_name_plural = 'Місця'
        verbose_name = 'Місце'

    def __str__(self) -> str:
        return self.name
