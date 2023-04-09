from tkinter import *
import csv

class GUI:
    def __init__(self, window):
        """
        - The code provided is meant to guide you on the dimensions used and variable names standards.
        - Add the widgets responsible for the age, status, and save button.
        """
        self.window = window

        #Name entry frame
        self.frame_name = Frame(self.window)
        self.frame_name.pack(anchor='w', pady=10)  # anchor='w' helps to change the frame position from center to west.

        self.name_label = Label(self.frame_name, text='Name')
        self.name_label.pack(padx=5, side='left')

        self.name_entry = Entry(self.frame_name)
        self.name_entry.pack(padx=5, side='left')

        #age entry frame
        self.frame_age = Frame(self.window)
        self.frame_age.pack(anchor='w', pady=10)

        self.age_label = Label(self.frame_age, text='Age')
        self.age_label.pack(padx=11, side='left')

        self.age_entry = Entry(self.frame_age)
        self.age_entry.pack(padx=5, side='left')



        #Status entry frame
        self.frame_status = Frame(self.window)
        self.frame_status.pack(anchor='w', pady=10)
        self.status_label = Label(self.frame_status, text='Status: ')
        self.status_label.pack(padx=5, side='left')

        self.status_selection = IntVar()

        choice_student = Radiobutton(self.frame_status, text="Student", variable=self.status_selection, value=1)
        choice_student.pack(side="left")

        choice_staff = Radiobutton(self.frame_status, text="Staff", variable=self.status_selection, value=2)
        choice_staff.pack(side="left")

        choice_both = Radiobutton(self.frame_status, text="Both", variable=self.status_selection, value=3)
        choice_both.pack(side="left")

        #Save button frame
        self.save_button_frame = Frame(self.window)
        self.save_button_frame.pack(anchor='s', pady=10)
        self.save_button = Button(self.save_button_frame, text="SAVE", command=self.clicked)
        self.save_button.pack()



    def clicked(self):
        try:
            name = self.name_entry.get()
            age = self.age_entry.get()
            status_key = self.status_selection.get()

            #Check if age is a number, clear if not
            if not(age.isdigit()):
                raise ValueError

            #Assign status based on entry
            all_possible_status = {0: 'Unknown', 1: 'Student', 2: 'Staff', 3: 'Both'}
            status = all_possible_status[status_key]

            #Double age
            age = int(age) * 2

            #Append to csv file
            with open('data.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([name, age, status])

            #Clear entries and return cursor to start
            self.name_entry.delete(0, END)
            self.age_entry.delete(0, END)
            self.status_selection.set(0)
            self.name_entry.focus()

        except ValueError:
            self.age_entry.delete(0, END)