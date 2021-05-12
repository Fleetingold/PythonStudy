from queue import Queue
from Task import Task
class Scheduler():
    def __init__(self):
        self.taskQueue = Queue()
        self.maxTaskId = 0
        self.taskMap = dict()

    def schduler(self,task):
        self.taskQueue.put(task)

    def newTask(self,coroutine):
        self.maxTaskId+=1
        task = Task(self.maxTaskId,coroutine)
        self.taskMap[self.maxTaskId] = task
        self.schduler(task)
        return self.maxTaskId

    def KillTask(self,taskid):
        if not taskid in self.taskMap:
            return False
        i = 0
        while i < self.taskQueue.qsize():
            tmp = self.taskQueue.get()
            if temp == self.taskMap[taskid]:
                del self.taskMap[taskid]
                break
            else:
                self.schduler(tmp)
            i+=1
        return True

    def run(self):
        while not self.taskQueue.empty():
            task = self.taskQueue.get()
            retval = task.run()
            if task.isFinished:
                tid = task.getTaskId()
                del self.taskMap[tid]
            else:
                self.schduler(task)