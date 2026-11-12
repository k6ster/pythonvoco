import tkinter as tk


def joonista_sein(canvas, x, y, laius, korgus, varv):
    canvas.create_rectangle(x, y, x + laius, y + korgus, fill=varv)


def joonista_katus(canvas, x, y, laius, korgus, varv):
    canvas.create_polygon(x, y, x + laius / 2, y - korgus, x + laius, y, fill=varv)


def joonista_aken(canvas, x, y, suurus):
    canvas.create_rectangle(x, y, x + suurus, y + suurus, fill="lightblue")


def joonista_maja(canvas, x, y, laius, korgus, varv="wheat"):
    joonista_sein(canvas, x, y, laius, korgus, varv)
    joonista_katus(canvas, x - 8, y, laius + 16, laius * 0.45, "firebrick")
    joonista_aken(canvas, x + laius * 0.15, y + korgus * 0.2, laius * 0.2)
    joonista_aken(canvas, x + laius * 0.65, y + korgus * 0.2, laius * 0.2)
    canvas.create_rectangle(x + laius * 0.42, y + korgus * 0.55,
                            x + laius * 0.62, y + korgus, fill="saddlebrown")


aken = tk.Tk()
aken.title("Kolm maja")
canvas = tk.Canvas(aken, width=640, height=320, bg="skyblue")
canvas.pack()
canvas.create_rectangle(0, 250, 640, 320, fill="forestgreen")
joonista_maja(canvas, 40, 165, 120, 85, "wheat")
joonista_maja(canvas, 245, 140, 150, 110, "lightgray")
joonista_maja(canvas, 480, 180, 100, 70, "khaki")
aken.mainloop()
