from django.db import models
from django.contrib import admin


class Blog_user(models.Model):
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    age = models.IntegerField('Возраст')
    about_me = models.TextField('Обо мне')
    hobby = models.TextField('Хобби')

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'


admin.site.register(Blog_user)
