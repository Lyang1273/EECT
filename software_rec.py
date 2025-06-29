import maliang
from maliang import theme
from loguru import logger
import webbrowser
import ctypes


# noinspection PyMethodMayBeStatic
class Main:
    def AIWB(self, cv):
        cv.clear()
        cv.place(width=650, height=450)

        InkCanvas = maliang.IconButton(cv, (10, 60), text="Ink Canvas", image=maliang.PhotoImage(file="./img/SoftWareREC/AIWB/InkCanvas.png").resize(32, 32))
        InkCanvasPlus = maliang.IconButton(cv, (170, 60), text="Ink Canvas Plus", image=maliang.PhotoImage(file="./img/SoftWareREC/AIWB/InkCanvasPlus.png").resize(32, 32))
        Inkeys = maliang.IconButton(cv, (375, 60), text="智绘教Inkeys", image=maliang.PhotoImage(file="./img/SoftWareREC/AIWB/Inkeys.png").resize(32, 32))
        InkCanvasArtistry = maliang.IconButton(cv, (10, 110), text="Ink Canvas Artistry", image=maliang.PhotoImage(file="./img/SoftWareREC/AIWB/InkCanvasArtistry.png").resize(32, 32))
        IccCE = maliang.IconButton(cv, (245, 110), text="ICC-CE", image=maliang.PhotoImage(file="./img/SoftWareREC/AIWB/icc-ce.png").resize(32, 32))
        SketchNow = maliang.IconButton(cv, (368, 110), text="SketchNow", image=maliang.PhotoImage(file="./img/SoftWareREC/AIWB/SketchNow.png").resize(32, 32))


if __name__ == "__main__":
    pass

