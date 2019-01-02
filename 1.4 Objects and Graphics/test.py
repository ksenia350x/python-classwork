from graphics import *
def main():
    win = GraphWin()
    shape = Rectangle(Point(50,50), Point(20,20))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    for i in range(10):
        clone = shape.clone()
        clone.draw(win)
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape.move(dx,dy)
    message = Text(Point(100,100), "Click again to quit")
    message.setSize(12)
    message.draw(win)
    win.getMouse()
    win.close()

main()
