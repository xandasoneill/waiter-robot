from graphics import *
from back import *


def main():
    win = GraphWin('buh ba bem', 800, 600)
    
    #first row of tables
    Table.circular((150,150),50, win)
    Table.rectangular((337,100), (438, 200), win)
    Table.oval((550, 100), (700, 200), win)
    
    #second row of tables
    Table.rectangular((112, 400), (188, 500), win)
    Table.circular((400,450), 50, win)
    Table.oval((550, 400), (700,500 ), win)
    win.getMouse()  
    win.getMouse()
    win.close()
    
main()