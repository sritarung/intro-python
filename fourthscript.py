#Sri Tarun Gulumuru
#duration:40 mins
#Question 4
class matrix:
    def __init__(self,n):
        self.n=n
        self.matrix=[]
        A=[[1,2,3],[4,5,6],[7,8,9]]

        if(self.n%4==0):
            self.printMatrix(A)
            
        elif(self.n<0):
            for i in range(4-(self.n%4)):
                A=self.rotate(A)
            self.printMatrix(A)
            
        elif(self.n % 4 > 0 ):
            for i in range(self.n % 4):
                A=self.rotate(A)
            self.printMatrix(A)

  
    def printMatrix(self,mat):
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                print(mat[i][j],end=' ')
            print()
 
    def rotate(self,mat):
        if(self.n<0):
            newlist=[]
            for i in range(len(mat)-1,-1,-1):
                li=[]
                for j in range(len(mat[i])-1,-1,-1):
                    li.append(mat[j][i])
                newlist.append(li)
            for i in newlist:
                i.reverse()
            return newlist
        else:
            newlist=[]
            for i in range(len(mat[0])):
                li=[]
                for j in range(len(mat)):
                    li.append(mat[j][i])
                li.reverse()
                newlist.append(li)
            return newlist

A=[[1,2,3],[4,5,6],[7,8,9]]
print("Original Matrix:")        
for i in range(len(A)):
      for j in range(len(A[i])):
          print(A[i][j],end=' ')
      print()
      
b=int(input("Input a positive number n to rotate the matrix clockwise n times\
and a negative number n to rotate the matrix anticlockwise n times"))


print("Rotated Matrix")
a=matrix(b)


  
