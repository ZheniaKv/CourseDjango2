from django.db import models

# Create your models here.

class Page(models.Model):
    """Модель страницы"""

    title = models.CharField("заголовок", max_length=250)
    text = models.TextField("текст")
    active = models.BooleanField("вкл/выкл", default=True)
    template =  models.CharField("шаблон", max_length=250, default='page/index.html')
    slug = models.SlugField("url", max_length=100, unique=True)

    def __str__(self):
        return '{0}' .format(self.title)

    class Meta:
        verbose_name = "Cтраница"
        verbose_name_plural = "Страницы"
