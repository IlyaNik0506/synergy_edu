from django.db import models


class Desk(models.Model):
     # title = models.CharField('название', max_length=50)
     text = models.TextField('текст')
     number = models.IntegerField('стоимость(цифры)')

     def __str__(self):
          return self.text

     class Meta:
          verbose_name = 'доска объявлений'
          verbose_name_plural = 'доски объявлений'
