import tkinter as tk

window = tk.Tk()
window.title("Rock Paper Sicorss")
window.configure(background = "white")

title = tk.Label(window, text = "Rock Paper Sicorss!", bg = "pink", fg = "black", font = ("Helvetica", 35), bd = 3, pady = 5, relief = tk.RIDGE).pack(pady = 10)

option_frame = tk.Frame(window, borderwidth = 5, relief = tk.GROOVE)
choice_label = tk.Label(option_frame, text = "Your options").pack()

option_frame.pack(fill = tk.BOTH, expand = True, pady = 10, padx = 20)


result_frame = tk.Frame(window, relief = tk.GROOVE, borderwidth = 3 )


result_frame.pack(fill = tk.BOTH, expand = True, padx = 10, pady = 20)



window.mainloop()
