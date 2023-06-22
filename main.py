from tkinter import *

# Password Generator Function

# Save Password Function
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    with open("password_file.txt", "a") as pf:
        pf.write(f"{website} | {email} | {password}\n")
        website_entry.delete(0, END)
        email_entry.delete(0, email_entry.index(END)-10)
        password_entry.delete(0, END)

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
website_entry = Entry(width=41)
website_entry.grid(row=1, column=1, columnspan=2)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
email_entry = Entry(width=41)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry = Entry(width=25)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=41, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)



window.mainloop()