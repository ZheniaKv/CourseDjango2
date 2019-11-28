from django.urls import reverse
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):
    """Модель категории"""
    name = models.CharField("имя", max_length=100)
    slug = models.SlugField("url", max_length=100, unique=True)
    description = models.TextField("описание", max_length=1000, default="", blank=True)
    parent = TreeForeignKey(
        'self',
        verbose_name="Родительская категория",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    template = models.CharField("шаблон", max_length=500, default="blog/single_post.html")
    published = models.BooleanField("отображать?", default=True)
    paginated = models.PositiveIntegerField("количество новостей на странице", default=5)
    sort = models.PositiveIntegerField('порядок', default=0)


    def __str__(self):
        return '{0} '.format(self.name)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Tag(models.Model):
    """Модель тега"""
    name = models.CharField("имя", max_length=100)
    slug = models.SlugField("url", max_length=100, unique=True)
    published = models.BooleanField("отображать?", default=True)

    def __str__(self):
        return '{0} '.format(self.name)

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Post(models.Model):
    """Модель поста"""
    author = models.ForeignKey(
        User,
        verbose_name="Автор",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    title = models.CharField("заголовок", max_length=250)
    subtitle = models.CharField("под заголовок", max_length=500, blank=True, null=True)
    mini_text = models.TextField("описание")
    text = models.TextField("текст")
    create_date = models.DateTimeField("дата создания", auto_now=True)
    slug = models.SlugField("url", max_length=100, unique=True)
    tag = models.ManyToManyField(Tag, verbose_name="Тег", blank=True)

    edit_date = models.DateTimeField(
        "дата редактирования",
        default=timezone.now,
        blank=True,
        null=True
    )
    published_date = models.DateTimeField(
        "дата публикации",
        default=timezone.now,
        blank=True,
        null=True
    )
    image = models.ImageField("главная фотография", upload_to="post/", null=True, blank=True)
    category = models.ForeignKey(Category, verbose_name="Категория",
                                 on_delete=models.CASCADE, null=True)
    template = models.CharField("шаблон", max_length=500, default="blog/post_detail.html")
    published = models.BooleanField("опубликовать?", default=True)
    viewed = models.PositiveIntegerField("просмотрено", default=0)
    status = models.BooleanField("для зарегистрированных", default=False)
    sort = models.PositiveIntegerField('порядок', default=0)


    def __str__(self):
        return '{0} {1} {2} {3}' .format(self.title, self.mini_text, self.text, self.create_date)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def get_absolute_url(self):
        return reverse('detail_post', kwargs={'category': self.category.slug, 'slug': self.slug})




class Comment(models.Model):
    """Модель поста"""
    author = models.ForeignKey(
        User,
        verbose_name="Автор",
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(Post, verbose_name="статья", on_delete=models.CASCADE)
    text = models.TextField("комментарий")
    create_date = models.DateTimeField("дата создания", auto_now=True)
    moderation = models.BooleanField(default=True)

    def __str__(self):
        return '{0} {1}' .format(self.text, self.create_date)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

