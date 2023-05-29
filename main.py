from tkinter import *

window = Tk()
window.title("Mile to Km")
window.minsize(width=50, height=30)
window.config(padx=50, pady=30)

# labels
label1 = Label(text="Equal to")
label1.grid(column=0, row=1)
label2 = Label(text="0")
label2.grid(column=1, row=1)
label3 = Label(text="Km")
label3.grid(column=2, row=1)
label4 = Label(text="Miles")
label4.grid(column=2, row=0)


# button action
def clicked():
    global entry
    miles = float(entry.get())
    # 1 miles equally to 1.60934 km
    # for an approximate result 1.609
    kilometers = miles * 1.609
    label2.config(text=kilometers)


# data entry
entry = Entry(width=7)
entry.focus_set()
entry.grid(column=1, row=0)

# button
button = Button(text="calculate", command=clicked)
button.grid(column=1, row=2)

window.mainloop()
