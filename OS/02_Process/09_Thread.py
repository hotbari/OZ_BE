import threading
import os

def func():
    print('...Half-assed function...')
    print('My Process ID is', os.getpid())
    print('Thread ID : ', threading.get_native_id())


if __name__ == '__main__':
    print('Process Id : ', os.getpid())
    thread1 = threading.Thread(target=func)
    thread1.start()