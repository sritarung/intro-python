# author: Sri Tarun Gulumuru
# duration: 
# morning session (9:30 am)

#Question 1
minutes_str=input("Enter the minutes to be converted to milliseconds: ") #takes input for minutes
minutes_int=int(minutes_str) # converts minutes in str form to integer
milliseconds=minutes_int*60000 # formula that converts minutes to milliseconds
print("The result is",milliseconds,"milliseconds.") #prints the result

#Question 2
import math #imports the module to use sqrt function 
a=1 #given values
b=2
c=1
discriminant=(b**2)-(4*a*c) 
x1=(-b+math.sqrt(discriminant))/(2*a) #formula for one soln
x2=(-b-math.sqrt(discriminant))/(2*a) #formula for other soln
print("The roots of the quadratic equation are",x1,"and",x2,"!") #prints the solns

#Question 3
final_score=int(input("Enter the final score out of 100: ")) #takes the input for the final score and converts it to int form
midterm_score=int(input("Enter the midterm score out of 100: ")) # does the above for the midterm score
overall_grade=(final_score*0.60)+(midterm_score*0.40) #formula for conversion of final and midterm score to overall grade
print("The overall grade is",overall_grade,"!") # prints the result of overall grade

#Question 4
final_score=int(input("Enter the final score out of 100: ")) #takes the input for the final score and converts it to int form
midterm_score=int(input("Enter the midterm score out of 100: ")) # does the above for the midterm score
overall_grade=(final_score*0.60)+(midterm_score*0.40) #formula for conversion of final and midterm score to overall grade
print("The overall grade is",overall_grade,"!")# prints the result of overall grade

#Question 5
help('modules') # this brings/prints all installed modules to screen
import random # I picked and imported random module, so its attributes are available
dir(random) #lists the functions in the module random
help(random) #gives the detailed description of each attributes/functions from the module

#Question 6
import math #to use sqrt function 
a=6  # defined the sides of the triangle for simplicity of highlighting the formula working
b=3 # input for the sides could be asked to but for simplicity it is defined
c=4
s=(a+b+c)/2
area=math.sqrt((s*(s-a)*(s-b)*(s-c))) #heron formula to find the area of triangle
print("The area of a triangle with sides",a,",",b,",",c,"are",area,"!") #prints the result

#Question 7 
import math #to use the pow function
n=2 # here rather than asking for input of n, I have used my n value. You can ask input for n if required.
radius=n/4 #given definition statement for radius based on n
cube=(math.pow(n,3)) # volume of cube
sphere=(4/3)*math.pi*(math.pow(radius,3)) # volume of sphere
print("The number of marbles of n/4 radius that can fit into n sized cube when n is",n,"equals to",(cube//sphere),"!") 
# above division gives the number of spheres that can be fitted into the cube 

#Question 8
celsius=int(input("Enter the Celsius value to be converted to other measurement units: ")) #takes and converts the input for celsius to int form
fahrenheit=(celsius*1.8)+32 #formula to convert celsius to fahrenheit
kelvin=celsius+273.15 #formula to convert celsius to kelvin
reaumur=celsius*0.8 #formula to convert celsius to reaumur
rankine=(celsius+273.15)*(9/5) #formula to convert to rankine
print("Inputted Celsius is equal to",fahrenheit,"Fahrenheit,",kelvin,"Kelvin,",reaumur,"Reaumur,",rankine,"Rankine.") #prints the converted values of celsius in various forms.




