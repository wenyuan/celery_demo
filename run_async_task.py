from tasks.my_tasks import *

# get() 方法用于获取任务的返回值，前面讲过
task1.delay().get()
task2.delay("张三").get()
task3.delay().get()
task4.delay("李四").get()
