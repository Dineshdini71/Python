from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_letters = [choice(letters) for _ in range(randint(8, 10)) ]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for char in range(randint(2, 4))]
    # --------------------- LIST COMPREHENSIVE ---------------------
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    # Instead of writing the above FOR-LOOP, To simplify use the list comprehensive like written in 15,16,17 lines
    #---------------------------------------------------------------
    password_list = password_numbers + password_letters + password_symbols
    shuffle(password_list)
    password = "".join(password_list)
    # for char in password_list:
    #   password += char
    print(f"Your password is: {password}")
    pass_entry.insert(0, password)
#     This is a pyperclip library is copying the form the clipboard
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_value = website_entry.get()
    email_value = email_entry.get()
    pass_value = pass_entry.get()
    if len(website_value) == 0 or len(pass_value) == 0:
        messagebox.showinfo(title="OOPS", message="Please make sure haven't left any fields Empty")
    else:
        is_okay =messagebox.askokcancel(title=website_value, message=f"These are details entered: \n Email: \n {email_value} \n "
                                                            f"Password: \n {pass_value} Is it Okay to SAVE ?")
        if is_okay:
            with open("data.txt", "a") as f:
                f.write(f"{website_value} | {email_value} | {pass_value} \n")
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                pass_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
# window.minsize(width=300, height=300)
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
image_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image_logo)
canvas.grid(column=1, row=0)
# -------------- WEBSITE --------------
website_text = Label(text="Website:")
website_text.grid(column=0, row=1)
website_entry = Entry(width=39)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
# -------------- EMAIL/PASSWORD --------------
email_text = Label(text="Email/Username:")
email_text.grid(column=0, row=2)
email_entry = Entry(width=39)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "dinidinesh@gmail.com")
# -------------- GENERATE PASSWORD --------------
pass_text = Label(text="Password:")
pass_text.grid(column=0, row=3)
pass_entry = Entry(width=21)
pass_entry.grid(column=1, row=3)
gen_pass = Button(text="Generate Password", command=generate_password)
gen_pass.grid(column=2, row=3)
# -------------- ADD BUTTON --------------
add_btn = Button(text="ADD", width=34, command=save)
add_btn.grid(column=1, row=4, columnspan=2)
window.mainloop()