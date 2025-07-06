import maliang
from maliang import theme
from loguru import logger
import webbrowser
import ctypes


# noinspection PyMethodMayBeStatic
class Main:
    def AIWB_Illustrate(self, cv):
        illustrate_cv = maliang.Canvas(cv)
        illustrate_cv.place(width=400, height=250, x=60, y=120)

        illustrate_cv.create_rectangle(0, 0, 400, 250, outline="grey", width=5)
        close = maliang.Button(illustrate_cv, (200, 215), text="确 定", anchor="center", command=lambda: illustrate_cv.destroy())
        maliang.Text(illustrate_cv, (20, 20), text="此处未列出在AIWB上标记为“停更”的\n软件，但一些带有“🥇”“🥈”“🌟”\n“🔴”标记的已停更软件仍会列出。")

    def AIWB(self, cv):
        aiwb_illustrate = Main()
        cv.clear()
        cv.place(width=650, height=450)

        tip = maliang.UnderlineButton(cv, (400, 10), text="关于未列出的软件……", fontsize=14, command=lambda: aiwb_illustrate.AIWB_Illustrate(cv))
        maliang.Text(cv, (20, 10), text="屏幕批注与白板软件", fontsize=26)
        InkCanvas = maliang.IconButton(cv, (10, 60), text="Ink Canvas", image=maliang.PhotoImage(file="./img/SoftWareREC/AIWB/InkCanvas.png").resize(32, 32))
        InkCanvasPlus = maliang.IconButton(cv, (170, 60), text="Ink Canvas Plus", image=maliang.PhotoImage(file="./img/SoftWareREC/AIWB/InkCanvasPlus.png").resize(32, 32))
        Inkeys = maliang.IconButton(cv, (375, 60), text="智绘教Inkeys", image=maliang.PhotoImage(file="./img/SoftWareREC/AIWB/Inkeys.png").resize(32, 32))
        InkCanvasArtistry = maliang.IconButton(cv, (10, 110), text="Ink Canvas Artistry", image=maliang.PhotoImage(file="./img/SoftWareREC/AIWB/InkCanvasArtistry.png").resize(32, 32))
        IccCE = maliang.IconButton(cv, (245, 110), text="ICC-CE", image=maliang.PhotoImage(file="./img/SoftWareREC/AIWB/icc-ce.png").resize(32, 32))
        SketchNow = maliang.IconButton(cv, (368, 110), text="SketchNow", image=maliang.PhotoImage(file="./img/SoftWareREC/AIWB/SketchNow.png").resize(32, 32))
        ppInk = maliang.Button(cv, (10, 160), text="□ ppInk")
        Inkways = maliang.IconButton(cv, (110, 160), text="Inkways", image=maliang.PhotoImage(file="./img/SoftWareREC/AIWB/Inkways.png").resize(32, 32))
        LemonxNote = maliang.Button(cv, (245, 160), text="□ 柠檬白板")

        maliang.Text(cv, (20, 230), text="课表与看板软件", fontsize=26)
        ClassIsland = maliang.IconButton(cv, (10, 280), text="ClassIsland", image=maliang.PhotoImage(file="./img/SoftWareREC/AIWB/ClassIsland.png"))
        ZongziTEK = maliang.IconButton(cv, (170, 280), text="ZongziTEK 黑板贴", image=maliang.PhotoImage(file="./img/SoftWareREC/AIWB/黑板贴.png").resize(32, 32))


if __name__ == "__main__":
    pass

