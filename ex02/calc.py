from calendar import c
import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    n = btn["text"]
    #tkm.showinfo("",f"{n}ボタン押された")
    entry.insert(tk.END, n)
if __name__ == "__main__":
    root = tk.Tk()
    #root.geometry("300x500")
    root.title("電卓")

    entry = tk.Entry(root, 
                    justify="right", 
                    width=10, 
                    font=("Times New Roman",40)
                    )
    entry.grid(row=0, column=0, columnspan=3)

    r, c = 0, 0
    for n in range(9, -1, -1):
        btn = tk.Button(root, 
                        text=f"{n}", 
                        width=4, 
                        height=2,
                        font=("Times New Roman",30)
                        )
        btn.bind("<1>", button_click)
        btn.grid(row=r, column=c)
        c += 1
        if (n+2) % 3 == 0:
            r += 1
            c = 0
        
    root.mainloop()