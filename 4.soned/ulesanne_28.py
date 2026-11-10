import tkinter as tk

aken = tk.Tk()
aken.title("Minu kujundid")
tahvel = tk.Canvas(aken, width=600, height=400, bg="white")
tahvel.pack()
tahvel.create_rectangle(30, 40, 180, 130, fill="red")
tahvel.create_oval(230, 40, 330, 140, fill="blue")
tahvel.create_line(380, 50, 550, 140, fill="green", width=5)
tahvel.create_oval(50, 220, 250, 310, fill="yellow")
tahvel.create_text(420, 270, text="Minu kujundid")
aken.mainloop()
