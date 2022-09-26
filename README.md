# Celery 使用案例

## 环境

> 本项目需要在 Linux 服务器上运行。

* Python 3.8.9
* Celery 5.2.7
* Redis 7

## 前置准备

* 本项目配套文档参考 [使用 celery 实现异步任务和定时任务](https://www.fedbook.cn/backend-knowledge/python/python-lib-celery/)
* 安装 Redis 参考 [Redis 的安装与卸载](https://www.fedbook.cn/basic-skills/redis/installation-of-redis/)
* 安装 Python 及虚拟环境参考 [Python 多版本虚拟环境共存](https://www.fedbook.cn/backend-knowledge/python/multiple-python-install-on-linux/)

## 项目结构

```
celery_demo/
├── tasks
│   │── my_tasks.py     # 异步任务
│   └── period_task.py  # 定时任务
├── app.py              # celery 实例
├── config.py           # celery 配置
├── run_async_task.py   # 手动调用异步任务
└── ...
```

## 运行代码

安装好依赖包后，进入 `celery_demo/` 目录下：

首先运行 celery work：

```bash
celery -A app worker -l info
```

### 手动调用异步任务

执行以下命令：

```bash
python run_async_task.py
```

然后观察 celery work 的输出。

### 定时执行异步任务

首先运行 celery beat：

```bash
celery -A app worker -l info
```

然后观察 celery work 的输出，定时任务将依次执行：

* 任务 task1 每 10 秒执行一次
* 任务 task2 每 15 秒执行一次
* 任务 task3 每 20 秒执行一次
* 而任务 task4 每个星期天的 18:05 执行一次
