print()
try:
 n=int(input('Enter the Numerator   : '))
 d=int(input('Enter the Denominator : '))
 q=n//d
 print('\noperation successful..\n')
except ValueError as e:
 print('\nalert - '+str(e))
 q=0
except ZeroDivisionError as e:
 print('\nalert - '+str(e))
 q=-1
print('\nQuotient : '+str(q)+'\n')
 