# In this document there will be all functions and classes used

from graphics import *
from math import *


def add_points(p1, p2):
    return Point(p1.getX() + p2.getX(), p1.getY() + p2.getY())

def subtract_points(p1, p2):
    return Point(p1.getX() - p2.getX(), p1.getY() - p2.getY())


def normalize(vector):
    x = vector.getX()
    y = vector.getY()
    return Point(x/sqrt(x**2 + y**2), y/sqrt(x**2 + y**2))

def distance(p1, p2):
    return sqrt((p1.getX() - p2.getX())**2 + (p1.getY() - p2.getY())**2)

def is_inside(table, mouse):
        if isinstance(table, Circle):
            
            if distance(mouse, table.getCenter()) < table.getRadius():
                return True
        elif isinstance(table, (Rectangle, Oval)):
            p1 = table.getP1()
            p2= table.getP2()
            big_x = max(p1.getX(), p2.getX())
            big_y = max(p1.getY(), p2.getY()) 
            small_x = min(p1.getX(), p2.getX())
            small_y = min(p1.getY(), p2.getY()) 
            
            if  small_x < mouse.getX() < big_x and small_y < mouse.getY() < big_y:
                return True
            
class Table:
    

    def oval(p1, p2, inside_colour, outer_colour, window):
        shape = Oval(p1, p2)
        shape.draw(window)
        shape.setFill(inside_colour)
        shape.setOutline(outer_colour)
        return shape

    def rectangular(p1, p2, inside_colour, outer_colour, window):
        shape = Rectangle(p1, p2)
        shape.draw(window)
        shape.setFill(inside_colour)
        shape.setOutline(outer_colour)
        return shape

    def circular(p1, radius, inside_colour, outer_colour, window):
        shape = Circle(p1, radius)      
        shape.draw(window)
        shape.setFill(inside_colour)
        shape.setOutline(outer_colour)
        return shape


def dock(p1, p2, window):
    shape = Rectangle(Point(*p1), Point(*p2))
    shape.draw(window)
    return shape


    
class Waiter:
    def __init__(self, p1, radius, tables, window):
        waitercenter = Point(*p1)
        xluz, yluz = waitercenter.getX() + 10, waitercenter.getY() + 10
        coorluz = (xluz, yluz)      
        self.shape = [Circle(waitercenter, radius), Circle(Point(*coorluz), 3)]
        for shape in self.shape:
            shape.draw(window)
            
        self.luz = self.shape[1]
        self.luz.setFill('green')
        
        self.status = 'free'
        self.battery = 100
        self.docked = False
 

    def navigate(self, vector):
        
        for shape in self.shape:
            
            x = vector.getX()
            y = vector.getY()
            shape.move(x, y)
            self.battery_usage()
            print(self.battery)
        
    
    def go_to_table(self, tables, window):
        mouse = window.getMouse()
        for table in tables:
            if is_inside(table ,mouse):
                for _ in range(1000):
                    vector = subtract_points(table.getCenter(), self.shape[0].getCenter())
                    vector_norm = normalize(vector)
                    self.navigate(vector_norm)
                    time.sleep(0.05)
                    if (distance(self.shape[0].getCenter(), table.getCenter()) - 0.24) < 0.1:
                        return None
    
    def waiter_light(self):
        if 20 < self.battery < 50:
            self.luz.setFill('orange')
        elif self.battery < 20:
            self.luz.setFill('red')
        elif self.battery > 50:
            self.luz.setFill('green')
    
    def battery_usage(self):
        self.battery -= 0.05
        self.waiter_light()
    
    def return_to_dock(self, dock):
        for _ in range(1000):
            vector_ds_w = (subtract_points(dock.getCenter(), self.shape[0].getCenter()))  
            vector_ds_w_norm = normalize(vector_ds_w)
            self.navigate(vector_ds_w_norm)  
            time.sleep(0.05)
            distance_ds_w = distance(dock.getCenter(), self.shape[0].getCenter())
            if (distance_ds_w - 0.24) < 0.01 :
                break
        self.docked = True
        self.charging()
    
    def charging(self):
        if self.docked == True:
            while self.battery <= 100:
                self.battery += 10
                self.waiter_light()
                print(self.battery)
                time.sleep(1)
            if self.battery > 100:
                self.battery = 100
        print(self.battery)
            
    