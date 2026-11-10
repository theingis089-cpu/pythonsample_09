num = int(input("Enter a number: "))
if(num % 2 ==0):
    print(num, "is an even number")
else:
    print(num, "is an odd number")
if num <= 1:
    print(num, "is not a prime number")
else:
    for i in range (2 , num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")


