# Generated by Django 2.2.7 on 2019-12-03 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20191129_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='template',
            field=models.CharField(default='blog/post_list.html', max_length=500, verbose_name='шаблон'),
        ),
    ]
