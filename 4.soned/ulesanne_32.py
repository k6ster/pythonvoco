import tkinter as tk

aken = tk.Tk()
tahvel = tk.Canvas(aken, width=500, height=500, bg="white", highlightthickness=0)
tahvel.pack()
for koordinaat in range(0, 501, 50):
    tahvel.create_line(koordinaat, 0, koordinaat, 500, fill="gray")
    tahvel.create_line(0, koordinaat, 500, koordinaat, fill="gray")
    asukoht = min(max(koordinaat, 12), 488)
    tahvel.create_text(asukoht, 12, text=str(koordinaat))
    tahvel.create_text(15, asukoht, text=str(koordinaat))
aken.mainloop()
