#i)
age=int(input("Enter Your Age"))

if age >=18:
    print("Your Eligible")
else:
    print("You are not eligible")
    
    
#ii)
mark=int(input("enter mark"))
def grade_students():
    if mark >=90 and mark <=100:
        print("A")  
    elif mark>=80 and mark <=89:
        print("B")
    elif mark>=70 and mark <=79:
        print("C")  
    elif mark>60 and mark <=69: 
        print("D")     
    else:
        print("F")    
grade_students()     
mark=85


#iv)
mark=int(input("enter mark"))
def grade_students():
    if mark is float:
        print("invalid input")  

        
#v)
mark=int(input("enter mark")) 
def grade_students():
    if mark >=90 and mark <=100:
        print("'Excellent' 'A'")  
    elif mark>=80 and mark <=89:
        print("'Excellent' 'B'")
    elif mark>=70 and mark <=79:
        print("'Good''C'")  
    elif mark>60 and mark <=69: 
        print("'Satisfactory' 'D'")     
    else:
        print("'Needs Improvement' 'F'")    
grade_students()     