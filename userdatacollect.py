from tkinter import *

# Create main window
root = Tk()
root.title("Student Registration Form")
root.geometry("400x350")
root.resizable(False, False)

# Heading
heading = Label(root, text="Contact App",
                font=("Arial", 18, "bold"))
heading.pack(pady=20)

# Name
Label(root, text="Name:", font=("Arial", 12)).pack()
name_entry = Entry(root, width=30, font=("Arial", 12))
name_entry.pack(pady=5)

# Email
Label(root, text="Email:", font=("Arial", 12)).pack()
email_entry = Entry(root, width=30, font=("Arial", 12))
email_entry.pack(pady=5)

# Mobile
Label(root, text="Mobile:", font=("Arial", 12)).pack()
mobile_entry = Entry(root, width=30, font=("Arial", 12))
mobile_entry.pack(pady=5)


# Submit function
def submit():
    name = name_entry.get()
    email = email_entry.get()
    mobile = mobile_entry.get()

    print("Student Details")
    print("Name:", name)
    print("Email:", email)
    print("Mobile:", mobile)


# Submit button
submit_btn = Button(root, text="Submit",
                    command=submit,
                    bg="green", fg="white",
                    font=("Arial", 12))
submit_btn.pack(pady=20)

# Run application
root.mainloop()