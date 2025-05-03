from tkinter import *
from tkinter import messagebox
from os import path
from PIL import Image, ImageTk
from LA import *
import csv

users = []

def clear_radiobutton():
    selected_trainer.set("")

def clear():
    username.set('')
    password.set('')



def clear_checkbox():
    zumba_checkbox.deselect()
    yoga_checkbox.deselect()
    pilates_checkbox.deselect()

def register_user():
    # Get user information from entry fields
    username = username_entry1.get()
    password = password_entry1.get()
    firstname = firstname_entry.get()
    lastname = last_name_entry.get()
    phone = phone_entry.get()

    # Check if username already exists
    if not username_exists(username):
        # Create a new User object
        user = User(username, password, firstname, lastname, phone)
        # Append the user to the list of users
        users.append(user)
        # Write user data to CSV file
        register_user_csv(user)
        messagebox.showinfo("Success", "Registration successful!")
        clear_registration_fields()
        back_login()
    else:
        messagebox.showerror("Error", "Username already exists!")

def register_user_csv(user):
    with open('user_registration.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        if file.tell() == 0:  # Check if file is empty
            writer.writerow(["Username", "Password", "First Name", "Last Name", "Phone"])  # Write header if empty
        writer.writerow([user.username, user.password, user.firstname, user.lastname, user.phone])



def username_exists(username):
    try:
        with open('user_registration.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                if row and row[0] == username:
                    return True
    except StopIteration:
        return False
    except IOError as e:
        print("Error: Unable to read file:", e)
    return False



current_user = None  # Initially no user is logged in

def login_user():
    global current_user
    username = username_entry.get()
    password = password_entry.get()

    if login(username, password):
        current_user = username  # Store the currently logged-in user
        messagebox.showinfo("Success", "Login successful!")
        clear_login_fields()
        next_page1()
    else:
        messagebox.showerror("Error", "Invalid username or password!")



def login(username, password):
    try:
        with open('user_registration.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                if row and row[0] == username and row[1] == password:
                    return True
    except IOError as e:
        print("Error: Unable to read file:", e)
    return False


def clear_login_fields():
    username_entry.delete(0, END)
    password_entry.delete(0, END)


def clear_registration_fields():
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)
    firstname_entry.delete(0, END)
    last_name_entry.delete(0, END)
    phone_entry.delete(0, END)


def next_to_new_account():
    login_frame.grid_forget()
    new_account.grid(row=0, column=0)


def back_login():
    new_account.grid_forget()
    login_frame.grid()


def exit_application():
    win.destroy()


def next_to_new_account():
    login_frame.grid_forget()
    new_account.grid()
    clear()


def next_page1():
    login_frame.grid_forget()
    virtual_class.grid()


def next2():
    virtual_class.grid_forget()
    schedule_frame.grid()


def back1():
    virtual_class.grid_forget()
    login_frame.grid()


def back2():
    schedule_frame.grid_forget()
    virtual_class.grid()


def home():
    schedule_frame.grid_forget()
    login_frame.grid()


def select_trainer():
    print("Selected Trainer:", selected_trainer.get())


import csv

def submit_for_classes():
    global current_user
    if current_user:
        # Retrieve user information based on the currently logged-in user
        username, firstname, lastname, phone = get_user_info(current_user)
        selected_classes = get_selected_classes()

        # Write booking information to user_bookings.csv
        with open('user_bookings.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            if file.tell() == 0:  # Check if file is empty
                writer.writerow(["Username", "First Name", "Last Name", "Phone Number", "Booked Classes"])  # Write header if empty
            writer.writerow([username, firstname, lastname, phone, ','.join(selected_classes)])

        messagebox.showinfo("Success", "Classes booked successfully!")
        next2()
        clear_checkbox()
    else:
        messagebox.showerror("Error", "No user is logged in!")
        clear_checkbox()



def submit_trainer():
    global current_user
    if current_user:
        # Retrieve user information based on the currently logged-in user
        username, firstname, lastname, phone = get_user_info(current_user)
        selected_trainer_name = selected_trainer.get()

        # Write booking information to user_bookings_trainer.csv
        with open('user_bookings_trainer.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            if file.tell() == 0:  # Check if file is empty
                writer.writerow(["Username", "First Name", "Last Name", "Phone Number", "Booked Trainer"])  # Write header if empty
            writer.writerow([username, firstname, lastname, phone, selected_trainer_name])

        messagebox.showinfo("Success", f"Trainer booked successfully! Your chosen personal trainer {selected_trainer_name} will contact you soon to consult and schedule an appointment with you!")
        clear_radiobutton()
    else:
        messagebox.showerror("Error", "No user is logged in!")
        clear_radiobutton()

def get_selected_classes():
    selected_classes = []
    if yoga_var.get() == 1:
        selected_classes.append("Yoga Class")
    if zumba_var.get() == 1:
        selected_classes.append("Zumba Class")
    if pilates_var.get() == 1:
        selected_classes.append("Pilates Class")
    return selected_classes

def get_user_info(username):
    with open('user_registration.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            if row[0] == username:
                return row[0], row[2], row[3], row[4]
    # If the username is not found, return default values
    return "", "", "", ""





win = Tk()
win.geometry('550x750')
win.title('LA Fitness')
win.config(bg='#89c4f4')

yoga_var = IntVar()
zumba_var = IntVar()
pilates_var = IntVar()

username = StringVar()
username.set('')
password = StringVar()
password.set('')
selected_trainer = StringVar()
firstname = StringVar()
lastname = StringVar()
phone = StringVar()
username1 = StringVar()
password1 = StringVar()

# log-in Frame
login_frame = Frame(win, width=550, height=750, bg='#89c4f4')
login_frame.grid(row=0, column=0)
welcome_label = Label(login_frame, text="Welcome to LA Fitness", font=("Helvetica", 32, "bold"), bg='#89c4f4')
welcome_label.grid(row=2, column=4, columnspan=12, padx=20, pady=(20, 10))

login_label = Label(login_frame, text="Login", bg='#89c4f4', font=("Helvetica", 20, "bold"))
login_label.grid(row=4, column=6, columnspan=3, pady=10)

username_label = Label(login_frame, text="Username", bg='#89c4f4', font=("Chalkboard", 18, "italic", "underline"))
username_label.grid(row=5, column=5)

username_entry = Entry(login_frame, width=20, textvariable=username)
username_entry.grid(row=5, column=6, columnspan=3, pady=5)

password_label = Label(login_frame, text="Password", bg='#89c4f4', font=("Chalkboard", 18, "italic", "underline"))
password_label.grid(row=6, column=5)

password_entry = Entry(login_frame, width=20, textvariable=password, show="****")
password_entry.grid(row=6, column=6, columnspan=3, pady=5)

button_label = Button(login_frame, text="Sign in", highlightbackground='#89c4f4', command=login_user)
button_label.grid(row=7, column=6, columnspan=1, padx=(5, 2), pady=5)

exit_button = Button(login_frame, text="Exit", command=exit_application, highlightbackground='#89c4f4')
exit_button.grid(row=7, column=7, columnspan=1, padx=(2, 5), pady=5)

image = Image.open('LA_Fitness.jpg')
new_width = 545
new_height = 405
image = image.resize((new_width, new_height))
photo = ImageTk.PhotoImage(image)

image_label = Label(login_frame, image=photo)
image_label.grid(row=3, column=5, columnspan=12)

# Create a new account
create_button = Button(login_frame, text="Create New Account", command=next_to_new_account,
                       highlightbackground='#89c4f4')
create_button.grid(row=8, column=6, columnspan=2)
new_account = Frame(win, width=500, height=500, bg='#89c4f4')
new_account.grid_propagate(False)

heading = Label(new_account, text='Registration Form', font=("Helvetica", 32, "bold"), bg='#89c4f4')
heading.grid(row=0, column=0, columnspan=12, padx=20, pady=(20, 10))

first_name = Label(new_account, text='First Name', bg='#89c4f4', font=("Arial", 18))
first_name.grid(row=1, column=1)

firstname_entry = Entry(new_account, width=20, textvariable=firstname)
firstname_entry.grid(row=1, column=2, columnspan=3, pady=5)

last_name = Label(new_account, text='Last Name', bg='#89c4f4', font=("Arial", 18))
last_name.grid(row=2, column=1)  # Specify the column for the label
last_name_entry = Entry(new_account, width=20, textvariable=lastname)
last_name_entry.grid(row=2, column=2, columnspan=3, pady=5)

phone = Label(new_account, text='Phone Number', bg='#89c4f4', font=("Arial", 18))
phone.grid(row=3, column=1)
phone_entry = Entry(new_account, width=20, textvariable=phone)
phone_entry.grid(row=3, column=2, columnspan=3, pady=5)

username_label1 = Label(new_account, text='Username', bg='#89c4f4', font=("Arial", 18))
username_label1.grid(row=4, column=1)  # Specify the column for the label
username_entry1 = Entry(new_account, width=20, textvariable=username1)
username_entry1.grid(row=4, column=2, columnspan=3, pady=5)

password_label1 = Label(new_account, text='Password', bg='#89c4f4', font=("Arial", 18))
password_label1.grid(row=5, column=1)  # Specify the column for the label
password_entry1 = Entry(new_account, width=20, textvariable=password1)
password_entry1.grid(row=5, column=2, columnspan=3, pady=5)

register_button = Button(new_account, command=register_user, font=("Arial", 16), text='Register', width=10,
                         highlightbackground='#89c4f4')
register_button.grid(row=6, column=2, pady=(10, 10), padx=(20, 0), sticky=W)
backback_button = Button(new_account, command=back_login, font=("Arial", 16), text='Back', width=10,
                         highlightbackground='#89c4f4')
backback_button.grid(row=7, column=2, pady=(10, 10), padx=(20, 0), sticky=W)

# Virtual Booking Classes Frame
virtual_class = Frame(win, width=550, height=750, bg='#89c4f4')
virtual_class.grid_propagate(False)  # Prevent frame from resizing to fit widgets

class_label = Label(virtual_class, text="Virtual Booking Classes", bg='#89c4f4', font=("Helvetica", 20, "bold"))
class_label.grid(row=0, column=0, columnspan=2, pady=10)

yoga_img = Image.open('yoga.jpg')  # Open the new image
new_width = 250
new_height = 150
yoga_img = yoga_img.resize((new_width, new_height))
photo1 = ImageTk.PhotoImage(yoga_img)  # Create PhotoImage object with the new image

image_label1 = Label(virtual_class, image=photo1)  # Update label with new image
image_label1.grid(row=1, column=0, columnspan=2, padx=10, pady=5)
yoga_description = "Yoga Class:\n- These classes unite your breath with your body\n offering a variety of poses accessible to all\n levels of yoga practitioners.\n- Time: Tuesday and Thursday at 6:30 A.M.\n- Duration: 2 hours"

# Display the yoga class description
description_label = Label(virtual_class, text=yoga_description, bg='#cdd1e4', font=("Arial", 12), justify=LEFT)
description_label.grid(row=1, column=2, columnspan=2, padx=10, pady=5, sticky=W)

yoga_checkbox = Checkbutton(virtual_class, text="Yoga Class", bg='#89c4f4', variable=yoga_var)
yoga_checkbox.grid(row=2, column=0, sticky=W)

zumba_img = Image.open('zumba.jpg')  # Open the new image
new_width = 250
new_height = 150
zumba_img = zumba_img.resize((new_width, new_height))
photo2 = ImageTk.PhotoImage(zumba_img)  # Create PhotoImage object with the new image

image_label2 = Label(virtual_class, image=photo2)  # Update label with new image
image_label2.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

zumba_description = "Zumba Class:\n- Zumba classes combine latin and international\n music and dance to create a dynamic\n calorie-burning formof workout for people of all\n fitness levels and age groups.\n- Time: Monday and Wednesdat at 4:30 P.M.\n- Duration: 2 hours"
description_label2 = Label(virtual_class, text=zumba_description, bg='#cdd1e4', font=("Arial", 12), justify=LEFT)
description_label2.grid(row=4, column=2, columnspan=2, padx=10, pady=5, sticky=W)

zumba_checkbox = Checkbutton(virtual_class, text="Zumba Class", bg='#89c4f4', variable=zumba_var)
zumba_checkbox.grid(row=5, column=0, sticky=W)

pilates_img = Image.open('pilates.jpg')  # Open the new image
new_width = 250
new_height = 150
pilates_img = pilates_img.resize((new_width, new_height))
photo3 = ImageTk.PhotoImage(pilates_img)  # Create PhotoImage object with the new image

image_label3 = Label(virtual_class, image=photo3)  # Update label with new image
image_label3.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

pilates_description = "Pilates Class\n- Mat-based Pilates class focuses on strength,\n stability, posture, proper breath control, and\n flexibility.\n- Time: Everyday at 7:00 P.M.\n- Duration: 1:30 hours"
description_label3 = Label(virtual_class, text=pilates_description, bg='#cdd1e4', font=("Arial", 12), justify=LEFT)
description_label3.grid(row=7, column=2, columnspan=2, padx=10, pady=5, sticky=W)

pilates_checkbox = Checkbutton(virtual_class, text="Pilates Class", bg='#89c4f4', variable=pilates_var)
pilates_checkbox.grid(row=8, column=0, sticky=W)

submit_button = Button(virtual_class, command=submit_for_classes, font=("Arial", 16), text='Reserve', width=10,
                       highlightbackground='#89c4f4')
submit_button.grid(row=10, column=1, pady=(10, 10), padx=(20, 0), sticky=W)

back_button = Button(virtual_class, command=back1, font=("Arial", 16), text='Back', width=10,
                     highlightbackground='#89c4f4')
back_button.grid(row=11, column=1, pady=(10, 10), padx=(10, 10), sticky=E)

exit_button = Button(virtual_class, command=exit_application, font=("Arial", 16), text='Exit', width=10,
                     highlightbackground='#89c4f4')
exit_button.grid(row=10, column=2, pady=(10, 10), padx=(20, 0), sticky=W)

next2_button = Button(virtual_class, command=next2, font=("Arial", 16), text='Next', width=10,
                      highlightbackground='#89c4f4')
next2_button.grid(row=11, column=2, pady=(10, 10), padx=(20, 0), sticky=W)

# Schedule
schedule_frame = Frame(win, width=550, height=750, bg='#96281b')
schedule_frame.grid_propagate(False)

schedule_label = Label(schedule_frame, text="Schedule with Personal Trainers", bg='#fef160',
                       font=("Helvetica", 20, "bold"))
schedule_label.grid(row=0, column=0, pady=10)

khoa = Image.open('khoa.jpg')
new_width = 250
new_height = 150
khoa = khoa.resize((new_width, new_height))
photo4 = ImageTk.PhotoImage(khoa)

image_label4 = Label(schedule_frame, image=photo4)
image_label4.grid(row=1, column=0, pady=5)

trainer1 = "\t      Khoa Pham\n I offer some PNF stretching towards the\n end of the workout, PNF is a stretching\n technique that can improve your range of\n motion. Many therapists use PNF to help\n people regain their range of motion after\n injury or surgery. However, it can also\n be used by athletes and dancers to\n improve their flexibility.\n\tPrice: $60/hr."
khoa_des = Label(schedule_frame, text=trainer1, font=("Arial", 12), justify=LEFT, bg='pink')
khoa_des.grid(row=1, column=2, columnspan=2, padx=5, pady=5, sticky=W)

trainer2 = "\t        Linny Alexson\n Skilled in helping clients with weight loss,\n strength training, and sport specific\n training. I am also capable of providing\n nutrition guidance and teaching healthy\n habits to promote wellbeing.\n\tPrice: $75/hr"

linny = Image.open('linny.jpg')
new_width = 250
new_height = 150
linny = linny.resize((new_width, new_height))
photo5 = ImageTk.PhotoImage(linny)

image_label5 = Label(schedule_frame, image=photo5)
image_label5.grid(row=2, column=0, pady=10)
linny_des = Label(schedule_frame, text=trainer2, bg='pink', font=("Arial", 12), justify=LEFT)
linny_des.grid(row=2, column=2, columnspan=2, padx=5, pady=5, sticky=W)

trainers = [
    ("Khoa Pham"),
    ("Linny Alexson")
]

question = Label(schedule_frame, text="Choose your Personal Trainers", bg='#fef160', font=("Helvetica", 20, "bold"))
question.grid(row=4, column=0, pady=10)

# Display radio buttons for each trainer
for idx, trainer in enumerate(trainers, start=5):
    radio = Radiobutton(schedule_frame, text=trainer, variable=selected_trainer, value=trainer, bg='#d24d57',
                        font=("Arial", 12), command=select_trainer)
    radio.grid(row=idx, column=0, columnspan=2, padx=10, pady=5, sticky=W)

submit_button2 = Button(schedule_frame, command=submit_trainer, font=("Arial", 16), text='Book', width=10,
                        highlightbackground='#f1828d')
submit_button2.grid(row=8, column=0, pady=(10, 10), padx=(20, 0), sticky=E, columnspan=2)

exit_button = Button(schedule_frame, command=exit_application, font=("Arial", 16), text='Exit', width=10,
                     highlightbackground='#f1828d')
exit_button.grid(row=8, column=1, pady=(10, 10), padx=(5, 20), sticky=E, columnspan=2)

back_button2 = Button(schedule_frame, command=back2, font=("Arial", 16), text='Back', width=10,
                      highlightbackground='#f1828d')
back_button2.grid(row=9, column=0, sticky=E, columnspan=2)

home_button = Button(schedule_frame, command=home, font=("Arial", 16), text='Home', width=10,
                     highlightbackground='#f1828d')
home_button.grid(row=9, column=1, sticky=W, padx=5, columnspan=2)
win.mainloop()