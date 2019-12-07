
from django.db import models
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey
# Create your models here.
from requests import options


class Menu(models.Model):
    """Модель меню"""
    name = models.CharField("имя",max_length=250)
    is_auth = models.BooleanField("для зарегистрированных?",default=True)
    active = models.BooleanField("вкл/выкл", default=True)

    def __str__(self):
        return '{0} '.format(self.name)

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"



class MenuItem(MPTTModel):
    """Модель пунктов меню"""
    name = models.CharField("name", max_length=250)
    title = models.CharField("заголовок", max_length=250)
    parent = TreeForeignKey(
        'self',
        verbose_name="родительская категория",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    menu = models.ForeignKey(
        Menu,
        verbose_name="меню",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    status =  models.BooleanField("вкл/выкл", default=True)
    is_auth = models.BooleanField("для зарегистрированных?", default=True)
    anchor = models.CharField("якорь",max_length=250)
    url = models.URLField("ссылка на внешний ресур",max_length=250)
    active = models.BooleanField("вкл/выкл", default=True)

    def __str__(self):
        return '{0} '.format(self.name)

    class Meta:
        verbose_name = "Пункты меню"
        verbose_name_plural = "Пункты меню"
