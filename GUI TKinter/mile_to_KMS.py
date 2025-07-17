from tkinter import *


window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=400, height=200)
window.config(padx=20, pady=20)

def miles_to_km():
    mile = float(mile_input.get())
    km = round(mile * 1.609)
    km_input.config(text=f"{km}")




mile_input = Entry(width=7)
mile_input.grid(column=2, row=0)

mile_label = Label(text="Miles")
mile_label.grid(column=3, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=1, row=1)

km_input = Label(text=0)
km_input.grid(column=2, row=1)

km_label = Label(text="KiloMeters")
km_label.grid(column=3, row=1)

converter_btn = Button(text="Calculate", command=miles_to_km)
converter_btn.grid(column=2, row=2)

# mile = 1 and Km = 1.609

window.mainloop()