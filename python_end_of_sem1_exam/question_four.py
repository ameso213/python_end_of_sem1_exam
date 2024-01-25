#i)
def pattern():
    x="abde"
    numbers = ""
    for i in range(len(x)):
        numbers += str(i+1)
        
        print(x[i] +"," + numbers)
pattern()    



#ii)
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
n = 5
factorial_of_n = factorial(n)
print(f"The factorial of n is {factorial_of_n}")
    




#iii)
a=input("Enter a:")
b=input("Enter b:")
total=(a+b)
def sum(a,b):
    total=0
    for x in a,b:
        total+=x
    print(f"The sum of {a} and {b} is {total}")
sum(3,4)    



#iv)
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        print("Brand: " + self.brand)
        print("Year: " + str(self.year))
        
        

#v)
my_car = Car("Wish", 2021)
my_car.display_info()



