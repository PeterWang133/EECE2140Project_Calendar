import tkinter as tk

def on_mousewheel(event):
    canvas.yview_scroll(-1 * int(event.delta / 120), "units")

root = tk.Tk()
root.title("Scrolling Widget with Trackpad")

canvas = tk.Canvas(root)
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")

frame.bind("<Configure>", lambda event, canvas=canvas: canvas.configure(scrollregion=canvas.bbox("all")))
frame.bind("<Motion>", on_mousewheel)

for i in range(30):
    tk.Label(frame, text=f"Label {i}").pack()

root.mainloop()
