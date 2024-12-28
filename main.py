from graphics import Window, Line, Point


def main():
    win = Window(800, 600)
    l = Line(Point(90,59), Point(900,400))
    win.draw_line(l,"black")

    win.wait_for_close()


main()

