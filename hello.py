def hello(name):
    print(f"Hello {name}")
  
def welcome(student, school):
        print(f"welcome to{school},{student}")




def my_details(fname):
    print(fname + " Stephanie")
my_details("Emmily")
my_details("Student name ")


def  my_detail(*identity):
     print("I have only one " + identity[2])
my_detail("fname", "lname","email")

def my_scores(math,chem,geog):
     print("My highest score is "+geog)
my_scores(math="eighty",chem="fifty",geog="ninety") 


def my_person (name,age):
     print("I am ${name}" + {age})
my_person("Emmily Stephanie", 20)

