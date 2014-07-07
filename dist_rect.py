import sys
f=open(sys.argv[1])     #dataset
g=str(sys.argv[2])      #positive class name
h=float(sys.argv[3])    #distribution fraction
q=open('shoppinglist.tsv','w') #final dataset
i=0.0
j=0.0
k=223284.0
l=0.0
b=0
for line in f:
	w=line.strip().split('\t')
	if g in w[0]:
		i=i+1
f.close()
f=open(sys.argv[1])
if(i/k <= h):
	for line in f:
		w=line.strip().split('\t')
		if g not in w[0]:
			l=l+1
			if(i/(k-l) >= h):
				q.write(line)
		else:
			q.write(line)
else:
	for line in f:
		w=line.strip().split('\t')
		if g in w[0]:
			l=l+1
			if((i-l)/k >= h):
				k=k-1
			else:
				q.write(line)
		else:
			q.write(line)
q.close()        
f.close()    


