from tkinter import Tk, messagebox
from tkinter import *
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title("Password Manager")
root.config(padx=20, pady=20, bg='#006a71')
canvas = Canvas(height=200, width=200, bg='#006a71', highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image, anchor=CENTER)
canvas.grid(row=0, column=0)
# =======================Variables================================#
web_input = StringVar()
email_input = StringVar()
pass_key_input = StringVar()


# =========================Function========================#
def on_entry_clique_web(event):
    """Function that gets called whenever entry is clicked"""
    if web_site_entry.get() == "Enter the website":
        web_site_entry.delete(0, 'end')  # delete all the text in the entry
        web_site_entry.insert(0, "")  # insert blank for user index
        web_site_entry.config(fg='black')


def focus_out_web(event):
    if web_site_entry.get() == '':
        web_site_entry.insert(0, "Enter the website")
        web_site_entry.config(fg='grey')


def on_entry_clique_email(event):
    """Function that gets called whenever  email entry is clicked"""
    if email_username_entry.get() == "Enter your Email/Username":
        email_username_entry.delete(0, 'end')
        email_username_entry.insert(0, "")
        email_username_entry.config(fg='black')


def focus_out_email(event):
    if email_username_entry.get() == '':
        email_username_entry.insert(0, "Enter your Email/Username")
        email_username_entry.config(fg='grey')


def on_entry_clique_pass(event):
    """Function that gets called whenever entry is clicked"""
    if password_key_entry.get() == "Enter password/Generate":
        password_key_entry.delete(0, 'end')  # delete all the text in the entry
        password_key_entry.insert(0, "")  # insert blank for user index
        password_key_entry.config(fg='black')


def focus_out_pass(event):
    if password_key_entry.get() == '':
        password_key_entry.insert(0, "Enter password/Generate")
        password_key_entry.config(fg='grey')


def add_pass_key():
    if email_input.get() != "Enter your Email/Username" and web_input.get() != "Enter the website" \
            and pass_key_input.get() != "Enter password/Generate" \
            and email_input.get() != "" and web_input.get() != "" and pass_key_input.get() != "":
        new_pass_key = f"Website: {web_input.get()} | Email/Username: {email_input.get()} | " \
                       f"Key: {pass_key_input.get()}\n"
        # print(new_pass_key)
        save_data = messagebox.askokcancel(title=web_input.get(),
                                           message=f"These are the details entered:\nEmail/Username: {email_input.get()}"
                                                   f"\nPassword: {pass_key_input.get()}\nIs it ok to save?")
        if save_data > 0:
            with open('Password_Manager', 'a+') as f:
                f.write(new_pass_key)
                web_site_entry.delete(0, 'end')
                web_site_entry.insert(0, "Enter the website")
                web_site_entry.config(fg='grey')
                email_username_entry.delete(0, 'end')
                email_username_entry.insert(0, "Enter your Email/Username")
                email_username_entry.config(fg='grey')
                password_key_entry.delete(0, 'end')
                password_key_entry.insert(0, "Enter password/Generate")
                password_key_entry.config(fg='grey')
    else:
        messagebox.showwarning(title='Empty Fields', message="Don't leave any fields blank")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_generator():
    global pass_key_input
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '@']

    lst_letter = [choice(letters) for _ in range(randint(6, 8))]

    lst_symbol = [choice(symbols) for _ in range(randint(1, 2))]

    lst_number = [choice(numbers) for _ in range(randint(1, 2))]

    password_list = lst_letter + lst_symbol + lst_number

    shuffle(password_list)

    password = "".join(password_list)
    password_key_entry.delete(0, 'end')
    password_key_entry.insert(0, password)
    password_key_entry.config(fg='black')
    pyperclip.copy(password)




# ========================Fame=============================#


# main_frame = Frame(root,width=200,height=250,bd=16)
# main_frame.grid()
text_label = Frame(root, bd=10, relief="ridge", height=70, width=100, padx=10, pady=10, bg='#006a71')
text_label.grid(row=1, column=0, )
# ========================Label % Entry=====================#
web_site = Label(text_label, text="Website:", font=("helvetica", 12, 'bold'), bg='#006a71')
web_site.grid(row=1, column=0)
web_site_entry = Entry(text_label, width=35, bd=5, bg='#e8e8e8', textvariable=web_input)
web_site_entry.insert(0, "Enter the website")
web_site_entry.bind('<FocusIn>', on_entry_clique_web)
web_site_entry.bind('<FocusOut>', focus_out_web)
web_site_entry.config(fg='grey')
web_site_entry.grid(row=1, column=1, columnspan=2)

email_username = Label(text_label, text="Email/Username:", font=("helvetica", 12, 'bold'), bg='#006a71')
email_username.grid(row=2, column=0)
email_username_entry = Entry(text_label, width=35, bd=5, bg='#e8e8e8', textvariable=email_input)
email_username_entry.insert(0, "Enter your Email/Username")
email_username_entry.bind('<FocusIn>', on_entry_clique_email)
email_username_entry.bind('<FocusOut>', focus_out_email)
email_username_entry.config(fg='grey')
email_username_entry.grid(row=2, column=1, columnspan=2)

password_key = Label(text_label, text="Password:", font=("helvetica", 12, 'bold'), bg='#006a71')
password_key.grid(row=3, column=0)
password_key_entry = Entry(text_label, width=21, bd=5, bg='#e8e8e8', textvariable=pass_key_input)
password_key_entry.grid(row=3, column=1)
password_key_entry.insert(0, "Enter password/Generate")
password_key_entry.bind('<FocusIn>', on_entry_clique_pass)
password_key_entry.bind('<FocusOut>', focus_out_pass)
password_key_entry.config(fg='grey')

generate_button = Button(text_label, text="Generate Password", font=("helvetica", 8, 'bold'), width=14, bg="#c0ded9"
                         , command=pass_generator)
generate_button.grid(row=3, column=2)

add_button = Button(text_label, text="Add", font=("helvetica", 12, 'bold'), width=30, relief="groove", bg="#c0ded9"
                    , command=add_pass_key)
add_button.grid(row=4, column=1, columnspan=2)
author_rfm = Label(text="The Palm App", anchor=E, bg='#006a71', font=("helvetica", 10, 'bold'), justify='right')
author_rfm.grid(row=2)

print(web_input.get())
print(email_input.get())
print(pass_key_input.get())
root.mainloop()
