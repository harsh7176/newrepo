nam=input('\nEnter your Name : ')  #input function returns string
print()
print('Hi '+nam)
print('Hi',nam)  #default separator is space" " ,positioning argument 1st priority and 2nd is keyword argument if both arguments are present in it

print(f'Hi {nam}')     

print('Hi {}'.format(nam))   #format is a method of string

print('Hi %s' %nam)
