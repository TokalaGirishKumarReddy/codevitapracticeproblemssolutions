

#This code is contributed by T.Girish Kumar Reddy 179X1A05H0
from itertools import permutations

def check(i,n2):
	x=''.join(i)
	y=int(x)
	return y
	print(y)

t=input().split(" ")
n1=list(t[0])
n1.sort()
n2=int(t[1])
mins=0
val=0
perm=permutations(n1)
for i in list(perm):
	res=check(i,n2)
	if res>n2:
		val=res
		mins=1
		break
if mins==0:
	print(-1)
else:
	print(val)
