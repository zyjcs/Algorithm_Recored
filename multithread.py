import threading
import time
def test():
    for i  in range(5):
        print(threading.currentThread().name+'test',i)
        time.sleep(0.5)
thread = threading.Thread(target=test,name="TestThread")
thread.start()
# thread.join()

for i in range(5):
    print(threading.current_thread().name+"main",i)
    print(thread.name+'alive',thread.is_alive())
    time.sleep(1)

