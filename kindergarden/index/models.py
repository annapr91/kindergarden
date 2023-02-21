from typing import List

from PIL import Image
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from parler.models import TranslatableModel, TranslatedFields


# Create your models here.
class ContactForm(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email



class AdditLes(models.Model):

    choice = models.CharField(max_length=154, unique=True)
    def __str__(self):
        return self.choice

_MAX_SIZE = 300
class Kindergarden(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=20),
        address = models.CharField(max_length=255),
        area = models.CharField(max_length=30),
        photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, max_length=50),
        phone_number = models.CharField(max_length=20),
        num_free_places = models.IntegerField(default=0, null=True),
        num_register_child = models.IntegerField(default=0, null=True),
        addition_lessons = models.ManyToManyField(AdditLes),
        free_places = models.BooleanField(default=True),
    )


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Сначала - обычное сохранение
        super(Kindergarden, self).save(*args, **kwargs)

        # Проверяем, указан ли логотип
        if self.photo:
            filepath = self.photo.path
            width = self.photo.width
            height = self.photo.height
            print(width)
            print(height)

            max_size = max(width, height)
            print(max_size)
            if max_size > _MAX_SIZE or max_size < _MAX_SIZE:
                # Надо, Федя, надо
                image = Image.open(filepath)
                print(filepath)
                # resize - безопасная функция, она создаёт новый объект, а не
                # вносит изменения в исходный, поэтому так
                image = image.resize(
                    (round(width / max_size * _MAX_SIZE),  # Сохраняем пропорции
                     round(height / max_size * _MAX_SIZE)),
                    Image.ANTIALIAS
                )
                print(image)
                # И не забыть сохраниться
                image.save(filepath)
class Child(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    id_number = models.CharField(max_length=20)
    roditeli = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='Родители')
    det_sads = models.ManyToManyField('Kindergarden')
    qeue = models.IntegerField(default=None,null=True)
    regist_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + ' ' + self.surname


    class Meta:
        verbose_name = 'Ребенок'
        verbose_name_plural = 'Дети'


class Children(models.Model):
     name = models.CharField(max_length=20)
     surname = models.CharField(max_length=20)
     id_number = models.CharField(max_length=20)
     roditeli= models.ForeignKey('Perents',on_delete=models.CASCADE, verbose_name='Родители')
     det_sads = models.CharField(max_length=20)
#
     def __str__(self):
         return self.name + ' ' + self.surname
#
     class Meta:
         verbose_name = 'Ребенок'
#
#
class Perents(models.Model):
     id_number = models.CharField(max_length=20)
     name = models.CharField(max_length=20)
     phone_number=models.CharField(max_length=20)

     def chirod(self):
         chil=Children.objects.all()
         chil.roditeli_id=self.pk
         chil.roditeli_id.save()

     def __str__(self):
         return self.name

     class Meta:
         verbose_name = 'Roditel'
#



class User(AbstractUser):
    address = models.CharField(max_length=150)
    phone = models.IntegerField(blank=True,null=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.last_name



    class Meta:
        verbose_name = 'Родитель'
        verbose_name_plural = 'Родители'







# class Kindergard(models.Model):
#      name = models.CharField(max_length=20)
#      address = models.CharField(max_length=50)
#     empty_space = models.CharField(max_length=50)
#     childrens = models.ManyToManyField(Children, through='Membership')
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Detskii sadik'
#
# class Membership(models.Model):
#     childrens=models.ForeignKey(Children,on_delete=models.CASCADE)
#     sad = models.ForeignKey(Kindergard, on_delete=models.CASCADE)
#
#     class Meta:
#         verbose_name = 'Deti-sadi'