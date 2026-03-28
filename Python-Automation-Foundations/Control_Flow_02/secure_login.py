import time

counter = 0
pssword = input("Enter password: ")
while pssword != "123" :
        print("Wrong password")
        counter += 1
        if counter == 3 :
            print("Too many attempts")
            time.sleep(3)
            exit()
        password = input("Enter password: ")
print("Correct password")

time.sleep(10)