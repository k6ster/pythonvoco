import tkinter as tk

laius = 600
korgus = 300
triip = korgus / 3
aken = tk.Tk()
aken.title("Eesti lipp")
tahvel = tk.Canvas(aken, width=laius, height=korgus, highlightthickness=0)
tahvel.pack()
tahvel.create_rectangle(0, 0, laius, triip, fill="blue", outline="")
tahvel.create_rectangle(0, triip, laius, 2 * triip, fill="black", outline="")
tahvel.create_rectangle(0, 2 * triip, laius, korgus, fill="white", outline="")
aken.mainloop()
