# author: Sri Tarun Gulumuru
# duration: 12 hours
# morning session (9:30 am)
#Question1
def binary(file1,file2):
    a=[]
    b=[]
    with open(file1,"r") as fa:
        data1=fa.read().splitlines()
    fa.close()
    with open(file2,"r") as fl:
        data2=fl.read().splitlines()
    fl.close()
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
                print("match/similarity :", similar[a][b])
binary('A.txt', 'B.txt')

#Question2
import random
def add(filename):
    f=open(filename,'r')
    lines=f.readlines()

    for i in range(len(lines)):
        lines[i]=lines[i].strip()

        n=random.randint(0,1)

        if(n==0):
            lines[i]=lines[i]+'x'
        else:
            lines[i]=lines[i]+'y'

    f.close()

    f=open(filename,'w')
    for l in lines:
        f.write(l+'\n')

def counter(filename):
    f=open(filename,'r')
    lines=f.readlines()
    counter=0

    for i in range(len(lines)):
        if(lines[i].strip().endswith('xx') or lines[i].strip().endswith('yy')):
           counter=counter+1
    print("The number of the lines finishing with XX and YY is:",counter)
    print("The ratio of the lines finishing with ‘XX’ and ‘YY’ / all n-lines is ",counter/len(lines))
add('abc.txt')         
counter('abc.txt')

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
class user:
    def __init__(self,ids,passs,stat):
    self.userid=ids
    self.password=passs
    self.loginstatus=stat
  
  def verifyLogin():
      pass

class customer(user):
    def __init__(self,name,adr,email,info,shpinfo):
        self.customername= name
        self.address=adr
        self.email=email
        self.creditcardinfo=info
        self.shoppinginfo=shpinfo
        
        self.shoppingcart=shoppingcart()
        self.orders=orders()
    def register():
        pass
    def login():
        pass
    def updateProfile():
        pass

  
class orders:
  def __init__(self,ordid=None,dcreated=None,dshipped=None,cname=None,cid=None,status=None,shippingid=None):
    self.orderid=ordid
    self.datecreated=dcreated
    self.dateshipped =dshipped
    self.customername=cname
    self.customerid=cid
    self.status=status
    self.shippingid=shippingid

    
    self.shippinginfo=shippinginfo()
    self.orderdetails=orderdetails()

  def placeorder():
    pass 

class orderdetails:
  def __init__(self,oid=None,pid=None,pname=None,quantity=None,unit=None,sub=None):
    self.orderid=oid
    self.productid=pid
    self.productname=pname
    self.quantity=quantity
    self.unitcost=unit
    self.subtotal=sub

  def calcprice:
    pass 

class shippinginfo:
  def __init__(self,sid=None,sty=None,scost=None,srid=None):
    self.shippingid=sid
    self.shippingtype=sty
    self.shippingcost=scost
    self.shippingregionid=srid

  def updateshippinginfo():
    pass

class shoppingcart:
  def __init__(self,cid=None,pid=None,quantity=None,date=None):
    self.cartid=cid
    self.productid=pid
    self.quantity=quantity
    self.dateadded=date

  def addcartitem():
    pass

  def updatequantity():
    pass

  def viewcartdetails():
    pass

  def checkout():
    pass

class administrator(user):
  def __init__(self,admin,emai):
    self.adminname=admin
    self.email=emai

  def updatecatalog():
    pass   



#Question5
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

#Question6
import random

x=int(input("Enter number of rows"))
y=int(input("Enter number of columns"))
a=int(input("Enter number of 2D lists"))

e=[]

for i in range(a):
    e.append([])
    for j in range(y):
        e[i].append([])
        for k in range(x):
           e[i][j].append(random.randint(0,1000))

print("3D",a,"x",y,"x",x,"random number list")
print(e)

def twod(el,z):
    for i in range(z):
        print(el[i])

print("The 2D list projection")
twod(e,a)















    

    
