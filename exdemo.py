print()
try:
 n=int(input('Enter the Numerator   : '))
 d=int(input('Enter the Denominator : '))
 q=n//d
except:
 print('\nalert - i/o or zero division..\n')
 q=0

print('\nQuotient  : ',q)