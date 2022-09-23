from celery.schedules import crontab
from app import app
from .my_tasks import task1, task2, task3, task4


@app.on_after_configure.connect
def period_task(sender, **kwargs):

    # 第一个参数为 schedule，可以是 float 或者 crontab
    # 第二个参数是任务，第三个参数是名字
    sender.add_periodic_task(10.0, task1.s(),
                             name="每10秒执行一次")
    sender.add_periodic_task(15.0, task2.s("task2"),
                             name="每15秒执行一次")
    sender.add_periodic_task(20.0, task3.s(),
                             name="每20秒执行一次")
    sender.add_periodic_task(
        crontab(hour=18, minute=5, day_of_week=0),
        task4.s("task4"),
        name="每个星期天的18:05运行一次"
    )
