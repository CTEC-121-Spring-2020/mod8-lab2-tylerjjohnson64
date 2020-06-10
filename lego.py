from graphics import *

class LegoBrick:
    # construter
    def __init__(self,win,lowerleftcorner,length,color):
        self.win = win
        self.color = color
        self.lengthIn = length

        #internal representation


def main():
    win = GraphWin("lego bricks",500,375)
    win.setCoords(0.0,0.0,20.0,15.0)
    win.setBackground("light gray")

    brick1 = LegoBrick(win,Point(1,1),1,"blue")


    win.getMouse()
main()