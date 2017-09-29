from math import *
class point:
    def __str__(self):          #Implicitly invoked by print()
        return('('+str(self.x)+','+str(self.y)+')')
    
    def __init__(self, a, b):
        self.x = a
        self.y = b
        print(self.x)
        print(self.y)
        print(self.x + self.y)

    def translate(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y
        print("Translated x: ", self.x)
        print("Translated y: ", self.y)
        
    def o_distance(self):
        return(
            sqrt(
                (self.x * self.x) + (self.y * self.y)
            ))

    def __add__(self, p):
        return(point(self.x + p.x, self.y + p.y))

    def __mult__(self, p):
        return(point(self.x * p.x, self.y * p.y))
    
p1 = point(3,4)
print(p1)   #implicity invoked by print()

p_dist = p1.o_distance()
print(p_dist)
p1.translate(10,10)

p2 = point(10,20)
print(p2)
p2.translate(50,50)

result1 = p1 + p2
print(result1)

result2 = p1 * p2
print(result2)
