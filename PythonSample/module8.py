import time
import threading
def Ordering(interval):
    cnt = 0
    while cnt<100:
        print('好了,你订餐成功，订餐号码是：%d号 订餐时间是：%s 请在旁边耐心等\n\n' %(cnt,time.ctime()))
        time.sleep(interval)
        cnt+1
    threading.current_thread()._stop()

def Notice(interval):
    cnt = 0
    while cnt<100:
        print('谁的号码是%d,您的餐好了,过来取一下\n'%cnt)
        cnt+=1
    threading.current_thread()._stop()

def work(): #Use thread.start_new_thread() to create 2 new threads
    threading._start_new_thread(Ordering,(1,))
    threading._start_new_thread(Notice,(5,))

if __name__=='__main__':
    work()