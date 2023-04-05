from math import *

class Shape:
 def __init__(this,left=0,top=0,right=0,bottom=0):
  this.left=left
  this.top=top
  this.right=right
  this.bottom=bottom
 def area(this):
  assert False, 'method not found - area()'
 def perimeter(this):
  assert False, 'method not found - perimeter()'

class Circle(Shape):
 def __init__(this,cx=0,cy=0,radius=0):
  this.cx=cx
  this.cy=cy
  this.radius=radius
  super().__init__(cx-radius,cy-radius,cx+radius,cy+radius)
 def area(this):
  return pi*this.radius**2
 def perimeter(this):
  return 2*pi*this.radius

class Rectangle(Shape):
 def __init__(this,x=0,y=0,width=0,height=0):
  this.width=width
  this.height=height
  super().__init__(x,y,x+width,y+height)
 def area(this):
  return this.width*this.height
 def perimeter(this):
  return 2*(this.width+this.height)