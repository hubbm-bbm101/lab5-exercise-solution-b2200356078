N = int(input("Write a number:"))
sumEven = 0
sumOdd = 0
for i in range(1, N + 1):
    if i % 2 == 0:
        sumEven += i

    else:
        sumOdd += i
print("The sum of the odd numbers is,", sumOdd)
print("the avegage of the even numbers is,", sumEven / N)
