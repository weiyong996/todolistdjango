import datetime
from django.db import models
import django.utils.timezone as timezone


NOT_DELETE = datetime.datetime(1900, 1, 1, 0, 0, 0)
NOT_COMPLETED = datetime.datetime(1900, 1, 1, 0, 0, 0)


class Item(models.Model):
    """Item 待办事项"""
    id = models.AutoField('id', primary_key=True)
    content = models.CharField('待办事项', default='', max_length=255, null=True, help_text='待办事项的内容')
    detail = models.TextField('详细内容', default='', null=True, blank=True, help_text='待办事项的详细内容')
    completed = models.BooleanField('是否完成', default=False, null=True, help_text='是否已完成')
    completed_time = models.DateTimeField('完成待办事项的时间', default=NOT_COMPLETED, help_text='完成待办事项的时间')
    deadline = models.DateField('截止时间', default=datetime.date.today, null=True, help_text='完成待办事项的截止时间')
    create_time = models.DateTimeField('创建时间', default=timezone.now, help_text='创建时间')
    update_time = models.DateTimeField('最后一次更新时间', auto_now=True, help_text='最后一次更新时间')
    delete_time = models.DateTimeField('删除时间', default=NOT_DELETE, help_text='删除待办事项的时间')
    tags = models.ManyToManyField('Tag', blank=True)

    class Meta:
        verbose_name = '待办事项'
        verbose_name_plural = '待办事项'


class Tag(models.Model):
    """Tag 标签"""
    id = models.AutoField('id', primary_key=True)
    name = models.CharField("tag name", default='', max_length=255, null=True, help_text='标签名称')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'
