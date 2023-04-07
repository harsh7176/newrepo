class Alfa:
 x=1
 _y=2
 __z=3
 def __init__(this):
  this.a=11
  this._b=12
  this.__c=13
 def disp(this):
  print()
  print(f'Alfa[x] : {Alfa.x}')
  print(f'Alfa[y] : {Alfa._y}')
  print(f'Alfa[z] : {Alfa.__z}')
 def print(this):
  print()
  print(f'Alfa[a] : {this.a}')
  print(f'Alfa[b] : {this._b}')
  print(f'Alfa[c] : {this.__c}')
 def display(this):
  print()
  print(f'Alfa[a] : {this.a}')
  print(f'Alfa[b] : {this._b}')
  print(f'Alfa[c] : {this.__c}')


class Beta(Alfa):
 def __init__(this):
  Alfa.__init__(this)
  this.a=21
 def show():
  print()
  print(f'Beta[x] : {Beta.x}')
  print(f'Beta[y] : {Beta._y}')
  #print(f'Beta[z] : {Beta.__z}')
 def print(this):
  print()
  print(f'Beta[a] : {this.a}')
  print(f'Beta[b] : {this._b}')
  #print(f'Beta[c] : {this.__c}')
  super().print()    


Beta.disp()   
b=Beta()
#b.disp() 
b.display()
b.print()

