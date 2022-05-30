"""
参考：https://zhuanlan.zhihu.com/p/430314894
"""
import os

from celery import Celery

# 导入DJANGO_SETTINGS_MODULE环境变量，为Celery命令行程序创造运行环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todolsitdjango.settings')
# 实例化一个app对象，是一个Celery程序实例
app = Celery('todolistdjango')
# 调用config_from_object()方法，从我们项目的设置文件中读取环境设置。namespace属性指定了在我们的settings.py文件中,
# 所有和Celery相关的配置都以CELERY开头，例如CELERY_BROKER_URL
app.config_from_object('django.conf:settings', namespace='CELERY')
# 调用autodiscover_tasks()，让Celery自动发现所有的异步任务。Celery会在每个INSTALLED_APPS中列出的应用中寻找task.py文件，
# 在里边寻找定义好的异步任务然后执行。
app.autodiscover_tasks()
