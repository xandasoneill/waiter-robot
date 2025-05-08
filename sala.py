from graphics import *
from back import *
from random import *
from math import *


def main():
    try:
        x, y = 500, 600
        win = GraphWin('buh ba bem', x, y)
        inside_colour = 'brown'
        outer_colour = 'yellow'
        #first row of tables
        t1= Table.circular(Point(int(x/2), int(y/2)), y/20, inside_colour, outer_colour, win)
        tables = [t1]
        
        #docking station (ds)
        ds = dock((0,0), (50, 50), win)
    
        
        w = Waiter((500, 500), 20, tables, win)
        n = int()
        
        #navigate to dockstation
        w.return_to_dock(ds)
        w.go_to_table(tables, win)
        
        win.getMouse()  
        win.getMouse()
        win.close()
        pass
    finally:
        win.close()
    
main()