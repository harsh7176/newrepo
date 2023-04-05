from datetime import *
from time import *

print()

fmt='%d/%m/%Y'

doi=date.today()
print('Date of Issue     : ' + doi.strftime(fmt))

dor=doi+timedelta(15)
print('Date of Return    : ' + dor.strftime(fmt))

rd=input('Returned On       : ')

try:
 rd=date(*strptime(rd,fmt)[:3])

 print('\nStatus            : ',end='')
 if rd<=dor:
  print("book returned within return period..\n")
 else:
  d=(rd-dor).days
  print('return delayed by ' + str(d) + ' days')
  print('Late Fee          : $'+str(d*5)+'  @ $5/day')

except ValueError as e:
 print('\nalert - ' + str(e))

print()
