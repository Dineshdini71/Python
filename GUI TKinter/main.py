from tkinter import *

window = Tk()
window.title("My GUI Project")
window.minsize(width=500, height=400)

# lable

my_label = Label(text='NEW LABEL', font=('Arial', 24, 'bold'))
my_label.grid(column=0, row=0)

new_button = Button(text="New click me")
new_button.grid(column=2, row=0)

# Button
button = Button(text="click me")
button.grid(column=1, row=1)

# Entry
entry = Entry(width=10)
entry.grid(column=3, row=4)
































window.mainloop()
