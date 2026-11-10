import tkinter as tk

aken = tk.Tk()
tahvel = tk.Canvas(aken, width=400, height=400, highlightthickness=0)
tahvel.pack()
kulg = 50
for rida in range(8):
    for veerg in range(8):
        if (rida + veerg) % 2 == 0:
            varv = "white"
        else:
            varv = "black"
        x = veerg * kulg
        y = rida * kulg
        tahvel.create_rectangle(x, y, x + kulg, y + kulg, fill=varv, outline="")
aken.mainloop()
