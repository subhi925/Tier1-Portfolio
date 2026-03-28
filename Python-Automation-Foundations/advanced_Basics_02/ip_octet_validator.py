import time

first_octet = input("Enter a number: ")

try:
    first_octet = int(first_octet)
except ValueError:
    print("Invalid input. Please enter a valid number.")
    time.sleep(10)
    exit()

if first_octet == 127 :
    print("Loopback address")
elif first_octet < 0 or first_octet > 255 :
    print("Invalid IP address")
else :
    print("Regular IP address")

time.sleep(10)