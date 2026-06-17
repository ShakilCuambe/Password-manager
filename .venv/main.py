from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

#Password Generator

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_list = [random.choice(letters) for char in range(random.randint(8, 10))]
    password_list.extend([random.choice(symbols) for sym in range(random.randint(2, 4))])
    password_list.extend([random.choice(numbers) for num in range(random.randint(2, 4))])
    random.shuffle(password_list)

    password = "".join(password_list)
    if not password_e.get():
        password_e.insert(END, password)
        pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------   ------------------- #


def save():
    website = website_e.get()
    email = email_e.get()
    password = password_e.get()
    global new_data
    new_data = {
        website: {
            "Email": email,
            "Password": password,
        }
    }

    if website and email and password:
        yes = messagebox.askokcancel(title="??", message="Website: " + website + "\n Email: " + email + "\n Password: "
                                                         + password + "\n Are you sure about this?")
        if yes:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
                    data.update(new_data)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)

            website_e.delete(0, END)
            email_e.delete(0, END)
            password_e.delete(0, END)
    else:
        messagebox.showinfo(title="Error", message="Please, fill the fields, master")

# Search


def seach():
    global new_data
    with open("data.json", "r") as data_file:
        data = json.load(data_file)
    try:
        messagebox.showinfo(title=f"{website_e.get()}", message=f"{data[website_e.get()]}")
    except:
        messagebox.showinfo(title="Error", message="This web does not exist in our data, master")
    finally:
        website_e.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()


window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

#
website_l = Label(text="Website:")
website_l.grid(row=1, column=0)
email_l = Label(text="Email/Username:")
email_l.grid(row=2, column=0)
password_l = Label(text="Password:")
password_l.grid(row=3, column=0)
#
# Entrys
website_e = Entry(width=38)
website_e.focus()
website_e.grid(row=1, column=1, columnspan=2)
email_e = Entry(width=38)
email_e.insert(END, "Xdead@gmail.com")
email_e.grid(row=2, column= 1, columnspan=2)
password_e = Entry(width=20)
password_e.grid(row=3, column=1)

# Buttons
generate_b = Button(text="Generate Password", command=generate_password)
generate_b.grid(row=3, column=2)
add_b = Button(text="Add", width=32, command=save)
add_b.grid(row=4, column=1, columnspan=2)
search = Button(text="Search", command=seach)
search.grid(row=1, column=2, columnspan=2)

window.mainloop()
