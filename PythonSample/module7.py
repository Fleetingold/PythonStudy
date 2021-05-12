from Scheduler import Scheduler

def task1():
    i = 0
    while i < 10:
        print('This is task 1 i is %s' %i)
        i+=1
        yield i

def task2():
    i = 0
    while i < 10:
        print('This is task 2 i is %s' %i)
        i+=1
        yield i

sch = Scheduler()
sch.newTask(task1())
sch.newTask(task2())
sch.run()