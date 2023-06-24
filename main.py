from tkinter import *
from tkinter import messagebox
import random
import re
import json

# Password Generator Function
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    password_entry.delete(0, END)
    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    generated_password = "".join(password_list)

    password_entry.insert(0, generated_password)

# Save Password Function
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) < 11 or len(password) == 0:
        messagebox.showinfo(title="Warning", message="Please complete the details")
        validate_email(email)
    elif not validate_email(email):
        messagebox.showinfo(title="Warning", message="Please input the correct email address")
    else:
        try:
            with open("password_file.json", "r") as pf:
                data = json.load(pf) # Read old data
                data.update(new_data) # Update old data with new data

        except FileNotFoundError:
            open("password_file.json", "r")

        else:
            with open("password_file.json", "w") as pf:
                json.dump(new_data, pf, indent=2) # Saving updated data

                website_entry.delete(0, END)
                email_entry.delete(0, email_entry.index(END)-10)
                password_entry.delete(0, END)
                messagebox.showinfo(title="Confirmation", message="Data has added to the database")

# Email Verification
def validate_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if(re.fullmatch(regex, email)):
        return True
    else:
        return False

# UI Setup
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(120, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels and Entries UI Setup
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_entry = Entry(width=25)
website_entry.grid(row=1, column=1)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
email_entry = Entry(width=41)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry = Entry(width=25)
password_entry.grid(row=3, column=1)

search_button = Button(text="Search", width=15)
search_button.grid(row=1, column=2)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=41, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)



window.mainloop()