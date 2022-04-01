#Sri Tarun Gulumuru
#duration:30 mins
#Question 1
import random

def prob(x):
    a=[0.0,1.0]
    for i in range(x-1):
        a.append(random.random())
    a.sort()
    b=[]
    for i in range(1,x+1):
        b.append(a[i]-a[i-1])

    return [b[i] for i in range(x)]

z= int(input("Give the size of the tables:"))
print("Table 1:",prob(z))
print("Table 2:",prob(z))
