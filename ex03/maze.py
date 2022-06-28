import tkinter as tk
from turtle import color
import maze_maker as mm
import random

def key_down(event):
    global key
    key = event.keysym
    

def key_up(event):
    global key
    key = ""

def start():
    if mx == 1 and my == 1:
        canvas.create_rectangle(100, 100, 200, 200, fill="red")

def goal():
    x = random.randint(2, 13)
    y = random.randint(2, 8)
    while maze_bg[y][x] == 1:
        x = random.randint(2, 13)
        y = random.randint(2, 8)
        pass
    canvas.create_rectangle(x*100, y*100, x*100+100, y*100+100, fill="blue")
        


def main_proc():
    global cx, cy, mx, my, tori
    if maze_bg[my-1][mx] == 0: #一マス上が床ならば
        if key == "Up":
            my -= 1
    if maze_bg[my+1][mx] == 0: #一マス下が床ならば
        if key == "Down":
            my += 1
    if maze_bg[my][mx+1] == 0: #一マス右が床ならば
        if key == "Right":
            mx += 1
    if maze_bg[my][mx-1] == 0: #一マス左が床ならば
        if key == "Left":
            mx -= 1

            

    cx, cy = mx*100+50, my*100+50
    canvas.coords("tori", cx, cy)
    root.after(100, main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")

    canvas = tk.Canvas(root, 
                       width=1500,
                       height=900,
                       bg="black" )
    canvas.pack()

    maze_bg = mm.make_maze(15, 9) #1:壁/0:床を表す二次元のリスト
    

    mm.show_maze(canvas, maze_bg) #

    tori = tk.PhotoImage(file="fig/5.png")
    mx , my = 1, 1
    start()
    goal()
    cx, cy = mx * 100 + 50, my * 100 + 50
    canvas.create_image(cx, cy, image=tori, tag="tori")

    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    root.after(100, main_proc)
    tk.mainloop()