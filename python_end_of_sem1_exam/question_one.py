#i)

def calculate_area(radius):
    area = 3.14* radius**2
    return area

radius=5
area=calculate_area(radius)
print(f"The area of the circle is {area}")



#ii)

def sum(n): 
    if n == 1:
        return 1
    else:
        return n + sum(n-1)


n = 4
sum_of_natural_numbers = sum(n)
print(f"Sum of natural numbers up to n is , {sum_of_natural_numbers}")

#iii)
numbers=[1,3,5,7,9]
numbers.remove(5)
print(numbers)

numbers.append(10)
print(numbers)

#iv)

original_list=[1,2,3,4,5,6,7,8,9,10]
even_numbers=[x for x in original_list if x % 2==0]
print(even_numbers)
        
#v)

student_info={
    "name":"Alice",
    "age" :20,
    "grade" : "A",   
}
student_info["age"]="25"



#vi)
original_dict={'a': 3, 'b': 8, 'c': 2, 'd': 7}
new_dict={}

for key, value in original_dict.items():
    if value> 5:
        new_dict[key]=value
print(new_dict)        



