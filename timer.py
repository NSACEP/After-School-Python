from time import time

def timer(func):
    ti = time()
    func()
    tf = time()
    return tf - ti

