def year_of_birth(name,age):
    year = 2023 -age
    print(f"Hello {name}, you were born in {year}")

def my_country(country="Kenya"):
    print(f"Hello you are from {country}")

def hello(*names):
    for name in names :
       print(f"hello{name}")

def sum (*nums):
    answer = 0
    for num in nums:
        answer += num
        return answer
    
def multiply_many(**kwags):
    answer = 1
    for num in kwags.values():
        answer *= num


    return answer

def concatenate_args(*names):
    answer =""
    for name in names:
        answer += name
    return answer

def concatenate_kwags(**numbers):
    answer =""
    for num in numbers:
        answer += num
    return answer

def sum_multiplication(sum,multiplication):
    return(f"The sum of 2 and 6 is {sum} and their product is{multiplication}")
#posotional arguments
print(sum_multiplication(2+6,2*6))
#kewword arguments
def firstname(*names):
    # for name in names:
    #  print(f"Hello{name}")
# firstname("emmie","diana","loice","steph")
#  final=[name for name in names]
#  print(f"hello {final}")
# firstname("emmie","diana","loice","steph")

#kwags
 def firstname(**kwargs):
    for name in kwargs.values():
        print(name)

firstname(a="loice",b="emmie",c="stephanie")
