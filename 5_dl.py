import numpy
import numpy as np
f=open("ras.txt","a+")
rows=10
cols=5
a=np.matrix(np.random.randint(10,20,size=(rows, cols))) #generate a reandom matrix
#numpy.savetxt(f,a)
#wines = np.genfromtxt("ras.txt", delimiter=";")
#print wines
#For save the matrix on a text file
b=np.matrix(np.random.randint(40000,50000,size=(rows, cols)))
#numpy.savetxt(f,b)
c=np.matrix(np.random.randint(70,80,size=(rows, cols)))
#numpy.savetxt(f,c)
print "1 st matrix-"
print a
print "2nd matrix-"
print b
print "3rd matrix-"
print c
print "The data matrix is-"
data_matrix=np.concatenate((a,b,c)) #concatenate all the mtrix to generate data matrix

print data_matrix
level=rows * 3
data_level=numpy.ndarray((level,cols)) 
#data_level=np.matrix(np.random.randint(10,20,size=(level, cols)))

print "Shape of data matrix-"
temp=np.shape(data_level)
print temp
temp2=np.size(data_level,0)
print "Size of data level-"
print temp2
#############################################################
a1 = numpy.zeros(shape=(temp2,1))  
#a=np.matrix(np.random.randint(10,20,size=(temp2,1)))
#print a1
#rm=np.matrix(np.random.randint(10,20,size=(temp2,1)))
#print rm

#xrange=5
for i in range(0,temp2):
	if(data_matrix[i,0] < 21 and data_matrix[i,0] > 9):   #if all(cond1,cond2,cond3) if any(cond1,cond2,cond3)
		a1[i,0]=1
        elif(data_matrix[i,0] < 50001 and data_matrix[i,0] > 39999):
		a1[i,0]=2
	elif(data_matrix[i,0] < 81 and data_matrix[i,0] > 69):
		a1[i,0]=3	
print a1 # Printing Data Label Matrix
u=data_matrix.std() # SD of Data matrix
print "The SD is"
print u
m=data_matrix.mean() #mean of data matrix
print "The mean is"
print m
z= numpy.zeros(shape=(temp2,cols)) 
for i in range(0,temp2):
	for j in range(0,cols):
		z[i,j]=(data_matrix[i,j]-m)/u
print z		
#############

