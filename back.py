# In this document there will be all functions and classes used

from graphics import *

class Table():
    
    
    def oval(p1, p2, window):
        Oval(Point(*p1), Point(*p2)).draw(window)
    
    def rectangular(p1, p2, window):
        Rectangle(Point(*p1), Point(*p2)).draw(window)
    
    def circular(p1, radius, window):
        Circle(Point(*p1), radius).draw(window)
