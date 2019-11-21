from django.db import models


class Category(models.Model):
    """Модель категории"""
    name = models.CharField("Имя", max_length=100)
    slug = models.SlugField("url", max_length=100, unique=True)

    def __str__(self):
        return '{0} '.format(self.name)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Tag(models.Model):
    """Модель тега"""
    name = models.CharField("имя", max_length=100)
    slug = models.SlugField("url", max_length=100, unique=True)

    def __str__(self):
        return '{0} '.format(self.name)

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Post(models.Model):
    """Модель поста"""
    title = models.CharField("заголовок", max_length=250)
    mini_text = models.TextField("описание")
    text = models.TextField("текст")
    create_date = models.DateTimeField("дата создания", auto_now=True)
    slug = models.SlugField("url", max_length=100, unique=True)

    def __str__(self):
        return '{0} {1} {2} {3}' .format(self.title, self.mini_text, self.text, self.create_date)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class Comment(models.Model):
    """Модель поста"""
    text = models.TextField("текст")
    create_date = models.DateTimeField("дата создания", auto_now=True)
    slug = models.SlugField("url", max_length=100, unique=True)
    moderation = models.BooleanField(default=True)

    def __str__(self):
        return '{0} {1}' .format(self.text, self.create_date)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

