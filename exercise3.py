import random
n = random.randint(0,100)
guess_time = 5
while True:
    a = int(input("please type a number:"))
    if a > n:
        print("decrease your number")
    elif a < n:
        print("increase your number")
    elif a == n:
        print("Wow , nice shot :).")
        break


