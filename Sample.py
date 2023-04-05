from math import *

try:
 n=int(input('\nEnter a Number : '))
 r=sqrt(n)
 print()
 print('sqr root of',n,':',r)
 print(f'sqr root of {n} : {r:.2f}')
 print('sqr root of %d : %.2f' %(n,r))
except ValueError:
 print('\ninvalid input..\n')