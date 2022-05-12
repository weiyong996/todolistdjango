import datetime
from django.db import models
import django.utils.timezone as timezone


class Item(models.Model):
    """Item 事项

    content: item's content. 事项内容
    completed: return true if item is completed, or false. 是否已完成，若完成则返回true，否则返回false
    deadline: item's deadline date, default today. 截止时间
    create_date: create item date(include time) 创建时间
    update_date: update item date(include time) 更新时间
    tags: item's tags
    """
    id = models.AutoField('id', primary_key=True)
    content = models.CharField('content', default='', max_length=255, null=True, help_text='事项')
    completed = models.BooleanField('is completed', default=False, null=True, help_text='是否已完成')
    deadline = models.DateField('deadline', default=datetime.date.today, null=True, help_text='截止时间')
    create_date = models.DateTimeField('create date', default=timezone.now, help_text='创建时间')
    update_date = models.DateTimeField('update date', auto_now=True, help_text='最后更新时间')
    tags = models.ManyToManyField('Tag')

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'


class Tag(models.Model):
    """Tag 标签

    name: tag's name 标签名称
    """
    id = models.AutoField('id', primary_key=True)
    name = models.CharField("tag name", default='', max_length=255, null=True, help_text='标签名称')

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
