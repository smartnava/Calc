a='''i
27 6 -1 85
6 15 2 72
1 1 54 110
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
s1=list(map(float,input().split()))
s2=list(map(float,input().split()))
s3=list(map(float,input().split()))
def dd(a):	
	s1,s2,s3=a
	for s1,s2,s3 in (list(permutations((s1,s2,s3)))):
		if all((s1[0]>(s1[1]+s1[2]),s2[1]>(s2[0]+s2[2]),s3[2]>(s3[0]+s3[1]))):return (s1,s2,s3)
	raise Exception('Not Diagonally Dominant')
def f2s(a):
	res=[]
	for x in a:
		for y in x:
			result = '{:.15f}'.format(y).rstrip('0').rstrip('.')
			res+= ['0' if result == '-0' else result]
	# print(res)
	return res

def main(a,b=1):
	try:
		z=dd(a)
	except Exception as e:
		return str(e)
	s1,s2,s3=z
	a1,b1,c1,d1=s1
	a2,b2,c2,d2=s2
	a3,b3,c3,d3=s3
	res=''

	
	
	
	# res="<div class='row'><div class='col s12'><div class='card-panel blue lighten-3'>$$[A,B] \sim \\begin{{vmatrix}} {} & {} & {} & {} \\\\{} & {} & {} & {} \\\\{} & {} & {} & {}\end{{vmatrix}}$$".format(*(f2s(z)))
	res2="<table><tr><th>Iteration</th><th>x value</th><th>y value</th><th>z value</th></tr>"
	x=y=z=0
	for i in count(1):
		d=((d1-b1*y-c1*z)/a1)
		e=((d2-a2*x-c2*z)/b2)
		f=((d3-a3*x-b3*y)/c3)
		if all(r2(i)==r2(j) for i,j in zip((x,y,z),(d,e,f))):break
		x,y,z=d,e,f
		res+='I{:<2} -> {:.4f} {:.4f} {:.4f}\n'.format(i,*(list(map(r2,(x,y,z)))))
		res2+='<tr><td>{:02} </td><td> {:.4f} </td><td> {:.4f} </td><td> {:.4f} </td></tr>'.format(i,*(list(map(r2,(x,y,z)))))
	res2+='</table></div></div></div>'
	return (res,res2)[b]

if __name__ == '__main__':
	print(main((s1,s2,s3),0))