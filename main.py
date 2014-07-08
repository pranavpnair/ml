import subprocess
import sys
i=float(sys.argv[1])    #noise percentage
j=str(sys.argv[2])      #positive class name
subprocess.call('python intro_noise_percentage.py shoppinglist.tsv shoppingListWithNoise.tsv ' + str(i) + ' '+ j,shell=True)
subprocess.call('python models_predict.py shoppingListWithNoise.tsv '+ j+ ' >support_vectors',shell=True)
subprocess.call('python density.py noise_lines support_vectors shoppingListWithNoise.tsv > density',shell=True)
f=open("density")
k=float(f.readline().strip())
g=open("noise_lines")
p=0
for line in g:
	p+=1
print(k/p)
