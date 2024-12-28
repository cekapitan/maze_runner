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

    def close(self) -> None:
        self.__is_running = False
