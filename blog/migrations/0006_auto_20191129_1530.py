# Generated by Django 2.2.7 on 2019-11-29 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20191129_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tag', to='blog.Tag', verbose_name='Тег'),
        ),
        migrations.AlterField(
            model_name='post',
            name='template',
            field=models.CharField(default='blog/post_list.html', max_length=500, verbose_name='шаблон'),
        ),
    ]
