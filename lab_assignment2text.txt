# author: Sri Tarun Gulumuru
# duration: 7 hours or more
# morning session (9:30 am)

#Question 1
def perfect_number(n):
    sum = 0
    for a in range(1, n):
        if n % a == 0:
            sum += a
    return sum == n

while(1==1):
    try:
        x=int(input("Enter a number to check: "))
        if(x<=0):
            raise Exception()
        print(perfect_number(x))
        ch=int(input("Press 0 to Quit or any other positive integer to continue : "))
        if(ch==0):
            break
        if(ch<0):
            raise Exception()
    except:
        print("Enter positive integer")

#Question 2
def prime(start,end):
    for i in range(start,end+1):
        if i>1:
            for j in range(2,i):
                if (i%j ==0):
                    break
            else:
                print(i)
start=int(input("Enter a positive start integer:"))
end=int(input("Enter a positive end integer:"))
prime(start,end)
f=open("primes.txt","w")
for i in range(start,end+1):
        if i>1:
            for j in range(2,i):
                if (i%j ==0):
                    break
            else:
                print(i,file=f)
f.close()

#Question 3
import math

while(True):
   try:
       print('Enter the 3 points that form the triangle')
       print('Point 1')
       x1 = int(input('Enter x: '))
       y1 = int(input('Enter y: '))
       print('Point 2')
       x2 = int(input('Enter x: '))
       y2 = int(input('Enter y: '))
       print('Point 3')
       x3 = int(input('Enter x: '))
       y3 = int(input('Enter y: '))

       a = math.sqrt((x2-x1)**2+ (y2-y1)**2)
       b = math.sqrt((x3-x2)**2+ (y3-y2)**2)
       c = math.sqrt((x3-x1)**2 + (y3-y1)**2)

       if a+b > c and b+c > a and c+a > b:
           print('({',x1,'},{',y1,'}), ({',x2,'},{',y2,'}) and ({',x3,'},{',y3,'}) form a triangle',sep="")
       else:
           print('({',x1,'},{',y1,'}), ({',x2,'},{',y2,'}) and ({',x3,'},{',y3,'}) Do Not form a triangle',sep="")
      
       ch=int(input("Press 0 to Quit or any other integer to continue : "))
       if(ch==0):
          break
   except ValueError:
       print('Invalid input!')

#Question 4
def eraser(f_name):
	f= open(f_name,'r')
	lines= f.readlines()
	f.close()
	g=[]
	for line in lines:
		if not line.isspace():
			g.append(line)
	f1=open("quotes2.txt",'w')
	f1.write("".join(g))
	f1.close()
eraser("quotes.txt")

#Question 5
def prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2,n):  
            if n % i == 0:
                return False
        return True

def line(file):

    f = open(file, 'r+')      
    text = f.read()         

    textList = text.split('\n') 
    newList = [i for i in textList if i != '']

    if prime(len(textList)):
        listToStr = '\n'.join([str(line) for line in newList])
        print('\nThe number of lines in the files is a prime number.')
        print('Will remove all newlines in the file.')
    else:
        listToStr = '\t'.join([str(line) for line in newList])
        print('\nThe number of lines in the files is not a prime number.')
        print('Will replace newlines with tabs.')

    f.seek(0)                 
    f.truncate()                
    f.write(listToStr)          
    f.close()
line("lab_assignment.txt")

#Question 6
def trimmer():
	try:
		a=input('Give the string to be trimmed:')
		k=int(input('Give the number of characters that should be left:'))
		if k>len(a):
			raise Exception()
		for i in range(0,len(a)):
			if (k==(len(a)-i+1)):
				break
			else:
				print(a[:len(a)-i])
	except:
		print("The length of the string cannot be greater than the number of characters left")
trimmer()
