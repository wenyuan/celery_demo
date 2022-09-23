from celery import Celery
import config

# 通过 include 指定存放任务的 py 文件，这里在前面的基础上新增了定时任务
app = Celery(__name__, include=["tasks.my_tasks", "tasks.period_task"])

# 其它参数通过加载配置文件的方式指定
app.config_from_object(config)
