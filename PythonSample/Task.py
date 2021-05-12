class Task():
    def __init__(self, taskid, coroutine):
        self.__taskId = taskid
        self.__coroutine = coroutine
        self.__sendValue = ''
        self.__beforeFirstYield = True
        self.isFinished = False

    def getTaskId(self):
        return self.__taskId

    def setValue(self,value):
        self.__sendValue == value

    def run(self):
        if(self.__beforeFirstYield):
            self.__beforeFirstYield = False
            return next(self.__coroutine)
            
        else:
            try:
                retval = self.__coroutine.send(self.__sendValue)
                return retval
            except StopIteration:
                self.isFinished = True
                return ""