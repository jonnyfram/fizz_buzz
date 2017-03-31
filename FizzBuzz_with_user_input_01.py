import sys

#used_arg = False

def GetInput(n):
    if sys.argv[1:]:
       n = sys.argv[1]
       return n
    else:
        #GetUserInput(n)
        n = input("Enter a number to fizzbuzz: ")
        return n

"""def GetUserInput(n):
    try:
        print("You must supply a number to fizzbuzz with")
        user_input = input("Enter a number to count Fizzbuzz")
        n = user_input

    except NameError:
        print("You must supply a number, text will not fizz buzz")
        GetUserInput(n)
    
    except ValueError:
        print("You must supply a number, text will not fizz buzz")
        GetUserInput(n)
        
    except TypeError:
        print("You must supply a number, text will not fizz buzz")
        GetUserInput(n)"""

def fizzbuzz(counter):
    while counter <= n:
        if counter % 3 ==0 and counter % 15 ==0:
            print("Fizzbuzz")
            counter+=1
            
        elif counter % 3==0:
           print("Fizz")
           counter+=1
        
        elif counter % 5==0:
            print("Buzz")
            counter+=1
        
        else:
            print(counter)
            counter+=1
n= 0
user_number=int(GetInput(n))
n = user_number
#print(type(n))#for debugging

counting_text = "Fizz buzz counting up to " + str(n)
print(counting_text)

fizzbuzz(counter=1)