import threading
import time

def boom():
    print('BOOM')

if __name__ == '__main__':
    timer = threading.Timer(5, boom)
    timer.start()
    time.sleep(2)
    timer.cancel()