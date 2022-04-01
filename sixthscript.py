import random

m1=[]
m2=[]
r1= random.randint(1,10)
c1= random.randint(1,10)
for i in range(r1):
    a=[]
    for j in range(c1):
        a.append(random.randint(0,9))
    m1.append(a)
r2= random.randint(1,10)
c2=random.randint(1,10)
for i in range(r2):
    a=[]
    for j in range(c2):
        a.append(random.randint(0,9))
    m2.append(a)
print("Rows and columns of matrix one respectively are:",r1,c1)
print("Rows and columns of matrix two respectively are:",r2,c2)
if(c1==r2):
    print("As there are",c1,"columns in the first matrix and",r2,"rows in the second matrix. Therefore, we can multiply the two matrices")
else:
    print("We can't multiply the two matrices as there are",c1,"columns in the first matrix and",r2,"rows in the second matrix.")
        
