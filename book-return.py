from time import *
from math import *

fmt='%d/%m/%Y'
print()
print('Date of Issue     : '+strftime(fmt,localtime()))
di=time()
dr=di+15*24*60*60
print('Date of Return    : '+strftime(fmt,localtime(dr)))
try:
 ar=input('Enter Return Date : ')
 ar=strptime(ar,fmt)
except ValueError as e:
 print('\nInput alert - '+str(e))
 exit(1)

if mktime(ar)<di:
 print('Invalid Date ')
else:
 d=ceil((mktime(ar)-dr)/(24*60*60))
 d=d*5
 if d>0:
  print('Late Fee          : $'+str(d)+'      @ 5$/day')
 else:
  print('Successfully Returned...')


