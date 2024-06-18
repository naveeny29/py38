class Father: 
   def height(self): 
      print('Height is 6.0 foot') 
class Mother: 
   def color(self): 
      print('Color is brown') 
class Child(Father, Mother): 
   pass 

c = Child() 
print('Child\'s inherited qualities:') 
c.height() 
c.color()
