import sys

f = open(sys.argv[1])
g = open(sys.argv[2],'w')
h=open("noise_lines",'w')
q=float(sys.argv[3])
c=0
n=0
i=0
for line in f:
	i=i+1
	word = line.strip().split('\t')
	if len(word) < 5:
		word.append(' ')
	if 'Grocery' in word[0]:
		c += 1
		if c==5:
			c=0
			word[0] = "carriers"
			h.write(str(i)+'\n')
	else:
		n += 1
		if n==q:
			n=0
			word[0] = "Grocery"
			h.write(str(i)+'\n')
	line1 = word[0]+'\t'+word[1]+'\t'+word[2]+'\t'+word[3]+'\t'+word[4]+'\n'
	g.write(line1)		
f.close()
g.close()	
