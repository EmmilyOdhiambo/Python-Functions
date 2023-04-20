def even_numbers():
    x = range(0,20)
    for i in x:
        if i % 2 !=0:
           print(i) 


def odd_numbers():
    x = range(0,20)
    for i in x:
        if i % 2 !=0:
           print(i) 

def divisible_by_five():
    x = range(50)
    for i in x:
        if i % 5 == 0:
            print(f"{i}is divisible by 5")
        else:
            print (f"{i} is not divisible by 5")

def multiple_comparison():
    x = range(50)
    for i in x:
        if i % 5 == 0:
            print(f"{i}is divisible by 5 ")
        elif i% 7 ==0:
             print(f"{i}is divisible by 7 ")
        elif i % 9 ==0:
             print(f"{i}is divisible by 9 ")
        else:
             print(f"{i}is divisible by 5 ,7,9")
        

def odd_or_even():
    x = range(20)
    for i in x:
        if i % 2 == 0 and i % 3 == 0:
            print(f"{i}is divisible by both 2 and 3 ")
        elif i% 2 ==0 or i % 3 ==0:
             print(f"{i}is divisible by either 2 or 3 ")
    
        else:
             print(f"{i}is not divisible by 2 or 3")

def while_loop():
    x = 1
    while x < 10:
        print("hello")
        x +=1
def break_statement():
    x = 1
    while x < 10:
        print("hello")
        x +=1
        if x == 5:
            break
             

def continue_statement():
    x = 0
    while x <= 20:
        x += 1
        if x % 3 ==0:
            continue
        print(x)

#Write a function that uses while, if and continue statements to print all
#the even numbers between 0 and 50. 
def even_nums():
    k = 0
    while k <= 50:
        k +=1
        if k % 2 != 0:
            continue
        print(k)
 #Write a function that takes an integer argument and prints "Prime" 
 # if the number is prime, and "Not prime" if the number is not prime
def prime_nums():
    num2=10
    num1=20
    for num in range(num2,num1+1):
       if num==1:
          print(num,"is not a prime number" )
       elif num>1:
        for i in range(2,num):
            if (num % i) ==0:
                print(num,"is not prime number")
                break
        else:
            print(num,"is prime number")
    else:
        print(num,"is nota prime number")
#Write a function that takes a list of integers as input and prints 
# the sum of all the even numbers in the list.
def sum(*numbers):
    sum = 0
    for i in numbers:
        if i % 2 ==0:
            sum +=i
    print (sum)
#Write a function that takes any two integers as input, and prints the sum of
#all the numbers between the two integers (inclusive) that are divisible by 3.
def numbers(*nums):
    num1 = 20
    sum = 0 
    for x in range(num1+1):
      if x % 3 == 0:
          sum = x + sum
    print(sum)


