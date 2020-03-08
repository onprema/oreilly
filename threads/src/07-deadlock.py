# Example of a deadlock situation
import threading


if __name__ == '__main__':

    # Create a lock
    lock = threading.Lock()

    # Acquire a lock 
    lock.acquire()

    # Acquire a lock again -- deadlock!
    lock.acquire()

    # Release the lock
    lock.release()
