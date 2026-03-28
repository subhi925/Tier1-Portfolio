import time

while True:
    # input pass
    #if the pass is 123 exite while loop
    #else print "Wrong password"
    pssword = input("Enter password: ")
    if pssword == "123" :
        print("Correct password")
        break
    else :
        print("Wrong password")
time.sleep(10)