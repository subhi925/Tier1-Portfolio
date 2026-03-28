import time

def double(num):
    """this function doubles the value of number"""
    return num * 2

res = double(5)
print(res)
print(double.__doc__)
time.sleep(10)  