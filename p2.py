a='''i
10 -5 -2 3
4 -10 3 -3
1 6 10 -3
'''
a=a.splitlines()[1:]
ai=-1


def input():
	global ai
	ai+=1
	return a[ai]

from itertools import *
from pprint import pprint
r2=lambda x,y=4: round(x+1e-15,y)
s1=list(map(int,input().split()))
s2=list(map(int,input().split()))
s3=list(map(int,input().split()))

def d2(s,a):
	return abs(s[a[0]])>abs(s[a[1]]+s[a[2]])
def dd():	
	global s1,s2,s3
	for s1,s2,s3 in (list(permutations((s1,s2,s3)))):
		if all((d2(s1,(0,1,2)),d2(s2,(1,2,0)),d2(s3,(2,0,1)))):return (s1,s2,s3)
	raise Exception('Not Diagonally Dominant')
s1,s2,s3=dd()

a1,b1,c1,d1=s1
a2,b2,c2,d2=s2
a3,b3,c3,d3=s3
x=y=z=0 
x1=y1=z1=0 
for i in count(1):
	x=((d1-b1*y-c1*z)/a1)
	y=((d2-a2*x-c2*z)/b2)
	z=((d3-a3*x-b3*y)/c3)
	if all(r2(i)==r2(j) for i,j in zip((x,y,z),(x1,y1,z1))):break
	x1,y1,z1=x,y,z
	print(i,list(map(r2,(x,y,z))))