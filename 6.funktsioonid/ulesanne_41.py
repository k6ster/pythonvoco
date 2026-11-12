import tkinter as tk


def joonista_ring(canvas, x, y, raadius, varv):
    canvas.create_oval(x - raadius, y - raadius, x + raadius, y + raadius, fill=varv)


aken = tk.Tk()
aken.title("Värvilised ringid")
canvas = tk.Canvas(aken, width=500, height=220, bg="white")
canvas.pack()
varvid = ["red", "orange", "gold", "green", "blue"]
for i in range(10):
    joonista_ring(canvas, 35 + i * 48, 90 + (i % 2) * 35, 15 + i % 3 * 4, varvid[i % len(varvid)])
aken.mainloop()
