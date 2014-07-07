import sys

f=open(sys.argv[1])
g=open(sys.argv[2])
a=[]
i=0
bucket=0
for line in f:
	a.append(int(float(line.strip())))
for line in g:
	bucket+=1
	w=int(line.strip().split(',')[0][1:])
	if(w in a):
		i+=1
	if(bucket>=1000):
		print(i)
		i=0
		bucket=0
		
	
		
	


