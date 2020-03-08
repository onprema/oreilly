# Example of a locking using Lock objects
import threading


if __name__ == '__main__':

    # Create a lock
    lock = threading.Lock()
    print(lock)

    # Acquire a lock for a section of code
    lock.acquire()
    print(lock)

    # Release the lock
    lock.release()
    print(lock)
