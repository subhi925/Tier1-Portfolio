import time
import random

randomNumber = random.randint(0, 9)
while randomNumber < 9 :
    print(randomNumber)
    randomNumber = random.randint(0, 9)
print("finish")
time.sleep(10)