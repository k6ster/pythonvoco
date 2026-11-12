import tkinter as tk


def joonista_ruut(canvas, x, y, suurus, varv):
    canvas.create_rectangle(x, y, x + suurus, y + suurus, fill=varv)


aken = tk.Tk()
aken.title("Värvilised ruudud")
canvas = tk.Canvas(aken, width=420, height=180, bg="white")
canvas.pack()
ruudud = [(20, 20, 50, "red"), (100, 25, 65, "blue"), (195, 20, 80, "green"),
          (300, 35, 55, "orange"), (365, 25, 40, "purple")]
for x, y, suurus, varv in ruudud:
    joonista_ruut(canvas, x, y, suurus, varv)
aken.mainloop()
