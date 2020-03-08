# This modules defines variables and functions used as examples in this training.
import requests
import time
import threading


WEBSITES = [
    'http://en.kremlin.ru/',
    'http://mfa.go.th/main/',
    'http://www.antarctica.gov.au/',
    'http://www.mofa.gov.la/',
    'http://www.presidency.gov.gh/',
    'https://www.aph.gov.au/',
    'https://www.argentina.gob.ar/',
    'https://www.fmprc.gov.cn/mfa_eng/',
    'https://www.gcis.gov.za/',
    'https://www.gov.ro/en',
    'https://www.government.se/',
    'https://www.india.gov.in/',
    'https://www.jpf.go.jp/e/',
    'https://www.oreilly.com/',
    'https://www.parliament.nz/en/',
    'https://www.peru.gob.pe/',
    'https://www.premier.gov.pl/en.html',
    'https://www.presidence.gov.mg/',
    'https://www.saskatchewan.ca/'
]










def visit_website(url):
    """Makes a request to a url and prints the status code and elapsed time"""
    r = requests.get(url) 
    print(f'{url} returned {r.status_code} after {r.elapsed} seconds')

#def visit_website(url):
#    #"""Makes a request to a url and prints the status code and elapsed time"""
#    #r = requests.get(url) 
#    #print(f'{url} returned {r.status_code} after {r.elapsed} seconds')
#    import time
#    import random
#    time.sleep(random.randint(0,5))
#    print(url)









class Account():
    def __init__(self):
        self.balance = 0

    def __repr__(self):
        return f'Current balance is {self.balance}'

    def deposit(self, amount):
        print(f'Depositing {amount}')
        # Simulates a database read and write
        state = self.balance
        state += amount
        time.sleep(0.1)
        self.balance = state

    def withdrawal(self, amount):
        print(f'Withdrawing {amount}')
        # Simulates a database read and write
        state = self.balance
        state -= amount
        time.sleep(0.1)
        self.balance = state










class ThreadSafeAccount():
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock() # Give each account a Lock

    def __repr__(self):
        return f'Current balance is {self.balance}'

    def deposit(self, amount):
        print(f'Depositing {amount}')

        # Limit access to shared data to only one thread at a time
        with self.lock:
            state = self.balance
            state += amount
            time.sleep(0.1)
            self.balance = state

    def withdrawal(self, amount):
        print(f'Withdrawaling {amount}')

        # Limit access to shared data to only one thread at a time
        with self.lock:
            state = self.balance
            state -= amount
            time.sleep(0.1)
            self.balance = state