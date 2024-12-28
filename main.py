from tkinter import Tk, BOTH, Canvas

class Window:
    tit = root.title("maze")
    can = root.Canvas(self.width, self.height)
    is_running = False

    def __init__(self, width, height):
        self.width
        self.height
        self.__root = Tk()

        self.__root.protocol("WM_DELETE_WINDOW")

    def redraw():
        root.update_ideltasks()
        root.update()

    def wait_for_close():
        is_running = True
        if is_running == True:
            self.redraw()

    def close():
        is_running = False

