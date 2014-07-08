import sys

f=open(sys.argv[1])	#noise_lines
g=open(sys.argv[2])	# support vectors
h=open(sys.argv[3]) # data file
a=[]
i=0
bucket=0
t=0
for line in h:
	t=t+1
for line in f:
	a.append(int(float(line.strip()))-1)
for line in g:
	bucket+=1
	w=int(line.strip().split(',')[0][1:])
	if(w in a):
		i+=1
	if(bucket>=0.05*t):
		print(i)
		i=0
		bucket=0
		
	
		
	


