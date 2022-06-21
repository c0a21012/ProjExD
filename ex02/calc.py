from calendar import c
import tkinter as tk
import tkinter.messagebox as tkm
import math

def button_click(event):
    btn = event.widget
    n = btn["text"]
    if n == "=":
        eq = entry.get()
        res = eval(eq)
        entry.delete(0, tk.END)
        entry.insert(tk.END, res)

    #三角関数の計算は角度(度数法）を入力
    elif n == "sin": 
        get = entry.get()
        ans = eval(get)
        sin = math.sin(math.radians(ans))    
        entry.delete(0, tk.END)
        entry.insert(tk.END, round(sin, 3))
    elif n == "cos":
        get = entry.get()
        ans = eval(get)
        cos = math.cos(math.radians(ans))
        entry.delete(0, tk.END)
        entry.insert(tk.END, round(cos, 3))
    elif n == "tan":
        get = entry.get()
        ans = eval(get)
        tan = math.tan(math.radians(ans))
        entry.delete(0, tk.END)
        entry.insert(tk.END, round(tan, 3))
    elif n == "A":
        entry.delete(0, tk.END)
    

    else:
        entry.insert(tk.END, n)


    #tkm.showinfo("",f"{n}ボタン押された")
    
if __name__ == "__main__":
    root = tk.Tk()
    #root.geometry("300x500")
    root.title("電卓")

    entry = tk.Entry(root, 
                    justify="right", 
                    width=10, 
                    font=("Times New Roman", 40)
                    )
    entry.grid(row=0, column=0, columnspan=3)

    r, c = 2, 0
    for i, n in enumerate([i for i in range(9, -1, -1)] + ["+","-", "*", "/", "sin","cos", "tan", "A", "="]):
        btn = tk.Button(root, 
                        text=f"{n}", 
                        width=4, 
                        height=2,
                        font=("Times New Roman", 30)
                        )
        btn.bind("<1>", button_click)
        btn.grid(row=r, column=c)
        c += 1
        if (i+1) % 5 == 0:
            r += 1
            c = 0
        
    root.mainloop()