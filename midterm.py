# author: Sri Tarun Gulumuru
# duration: 12 hours
# morning session (9:30 am)
#Question1
def binary(file1,file2):
    a=[]
    b=[]
    with open(file1,"r") as f:
        data1=f.read().splitlines()
    f.close()
    with open(file2,"r") as f:
        data2=f.read().splitlines()
    f.close()
    similar=[]
    count=[]
    for i in data1:
        len1=len(str(i))
        c=[]
        d=[]
        for j in data2:
            len2=len(str(j))
            match=""
            counter=0
            if(len1<len2):
                le=len1
            else:
                le=len2
            for z in range(le):
                if str(i)[z]==str(j)[z]:
                    match+=str(j)[z]
                    counter=counter+1
            c.append(match)
            d.append(counter)
        similar.append(c)
        count.append(d)	
    for a in range(len(data1)):
        for b in range(len(data2)):
            if(count[a][b] == 0):
                print("\nThere is no similarity between A.txt and B.txt in line",a+1,"and",b+1,"respectively")
            else:
                print("\nThere are some similarities in line", a+1, "in A text file and line", b+1, "in B text file")
                print("The total count of matches/similarity :", count[a][b])
                print("match/similarity :", similar[a][b])
binary('A.txt', 'B.txt')

#Question2
def change(file1,n):
    with open(file1,"r") as f:
        data=f.readlines()
    second=data[1].split()
    last=data[-1].split()
    a=[]
    a=second[:n]
    second[:n]=last[-n:]
    last[-n:]=a[:n]
    data[1]=' '.join(second)+'\n'
    data[-1]=" ".join(last)
    f.close()
    with open(file1,'w') as f:
        f.writelines(data)
change("Julius.txt",4)

#Question3
i=[1,2.09,3,4,5,6,'a',8,9,10.14,11,'b']
j={1,2,7}
def twod(i):
    d=0
    two=[]
    a=[]
    for j in range(int(len(i)/2)):
        for k in range(2):
            a.append(i[d])
            d=d+1
        two.append(a)
        a=[]
    return two

print(twod(i))

def projection(x,y):
    project=[]
    for i in y:
        if i<=len(x)-1:
            project.append(x[i-1])
        else:
            print("The index",i,"is out of range")
    return project

print(projection(twod(i),j))

#Question4
def printf(x,y):
    print(x)
    for i in range(3):
        for j in range(4):
            print(y[i][j],end="\t")
        print()
    
def two(filename):
    twod=[]
    d=0
    a=[]
    with open(filename,"r")as f:
        data= f.read().splitlines()
    for i in range(3):
        for j in range(4):
            a.append(int(data[d]))
            d=d+1
        twod.append(a)
        a=[]
    f.close()

    printf("Original",twod)
    
    import random
    random.shuffle(twod[0])
    random.shuffle(twod[1])
    random.shuffle(twod[2])
    random.shuffle(twod)
    
    printf("Shuffled",twod)
    with open(filename,"w") as f:
        for i in range(3):
            for j in range(4):
                f.write('%s\n'%twod[i][j])
    f.close()



two("input.txt")

#Question5
def design():
    print('**\n*\n****\n***\n******\n*****\n********\n*******\n**********')

design()

#Question6
def designs():
    print('*\n**\n***\n***\n****\n*****\n****\n*****\n******\n*******\n*****\n******\n*******\n********\n*********')

designs()

#Question7
def caesar_shift(filename,N):
    if N>26 or N<-26:
        N=N%26
    encrypt=[]
    with open(filename,"r") as f:
        data=f.read().splitlines()
    for line in data:
        for char in line:
            if char.isalpha():
                value=ord(char)
                value=value+N
                if char.isupper() and value<65:
                    diff=65-value-1
                    newChar=chr(90-diff)
                elif char.isupper() and value>90:
                    diff=value-90-1
                    newChar=chr(65+diff)
                elif char.islower() and value<97:
                    diff=97-value-1
                    newChar=chr(122-diff)
                elif char.islower() and value>122:
                    diff=value-122-1
                    newChar=chr(97+diff)
                else:
                    newChar=chr(value)
                encrypt.append(newChar)
            else:
                encrypt.append(char)
        encrypt.append("\n")
    output= open("CeaserOut.txt", "w")
    for line in encrypt:
        output.write(line)
    output.close()
    
caesar_shift("Ceaser1.txt",-28)

#Question8
def compare(X,Y):	
	temp= set()	
	a=0
	b=0
	while a < len(X):
		if X[b] == X[b-a]:		
			temp.add(X[a: b+1])		
			b += 1
			if b == len(X):
				a += 1
				b = a
		else:						
			a += 1
			b = a

	match = set() 
	for i in temp:  
		if i in Y:  
			match.add(i)  
	sort = sorted(match)	
	reverse = sorted(match, reverse = True)	
	return sort, reverse	

X = input("Enter string X : ")	
Y = input("Enter string Y : ")	
A, B = compare(X,Y)	
print("Matching sorted set.")
print(A)	
print("Matching reversely sorted set.")
print(B)


