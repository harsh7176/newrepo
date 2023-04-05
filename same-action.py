print()
try:
 n=int(input('Enter the Numerator   : '))
 d=int(input('Enter the Denominator : '))
 if d>n : raise OverflowError('denominator is larger..')
 q=n/d
except ValueError as e:
 print('\ni/o alert : '+str(e))
 q=-1
except (ZeroDivisionError,OverflowError) as e:
 print('\nopn alert : '+str(e))
 q=0
else:
 print('\noperation successful..\n')
finally:
 print('\ntry block exited..\n')
print('\nQuotient : '+str(q)+'\n')