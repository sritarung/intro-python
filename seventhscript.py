#Sri Tarun Gulumuru
#duration:25 mins
#Question7
class emptySet(Exception):
    def __init__(self,data):
        self.data=data
    def __str__(self):
        return self.data

def cartesionProduct(s1,s2):
    if len(s1)==0 or len(s2)==0:
        raise emptySet("Two sets are required to produce a cartesian product. Please give your input for two sets again")
    else:
        print("The cartesian product is:",[(a,b) for a in s1 for b in s2])

def inputs():
    s1=set(map(int,input("Input values for Set1: ").split()))
    s2=set(map(int,input("Input values for Set2: ").split()))
    return (s1,s2)

a=True

while a:
    try:
        s1,s2=inputs()
        cartesionProduct(s1,s2)
        a=False
    except emptySet as e:
        print(e)
        a=True
