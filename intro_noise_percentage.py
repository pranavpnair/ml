import sys

f = open(sys.argv[1])   #dataset
g = open(sys.argv[2],'w')   #dataset with noise
h=open("noise_lines",'w')   # noise line numbers
noise_per=float(sys.argv[3])    # noise percentage to be introduced
s=str(sys.argv[4]) # positive class name
c=0.0
n=0.0
noise=0.0
w=0.0
i=0.0
total=0.0
for line in f:
	total=total+1
f.close()
f = open(sys.argv[1])
for line in f:
	i=i+1
	word = line.strip().split('\t')
	if len(word) < 5:
		word.append(' ')
	if s in word[0]:
		c += 1
		if c==10:
			c=0
			if(noise/total < noise_per):
				noise=noise+1
				word[0] = "cariers"
				h.write(str(i)+'\n')
				line1 = word[0]+'\t'+word[1]+'\t'+word[2]+'\t'+word[3]+'\t'+word[4]+'\n'
				g.write(line1)
		else:
			g.write(line)
f.close()
f = open(sys.argv[1])   #dataset
i=0
for line in f:
	i=i+1
	word = line.strip().split('\t')
	if len(word) < 5:
		word.append(' ')
	if s not in word[0]:
		if(noise/total < noise_per):
			noise=noise+1
			word[0] = s
			h.write(str(i)+'\n')
			line1 = word[0]+'\t'+word[1]+'\t'+word[2]+'\t'+word[3]+'\t'+word[4]+'\n'
			g.write(line1)	
		else:
			g.write(line)
f.close()
g.close()	
