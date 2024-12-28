from tkinter import Tk, BOTH, Canvas
from typing import List, Dict

    # tit = root.title("maze")
    # can = root.Canvas(self, width : int, height: int)
    # is_running = False
class Window:
    def __init__(self, width : int, height : int):
        self.__root = Tk()
        self.__root.title("Maze_Solver")
        self.__canvas = Canvas(self.__root, bg = "white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE", self.close)

    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self) -> None:
        self.__is_running = True
        while self.__is_running:
            self.redraw()
        print("window closed...")

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

    def close(self) -> None:
        self.__is_running = False
    
class Point:
    def __init__(self, x : int, y: int) -> None:
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1 : int, p2: int) -> None:
        self.p1 = p1
        self.p2 = p2
    
    def draw(self, canvas, fill_color="black") -> None:
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)
