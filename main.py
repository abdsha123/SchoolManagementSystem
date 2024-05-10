import tkinter as tk
from tkinter import ttk
import mysql.connector
from PIL import ImageTk, Image
from win32api import GetSystemMetrics
import os
from email.message import EmailMessage


# Hex codes of all the colors used in the project
bg_white = "#FFFFFF"
fg_black = "#3C3C3C"
c_blue = "#57E2FF"
s_green = "#57FF8F"
t_orange = "#FFB157"
r_red = "#F15044"
f_grey = "#F6F6F6"

# Fonts
n_font = ('Hero', 16)
s_font = ('Hero', 13)
big_font = ('Arial', 22)


mydb = None
c = None
run_app = False

class Login(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("700x500")
        self.config(bg=bg_white)
        self.title("LOGIN TO MYSQL")


        top_bar = tk.Frame(self)
        top_bar.config(bg=fg_black)
        top_bar.columnconfigure(3, weight=1)
        msgFrame=tk.Frame(self)
        msgFrame.config(bg=bg_white)
        self.message = tk.Label(msgFrame, text="", bg=bg_white,fg=r_red, font=s_font)

        self.logo = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\smartschool.png"))
        self.login_img = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\loginbtn.png"))
        self.exit_img = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\exitbtn.png"))

        tk.Label(top_bar, image=self.logo, bg=fg_black).pack()
        top_bar.pack(fill=tk.X)
        msgFrame.pack()
        login_frame = tk.Frame(self)
        login_frame.config(bg=bg_white)
        tk.Label(login_frame, text="Login to MySQL", bg=bg_white,fg=fg_black, font=big_font).grid(row=0, column=0, padx=5, pady=20, columnspan=2)
        tk.Label(login_frame, text="Host: ", bg=bg_white, font=s_font).grid(row=1, column=0, padx=5,pady=5,sticky="w")
        tk.Label(login_frame, text="User: ", bg=bg_white, font=s_font).grid(row=2, column=0, padx=5,pady=5,sticky="w")
        tk.Label(login_frame, text="Password: ", bg=bg_white, font=s_font).grid(row=3, column=0, padx=5,pady=5,sticky="w")
        tk.Label(login_frame, text="Database Name: ", bg=bg_white, font=s_font).grid(row=4, column=0, padx=5,pady=5,sticky="w")
        self.e_host = ttk.Entry(login_frame, width=30, font=s_font)
        self.e_host.grid(row=1, column=1, padx=5)
        self.e_user = ttk.Entry(login_frame, width=30, font=s_font)
        self.e_user.grid(row=2, column=1, padx=5)
        self.e_password = ttk.Entry(login_frame, width=30, font=s_font, show="*")
        self.e_password.grid(row=3, column=1, padx=5)
        self.e_db = ttk.Entry(login_frame, width=30, font=s_font)
        self.e_db.grid(row=4, column=1, padx=5)

        self.e_host.insert(tk.END,"localhost")
        self.e_user.insert(tk.END,"root")
        self.e_password.insert(tk.END, "")
        self.e_db.insert(tk.END,"school")

        btn_login = tk.Button(login_frame, image=self.login_img, bg=bg_white, border=0, activebackground=bg_white,
                            command=lambda: self.login())

        btn_exit =tk.Button(login_frame, image=self.exit_img, bg=bg_white, border=0, activebackground=bg_white,
                            command=lambda: self.exit())

        btn_login.grid(row=5,column=0,pady=10)
        btn_exit.grid(row=5,column=1,pady=10)
        login_frame.pack()
        tk.Label(self, text="Please Make sure your Screen Resolution is 1920x1080  and Scale is 100% in your display settings",
                 bg=bg_white, fg=r_red).pack(pady=10)

    def exit(self):
        self.destroy()

    def login(self):
        try:
            global mydb
            mydb = mysql.connector.connect(
                host=self.e_host.get(),
                user=self.e_user.get(),
                password=self.e_password.get(),
                database=self.e_db.get()
            )
            global c
            c = mydb.cursor()
        except:
            self.message.config(text="Unable to Login, Please check login credentials")
            self.message.pack()
            return
        width = GetSystemMetrics(0)
        height = GetSystemMetrics(1)

        if width < 1920 or height < 1080:
            self.message.config(text="Please change Screen Resolution to 1920x1080 or higher, and scale to 100% ")
            self.message.pack()
            return


        global run_app
        run_app = True
        self.destroy()


class SchoolManagementSystem(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("1900x1050")
        self.config(bg=fg_black)
        self.title("Imaginary School management System")

        # importing images used on this screen
        self.logo = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\smartschool2.png"))
        self.back_button = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\backButton.png"))
        self.forward_button = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\forwardBtn.png"))
        self.exit_button = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\exit cross.png"))

        self.message_frame = tk.Frame(self)
        self.message_frame.config(bg=fg_black)
        self.message = tk.Label(self.message_frame, text="", bg=fg_black,font=n_font)

        # Black bar with logo
        top_bar = tk.Frame(self)
        top_bar.config(bg=fg_black)
        top_bar.columnconfigure(3, weight=1)

        # adding logo to top bar
        logo_label = tk.Label(top_bar, image=self.logo, bg=fg_black)
        # adding the top bar to Main window

        btn_back = tk.Button(top_bar, image=self.back_button, bg=fg_black, border=0, activebackground=fg_black,
                             command=lambda: self.previous_screen())

        btn_fwd = tk.Button(top_bar, image=self.forward_button, bg=fg_black, border=0, activebackground=fg_black,
                            command=lambda: self.next_screen())

        btn_exit = tk.Button(top_bar, image=self.exit_button, bg=fg_black, border=0, activebackground=fg_black,
                            command=lambda: self.destroy())

        btn_back.grid(row=0, column=0, padx=40)
        btn_fwd.grid(row=0, column=1, padx=40)
        logo_label.grid(row=0, column=2, padx=450)
        btn_exit.grid(row=0, column=3,padx=20, sticky="e")

        top_bar.pack(fill=tk.X)
        self.message_frame.pack()

        main_frame = tk.Frame(self)
        main_frame.config(bg=bg_white)

        scroll_canvas = tk.Canvas(main_frame)


        scroll_bar= ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=scroll_canvas.yview)
        scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)

        scroll_canvas.configure(yscrollcommand=scroll_bar.set)
        scroll_canvas.bind('<Configure>', lambda e: scroll_canvas.configure(scrollregion=scroll_canvas.bbox("all")))

        main_frame.pack(fill="both",expand=1)


        content_frame = tk.Frame(scroll_canvas,width=1920,height=1080)
        content_frame.config(bg=bg_white)
        content_frame.grid_propagate(0)
        content_frame.pack(fill="both", expand=1,padx=50)
        content_frame.rowconfigure(0, weight=1)
        content_frame.columnconfigure(0, weight=1)

        scroll_canvas.pack(side=tk.LEFT, fill="both", expand=1)
        scroll_canvas.create_window((0, 0), window=content_frame,anchor="nw")

        self.screens = {}

        self.prevscreenstack = []
        self.nextscreenstack = []

        self.currentscreen = HomeScreen

        screenstuple = (HomeScreen, ClassesScreen, StudentScreen, TeacherScreen, ResultScreen,
                        StudentForm, TeacherForm, ExamForm, TeacherSearch, StudentSearch,
                        ClassesInformationScreen, ClassesTimeTable, ClassResultScreen, StudentResultScreen,
                        SubjectTeachers)

        for F in screenstuple:
            frame = F(content_frame, self)
            self.screens[F] = frame
            frame.grid(row=0, column=0, columnspan=2, sticky="nsew")

        self.show_screen(self.currentscreen)

    def show_screen(self, framename):
        self.prevscreenstack.append(self.currentscreen)
        self.nextscreenstack = []
        self.currentscreen = framename
        frame = self.screens[framename]
        frame.tkraise()
        self.show_message("",bg_white)

    def previous_screen(self):
        if len(self.prevscreenstack) > 0:
            self.nextscreenstack.append(self.currentscreen)
            screen = self.prevscreenstack.pop()
            frame = self.screens[screen]
            self.currentscreen = screen
            frame.tkraise()
            self.show_message("", bg_white)

    def next_screen(self):
        if len(self.nextscreenstack) > 0:
            self.prevscreenstack.append(self.currentscreen)
            screen = self.nextscreenstack.pop()
            frame = self.screens[screen]
            self.currentscreen = screen
            frame.tkraise()
            self.show_message("", bg_white)

    def show_message(self, message, color):
        self.message.config(text=message, fg=color)
        self.message.pack()
        self.message_frame.pack()


class HomeScreen(tk.Frame):

    def __init__(self, parent, window):
        tk.Frame.__init__(self, parent)
        self.config(bg=bg_white)

        # importing all images used on this screen
        self.welcome_msg = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\hs_title.png"))
        self.img_classes = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\hs_classes_b.png"))
        self.img_students = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\hs_students_b.png"))
        self.img_teachers = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\hs_teachers_b.png"))
        self.img_results = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\hs_result_b.png"))
      
        
    

        # creating the welcome message
        welcome_label = tk.Label(self, image=self.welcome_msg, bg=bg_white)

        # Home screen Buttons frames
        buttonsFrame = tk.Frame(self)
        buttonsFrame.config(bg=bg_white)

        # creating buttons using images and adding lambda expressions
        btn_classes = tk.Button(buttonsFrame, image=self.img_classes, bg=bg_white, border=0, activebackground=bg_white,
                                command=lambda: window.show_screen(ClassesScreen))

        btn_students = tk.Button(buttonsFrame, image=self.img_students, bg=bg_white, border=0,
                                 activebackground=bg_white,
                                 command=lambda: window.show_screen(StudentScreen))

        btn_teachers = tk.Button(buttonsFrame, image=self.img_teachers, bg=bg_white, border=0,
                                 activebackground=bg_white,
                                 command=lambda: window.show_screen(TeacherScreen))

        btn_results = tk.Button(buttonsFrame, image=self.img_results, bg=bg_white, border=0, activebackground=bg_white,
                                command=lambda: window.show_screen(ResultScreen))

        # adding the button in horizontal grid
        btn_classes.grid(row=1, column=0, padx=10)
        btn_students.grid(row=1, column=1, padx=10)
        btn_teachers.grid(row=1, column=2, padx=10)
        btn_results.grid(row=1, column=3, padx=10)
        

        # Adding everything to the Home screen
        welcome_label.pack(pady=75)
        buttonsFrame.pack(pady=75)


class ClassesScreen(tk.Frame):

    def __init__(self, parent, window):
        tk.Frame.__init__(self, parent)
        self.config(bg=bg_white)

        # opening all the images
        self.title_image = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\cs_title.png"))
        self.img_classinfo = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\cs_classinfo.png"))
        self.img_timetable = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\cs_timetable.png"))
        self.img_results = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\cs_result.png"))
        self.img_addclass = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\cs_addclass.png"))

        titlelabel = tk.Label(self, image=self.title_image, bg=bg_white)

        # classes screen Buttons frames
        buttonsFrame = tk.Frame(self)
        buttonsFrame.config(bg=bg_white)

        btn_classinfo = tk.Button(buttonsFrame, image=self.img_classinfo, bg=bg_white, border=0,
                                  activebackground=bg_white,
                                  command=lambda: window.show_screen(ClassesInformationScreen))
        btn_timetable = tk.Button(buttonsFrame, image=self.img_timetable, bg=bg_white, border=0,
                                  activebackground=bg_white,
                                  command=lambda: window.show_screen(ClassesTimeTable))
        btn_results = tk.Button(buttonsFrame, image=self.img_results, bg=bg_white, border=0, activebackground=bg_white,
                                command=lambda: window.show_screen(ClassResultScreen))

        # adding the button in horizoltal grid
        btn_classinfo.grid(row=1, column=0, padx=10)
        btn_timetable.grid(row=1, column=1, padx=10)
        btn_results.grid(row=1, column=2, padx=10)

        # adding the bar and buttons to the screen
        titlelabel.pack(pady=65, fill="x")
        buttonsFrame.pack(pady=75)


class ClassesInformationScreen(tk.Frame):

    def __init__(self, parent, window):
        tk.Frame.__init__(self, parent)
        self.config(bg=bg_white)
        self.search_btn = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\c_searchbtn.png"))
        self.result_frame = tk.Frame(self)
        self.result_frame.config(bg=bg_white)
        class_frame = tk.Frame(self)
        class_frame.config(bg=bg_white)
        # opening all the images
        self.title_image = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\ci_title.png"))

        tk.Label(self, image=self.title_image, bg=bg_white).pack(pady=(50, 20))
        classLabel = tk.Label(class_frame, text="Select Class :", bg=bg_white, font=n_font)

        c.execute("SELECT * from class_view ")
        class_list = []
        for E in c.fetchall():
            class_list.append(E[0])

        v_class = tk.StringVar()
        d_class = ttk.OptionMenu(class_frame, v_class, class_list[0], *class_list)
        d_class.config(width=75)

        btn_search = tk.Button(class_frame, image=self.search_btn, bg=bg_white, border=0,
                               activebackground=bg_white,
                               command=lambda: self.searchClass(v_class.get()))

        classLabel.grid(row=0, column=0, padx=10)
        d_class.grid(row=0, column=1, padx=10, ipady=10)
        btn_search.grid(row=0, column=2, padx=10, pady=3)

        class_frame.pack()

    def searchClass(self, class_id):


        c.execute("""SELECT count(rollNum) 
                                FROM student
                                WHERE classID = \"{}\"""".format(class_id))


        for widget in self.result_frame.winfo_children():
            widget.destroy()

        tempFrame = tk.Frame(self.result_frame)
        tempFrame.config(bg=bg_white)

        ctLabel = tk.Label(tempFrame, text="Class Teacher :", bg=bg_white, font=n_font)
        strengthLabel = tk.Label(tempFrame, text="Class Strength :", bg=bg_white, font=n_font)
        subjectLabel = tk.Label(tempFrame, text="Students List", fg=c_blue, bg=bg_white, font=big_font)

        strength = c.fetchone()[0]
        strengthDisplay = tk.Label(tempFrame, text=strength, bg=bg_white, font=n_font)

        c.execute("""
            SELECT CONCAT(fname ,' ', lname) as ClassTeacher
            FROM class JOIN teacher ON class.ClassTeacher = teacher.teacherID
            WHERE classID = \"{}\"
            """.format(class_id))

        classTeacher = c.fetchone()[0]
        classTeacherDisplay = tk.Label(tempFrame, text=classTeacher, bg=bg_white, font=n_font)

        strengthLabel.grid(row=0, column=0, sticky="w")
        strengthDisplay.grid(row=0, column=1, sticky="w")
        ctLabel.grid(row=0, column=2, sticky="w")
        classTeacherDisplay.grid(row=0, column=3, sticky="w")
        subjectLabel.grid(row=2, column=0, sticky="w", pady=(20, 0))

        query = """SELECT rollNum,concat(fname,' ',lname),dob,address,fatherName,contactNum,email,classID 
                FROM student WHERE classID = \"{}\" """.format(
            class_id)
        c.execute(query)
        att = ("Roll No", "First Name", "DOB", "Address", "Father's Name",
               "Contact No.", "Email", "Class")
        ct = CustomTable(tempFrame, att, c.fetchall(), c_blue)
        ct.grid(row=3, column=0, columnspan=8)
        tempFrame.pack()
        self.result_frame.pack()


class ClassesTimeTable(tk.Frame):
    def __init__(self, parent, window):
        tk.Frame.__init__(self, parent)
        self.config(bg=bg_white)
        self.search_button = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\c_searchbtn.png"))
        class_frame = tk.Frame(self)
        class_frame.config(bg=bg_white)
        # opening all the images
        self.title_image = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\ct_title.png"))
        tk.Label(self, image=self.title_image, bg=bg_white).pack(pady=15)
        classLabel = tk.Label(class_frame, text="Select Class :", bg=bg_white, font=n_font)

        self.tt_frame = tk.Frame(self)
        c.execute("SELECT * FROM class_view ")
        class_list = []
        for E in c.fetchall():
            class_list.append(E[0])

        v_class = tk.StringVar()
        d_class = ttk.OptionMenu(class_frame, v_class, class_list[0], *class_list)
        d_class.config(width=75)

        btn_search = tk.Button(class_frame, image=self.search_button, bg=bg_white, border=0,
                               activebackground=bg_white,
                               command=lambda: self.searchClass(v_class.get()))
        classLabel.grid(row=0, column=0, padx=10)
        d_class.grid(row=0, column=1, padx=10, ipady=10)
        btn_search.grid(row=0, column=2, padx=10, pady=3)

        class_frame.pack()

    def searchClass(self, classID):
        for widget in self.tt_frame.winfo_children():
            widget.destroy()
        self.tt_frame.config(bg=bg_white)
        titles = ("Subject", "Room No")
        days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
        daily_tables_list = []

        periods_list_frame = tk.Frame(self.tt_frame)
        periods_list_frame.config(bg=bg_white)
        period_list = []

        tk.Label(periods_list_frame, text="Period", bg=bg_white, font=n_font).grid(row=0, column=0, pady=10)

        for i in range(1, 7):
            period_list.append(tk.Label(periods_list_frame, text=i, bg=bg_white, font=n_font))
            period_list[i - 1].grid(row=i, column=0, ipadx=15)

        periods_list_frame.grid(row=1, column=0)

        for day in days:
            c.execute("""SELECT S.title,roomNum
                    FROM meeting AS M JOIN class AS C ON M.classID = C.classID
                    JOIN subjects AS S ON S.subjectID = M.subjectID
                    WHERE C.classID = \"{}\" AND M.dayOfWeek = \"{}\" ORDER BY period""".format(classID, day))

            daily_tables_list.append(CustomTable(self.tt_frame, titles, c.fetchall(), c_blue))

        for i, column in enumerate(daily_tables_list):
            tk.Label(self.tt_frame, text=days[i], bg=bg_white, font=n_font).grid(row=0, column=i + 1, padx=2,
                                                                                 sticky="ns")
            column.grid(row=1, column=i + 1, padx=2, sticky="n")
        self.tt_frame.pack(pady=25)


class StudentScreen(tk.Frame):

    def __init__(self, parent, window):
        tk.Frame.__init__(self, parent)
        self.config(bg=bg_white)
        # opening all the images
        self.title_image = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\ss_title.png"))
        self.img_studentinfo = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\ss_studentinfo.png"))
        self.img_results = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\ss_studentresult.png"))
        self.img_addstudent = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\ss_addstudent.png"))

        # adding the title to the frame
        tk.Label(self, image=self.title_image, bg=bg_white).pack(pady=65, fill="x")

        # classes screen Buttons frames
        buttonsFrame = tk.Frame(self)
        buttonsFrame.config(bg=bg_white)

        btn_student_info = tk.Button(buttonsFrame, image=self.img_studentinfo, bg=bg_white, border=0,
                                     activebackground=bg_white, command=lambda: window.show_screen(StudentSearch))
        btn_results = tk.Button(buttonsFrame, image=self.img_results, bg=bg_white, border=0,
                                activebackground=bg_white, command=lambda: window.show_screen(StudentResultScreen))
        btn_addstudent = tk.Button(buttonsFrame, image=self.img_addstudent, bg=bg_white, border=0,
                                   activebackground=bg_white, command=lambda: window.show_screen(StudentForm))

        # adding the button in horizoltal grid
        btn_student_info.grid(row=1, column=0, padx=10)
        btn_results.grid(row=1, column=1, padx=10)
        btn_addstudent.grid(row=1, column=2, padx=10)

        # adding the bar and buttons to the screen
        buttonsFrame.pack(pady=75)


class StudentForm(tk.Frame):

    def __init__(self, parent, window):
        tk.Frame.__init__(self, parent)
        self.config(bg=bg_white)
        self.window = window

        # opening all the images
        self.title_image = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\sf_title.png"))
        self.img_add = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\sf_addbtn.png"))
        self.img_cancel = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\sf_cancelbtn.png"))

        # adding the title image to the frame
        tk.Label(self, image=self.title_image, bg=bg_white).pack(pady=65, fill="x")

        # classes screen Buttons frames
        buttonsFrame = tk.Frame(self)
        buttonsFrame.config(bg=bg_white)

        c.execute("SELECT * FROM class_view ")
        class_list = []
        for E in c.fetchall():
            class_list.append(E[0])

        form = tk.Frame(self)
        form.config(bg=bg_white)
        l_reg_no = tk.Label(form, text="Registration Number :", bg=bg_white, font=n_font)
        l_reg_no.grid(row=0, column=0, ipadx=10, pady=10, sticky="W")
        l_first_name = tk.Label(form, text="First Name :", bg=bg_white, font=n_font)
        l_first_name.grid(row=1, column=0, ipadx=10, pady=10, sticky="W")
        l_last_name = tk.Label(form, text="Last Name :", bg=bg_white, font=n_font)
        l_last_name.grid(row=2, column=0, ipadx=10, pady=10, sticky="W")
        l_dob = tk.Label(form, text="Date Of Birth :", bg=bg_white, font=n_font)
        l_dob.grid(row=3, column=0, ipadx=10, pady=10, sticky="W")
        l_address = tk.Label(form, text="Address :", bg=bg_white, font=n_font)
        l_address.grid(row=4, column=0, ipadx=10, pady=10, sticky="W")
        l_father_name = tk.Label(form, text="Father Name :", bg=bg_white, font=n_font)
        l_father_name.grid(row=5, column=0, ipadx=10, pady=10, sticky="W")
        l_contact_no = tk.Label(form, text="Contact Number :", bg=bg_white, font=n_font)
        l_contact_no.grid(row=6, column=0, ipadx=10, pady=10, sticky="W")
        l_email = tk.Label(form, text="Email :", bg=bg_white, font=n_font)
        l_email.grid(row=7, column=0, ipadx=10, pady=10, sticky="W")
        l_class = tk.Label(form, text="Class :", bg=bg_white, font=n_font)
        l_class.grid(row=9, column=0, ipadx=10, pady=10, sticky="W")

        self.e_reg_no = ttk.Entry(form, width=30, font=n_font)
        self.e_reg_no.grid(row=0, column=1, padx=5, ipadx=5)
        self.e_first_name = ttk.Entry(form, width=30, font=n_font)
        self.e_first_name.grid(row=1, column=1, padx=5, ipadx=5)
        self.e_last_name = ttk.Entry(form, width=30, font=n_font)
        self.e_last_name.grid(row=2, column=1, padx=5, ipadx=5)

        frame_date = tk.Frame(form)
        frame_date.config(bg=bg_white)
        self.e_dd = ttk.Entry(frame_date, width=10, font=n_font)
        self.e_mm = ttk.Entry(frame_date, width=10, font=n_font)
        self.e_yy = ttk.Entry(frame_date, width=10, font=n_font)

        self.e_dd.insert(tk.END, 'dd')
        self.e_mm.insert(tk.END, 'mm')
        self.e_yy.insert(tk.END, 'yyyy')

        self.e_dd.grid(row=0, column=0)
        self.e_mm.grid(row=0, column=1)
        self.e_yy.grid(row=0, column=2)

        frame_date.grid(row=3, column=1, padx=5)
        self.e_address = ttk.Entry(form, width=30, font=n_font)
        self.e_address.grid(row=4, column=1, padx=5, ipadx=5)
        self.e_father_name = ttk.Entry(form, width=30, font=n_font)
        self.e_father_name.grid(row=5, column=1, padx=5, ipadx=5)
        self.e_contact_no = ttk.Entry(form, width=30, font=n_font)
        self.e_contact_no.grid(row=6, column=1, padx=5, ipadx=5)
        self.e_email = ttk.Entry(form, width=30, font=n_font)
        self.e_email.grid(row=7, column=1, padx=5, ipadx=5)

        self.v_class = tk.StringVar()
        self.d_class = ttk.OptionMenu(form, self.v_class, class_list[0], *class_list)
        self.d_class.config(width=52)
        self.d_class.grid(row=9, column=1, ipady=3)

        btn_add = tk.Button(buttonsFrame, image=self.img_add, bg=bg_white, border=0, activebackground=bg_white
                            , command=lambda: addStudent())
        btn_cancel = tk.Button(buttonsFrame, image=self.img_cancel, bg=bg_white, border=0, activebackground=bg_white,
                               command=lambda: window.previous_screen())

        # adding the button in horizoltal grid
        btn_add.grid(row=1, column=0, padx=10)
        btn_cancel.grid(row=1, column=1, padx=10)

        # adding the bar and buttons to the screen
        form.pack()
        buttonsFrame.pack(pady=50)

        def addStudent():
            dob = "{}-{}-{}".format(self.e_yy.get(), self.e_mm.get(), self.e_dd.get())
            query = "INSERT INTO student VALUES(\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\")".format(
                self.e_reg_no.get(),
                self.e_first_name.get(),
                self.e_last_name.get(),
                dob,
                self.e_address.get(),
                self.e_father_name.get(),
                self.e_contact_no.get(),
                self.e_email.get(),
                self.v_class.get()

            )

            try:
                c.execute(query)
                self.window.show_message("Data Added sucessfully", s_green)
            except:
                self.window.show_message("Can not continue, The data entered is incorrect", r_red)
                return

            self.e_reg_no.delete(0, tk.END)
            self.e_first_name.delete(0, tk.END)
            self.e_last_name.delete(0, tk.END)
            self.e_address.delete(0, tk.END)
            self.e_father_name.delete(0, tk.END)
            self.e_contact_no.delete(0, tk.END)
            self.e_email.delete(0, tk.END)

            mydb.commit()


class StudentSearch(tk.Frame):

    def __init__(self, parent, window):
        tk.Frame.__init__(self, parent)
        self.config(bg=bg_white)
        self.window = window
        # opening all the images
        self.title_image = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\sss_title.png"))
        self.img_searchid = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\sss_searchregnobtn.png"))

        form = tk.Frame(self)
        form.config(bg=bg_white)

        titlelabel = tk.Label(self, image=self.title_image, bg=bg_white)

        btn_id = tk.Button(form, image=self.img_searchid, bg=bg_white, border=0, activebackground=bg_white,
                           command=lambda: search())

        ssr_table = tk.Frame(self, bg=bg_white)

        l_id = tk.Label(form, text="Roll Number :", bg=bg_white, font=n_font)
        l_id.grid(row=0, column=0, ipadx=10, pady=10, sticky="W")

        e_regNum = tk.Entry(form, width=50, border=0, bg=f_grey, font=n_font, bd=0)
        e_regNum.grid(row=0, column=1, padx=5, ipadx=5, ipady=3)

        btn_id.grid(row=1, column=1, padx=0, pady=20)

        # adding the bar and buttons to the screen
        titlelabel.pack(pady=65, fill="x")
        form.pack()
        ssr_table.pack()

        def search():
            query = "SELECT rollNum,concat(fname,' ',lname),dob,address,fatherName,contactNum,email,classID FROM student WHERE rollNum = {}".format(
                e_regNum.get())
            try:
                c.execute(query)
                self.window.show_message("", bg_white)
            except:
                self.window.show_message("Can not search, Invalid Roll Number", r_red)
                return

            q_result = c.fetchall()

            if len(q_result) == 0:
                self.window.show_message("Student Not Found, make sure Roll Number is correct", r_red)
                return

            for widget in ssr_table.winfo_children():
                widget.destroy()

            att = ("Roll No", "First Name", "DOB", "Address", "Father's Name",
                   "Contact No.", "Email", "Class")
            ct = CustomTable(ssr_table, att, q_result, s_green)
            ct.pack()


class StudentSearchResults(tk.Frame):

    def __init__(self, parent, window):
        tk.Frame.__init__(self, parent)
        self.config(bg=bg_white)

        # opening all the images
        self.title_image = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\ssr_title.png"))

        titlelabel = tk.Label(self, image=self.title_image, bg=bg_white)

        ssr_table = tk.Frame(self, bg=bg_white)
        # adding the bar and buttons to the screen
        titlelabel.pack(pady=65, fill="x")
        ssr_table.pack()


class TeacherScreen(tk.Frame):

    def __init__(self, parent, window):
        tk.Frame.__init__(self, parent)
        self.config(bg=bg_white)

        # opening all the images
        self.title_image = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\ts_title.png"))
        self.img_teacherinfo = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\ts_teacherinfo.png"))
        self.img_subject = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\ts_subjectteachers.png"))
        self.img_addteacher = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\ts_addteacher.png"))

        titlelabel = tk.Label(self, image=self.title_image, bg=bg_white)

        # classes screen Buttons frames
        buttonsFrame = tk.Frame(self)
        buttonsFrame.config(bg=bg_white)

        btn_teacherinfo = tk.Button(buttonsFrame, image=self.img_teacherinfo, bg=bg_white, border=0,
                                    activebackground=bg_white,
                                    command=lambda: window.show_screen(TeacherSearch))
        btn_subject = tk.Button(buttonsFrame, image=self.img_subject, bg=bg_white, border=0, activebackground=bg_white,
                                command=lambda: window.show_screen(SubjectTeachers))

        btn_addteacher = tk.Button(buttonsFrame, image=self.img_addteacher, bg=bg_white, border=0,
                                   activebackground=bg_white,
                                   command=lambda: window.show_screen(TeacherForm))

        # adding the button in horizoltal grid
        btn_teacherinfo.grid(row=1, column=0, padx=10)
        btn_subject.grid(row=1, column=1, padx=10)
        btn_addteacher.grid(row=1, column=2, padx=10)

        # adding the bar and buttons to the screen
        titlelabel.pack(pady=65, fill="x")
        buttonsFrame.pack(pady=75)


class TeacherForm(tk.Frame):

    def __init__(self, parent, window):
        tk.Frame.__init__(self, parent)
        self.config(bg=bg_white)
        self.window = window

        # opening all the images
        self.title_image = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\tf_title.png"))
        self.img_add = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\tf_add.png"))
        self.img_cancel = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\tf_cancel.png"))

        titlelabel = tk.Label(self, image=self.title_image, bg=bg_white)

        # classes screen Buttons frames
        buttonsFrame = tk.Frame(self)
        buttonsFrame.config(bg=bg_white)

        btn_add = tk.Button(buttonsFrame, image=self.img_add, bg=bg_white, border=0, activebackground=bg_white,
                            command=lambda: addTeacher())
        btn_cancel = tk.Button(buttonsFrame, image=self.img_cancel, bg=bg_white, border=0, activebackground=bg_white,
                               command=lambda: window.previous_screen())

        form = tk.Frame(self)
        form.config(bg=bg_white)
        l_teacher_id = tk.Label(form, text="Teacher ID :", bg=bg_white, font=n_font)
        l_teacher_id.grid(row=0, column=0, ipadx=10, pady=10, sticky="W")
        l_first_name = tk.Label(form, text="First Name :", bg=bg_white, font=n_font)
        l_first_name.grid(row=1, column=0, ipadx=10, pady=10, sticky="W")
        l_last_name = tk.Label(form, text="Last Name :", bg=bg_white, font=n_font)
        l_last_name.grid(row=2, column=0, ipadx=10, pady=10, sticky="W")
        l_qualification = tk.Label(form, text="Qualification :", bg=bg_white, font=n_font)
        l_qualification.grid(row=3, column=0, ipadx=10, pady=10, sticky="W")
        l_address = tk.Label(form, text="address :", bg=bg_white, font=n_font)
        l_address.grid(row=4, column=0, ipadx=10, pady=10, sticky="W")
        l_contact_no = tk.Label(form, text="Contact Number :", bg=bg_white, font=n_font)
        l_contact_no.grid(row=6, column=0, ipadx=10, pady=10, sticky="W")
        l_email = tk.Label(form, text="Email :", bg=bg_white, font=n_font)
        l_email.grid(row=7, column=0, ipadx=10, pady=10, sticky="W")

        self.e_teacher_id = ttk.Entry(form, width=30, font=n_font)
        self.e_teacher_id.grid(row=0, column=1, padx=5, ipadx=5, ipady=3)
        self.e_first_name = ttk.Entry(form, width=30, font=n_font)
        self.e_first_name.grid(row=1, column=1, padx=5, ipadx=5, ipady=3)
        self.e_last_name = ttk.Entry(form, width=30, font=n_font)
        self.e_last_name.grid(row=2, column=1, padx=5, ipadx=5, ipady=3)
        self.e_qualification = ttk.Entry(form, width=30, font=n_font)
        self.e_qualification.grid(row=3, column=1, padx=5, ipadx=5, ipady=3)
        self.e_address = ttk.Entry(form, width=30, font=n_font)
        self.e_address.grid(row=4, column=1, padx=5, ipadx=5, ipady=3)
        self.e_contact_no = ttk.Entry(form, width=30, font=n_font)
        self.e_contact_no.grid(row=6, column=1, padx=5, ipadx=5, ipady=3)
        self.e_email = ttk.Entry(form, width=30, font=n_font)
        self.e_email.grid(row=7, column=1, padx=5, ipadx=5, ipady=3)

        # adding the button in horizoltal grid
        btn_add.grid(row=1, column=0, padx=10)
        btn_cancel.grid(row=1, column=1, padx=10)

        # adding the bar and buttons to the screen
        titlelabel.pack(pady=65, fill="x")
        form.pack()
        buttonsFrame.pack(pady=50)

        def addTeacher():
            query = "INSERT INTO teacher VALUES(\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\")".format(
                self.e_teacher_id.get(),
                self.e_first_name.get(),
                self.e_last_name.get(),
                self.e_address.get(),
                self.e_contact_no.get(),
                self.e_email.get(),
                self.e_qualification.get())

            try:
                c.execute(query)
                self.window.show_message("Data Added sucessfully", s_green)
            except:
                self.window.show_message("Can not continue, The data entered is incorrect", r_red)
                return

            self.e_teacher_id.delete(0, tk.END)
            self.e_first_name.delete(0, tk.END)
            self.e_last_name.delete(0, tk.END)
            self.e_qualification.delete(0, tk.END)
            self.e_address.delete(0, tk.END)
            self.e_contact_no.delete(0, tk.END)
            self.e_email.delete(0, tk.END)

            mydb.commit()


class TeacherSearch(tk.Frame):

    def __init__(self, parent, window):
        tk.Frame.__init__(self, parent)
        self.config(bg=bg_white)
        self.window = window

        # opening all the images
        self.title_image = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\tss_title.png"))
        self.img_searchname = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\tss_searchnamebtn.png"))
        self.img_searchid = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\tss_searchidbtn.png"))

        titlelabel = tk.Label(self, image=self.title_image, bg=bg_white)

        form = tk.Frame(self, bg=bg_white)

        tsr_table = tk.Frame(self)
        tsr_table.config(bg=bg_white)

        btn_id = tk.Button(form, image=self.img_searchid, bg=bg_white, border=0, activebackground=bg_white,
                           command=lambda: search())

        l_id = tk.Label(form, text="Teacher Id :", bg=bg_white, font=n_font)
        l_id.grid(row=4, column=0, ipadx=10, pady=10, sticky="W")

        e_id = tk.Entry(form, width=50, border=0, bg=f_grey, font=n_font, bd=0)
        e_id.grid(row=5, column=0, padx=5, ipadx=5, ipady=3)

        btn_id.grid(row=6, column=0, padx=5, pady=10)

        # adding the bar and buttons to the screen
        titlelabel.pack(pady=65, fill="x")
        form.pack()
        tsr_table.pack()

        def search():
            query = "SELECT * FROM teacher WHERE teacherID = {}".format(e_id.get())
            try:
                c.execute(query)
                self.window.show_message("", bg_white)
            except:
                self.window.show_message("Can not search, invalid ID", r_red)
                return

            q_result =c.fetchall()
            if len(q_result) == 0:
                self.window.show_message("Teacher not found, make sure ID is correct", r_red)
                return

            for widget in tsr_table.winfo_children():
                widget.destroy()

            att = ("Teacher ID", "First Name", "Last Name", "Address", "Contact", "Email", "Qualification")
            ct = CustomTable(tsr_table, att, q_result, t_orange)
            ct.pack()


class SubjectTeachers(tk.Frame):

    def __init__(self, parent, window):
        tk.Frame.__init__(self, parent)
        self.config(bg=bg_white)
        self.window = window
        # opening all the images
        self.title_image = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\st_title.png"))
        self.img_searchbtn = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\t_searchBtn.png"))
        self.info_frame = tk.Frame(self)
        self.info_frame.config(bg=bg_white)
        searchbar = tk.Frame(self)
        searchbar.config(bg=bg_white)
        titlelabel = tk.Label(self, image=self.title_image, bg=bg_white)
        classLabel = tk.Label(searchbar, text="Select Class :", bg=bg_white, font=n_font)

        c.execute("SELECT * FROM class_view ")
        class_list = []
        for E in c.fetchall():
            class_list.append(E[0])

        v_class = tk.StringVar()
        d_class = ttk.OptionMenu(searchbar, v_class, class_list[0], *class_list)
        d_class.config(width=75)

        btn_search = tk.Button(searchbar, image=self.img_searchbtn, bg=bg_white, border=0,
                               activebackground=bg_white,
                               command=lambda: self.search(v_class.get()))

        titlelabel.pack(pady=(50, 20))
        classLabel.grid(row=0, column=0, padx=10)
        d_class.grid(row=0, column=1, padx=10, ipady=10)
        btn_search.grid(row=0, column=2, padx=10)
        searchbar.pack()

    def search(self, class_id):
        query = """SELECT T.teacherID, concat(T.fname,' ',T.lname), S.title
                    FROM teaches JOIN subjects AS S ON teaches.subjectID = S.subjectID
                    JOIN teacher AS T ON teaches.teacherID = T.teacherID 
                    WHERE classID = \"{}\"""".format(class_id)

        c.execute(query)


        for widget in self.info_frame.winfo_children():
            widget.destroy()

        tk.Label(self.info_frame, text=class_id + " Subject Teachers", fg=t_orange, bg=bg_white, font=big_font).pack()
        ct = CustomTable(self.info_frame, ("Teacher ID", "Name", "Subject"), c.fetchall(), t_orange)
        ct.pack()
        self.info_frame.pack()


class ResultScreen(tk.Frame):

    def __init__(self, parent, window):
        tk.Frame.__init__(self, parent)
        self.config(bg=bg_white)

        # opening all the images
        self.title_image = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\rs_title.png"))
        self.img_student = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\rs_student.png"))
        self.img_class = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\rs_class.png"))
        self.img_add = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\rs_add.png"))

        titlelabel = tk.Label(self, image=self.title_image, bg=bg_white)

        # classes screen Buttons frames
        buttonsFrame = tk.Frame(self)
        buttonsFrame.config(bg=bg_white)

        btn_student = tk.Button(buttonsFrame, image=self.img_student, bg=bg_white, border=0, activebackground=bg_white,
                                command=lambda: window.show_screen(StudentResultScreen))
        btn_class = tk.Button(buttonsFrame, image=self.img_class, bg=bg_white, border=0, activebackground=bg_white,
                              command=lambda: window.show_screen(ClassResultScreen))
        btn_add = tk.Button(buttonsFrame, image=self.img_add, bg=bg_white, border=0, activebackground=bg_white,
                            command=lambda: window.show_screen(ExamForm))

        # adding the button in horizoltal grid
        btn_student.grid(row=1, column=0, padx=10)
        btn_class.grid(row=1, column=1, padx=10)
        btn_add.grid(row=1, column=3, padx=10)

        # adding the bar and buttons to the screen
        titlelabel.pack(pady=65, fill="x")
        buttonsFrame.pack(pady=75)


class ClassResultScreen(tk.Frame):

    def __init__(self, parent, window):
        tk.Frame.__init__(self, parent)
        self.config(bg=bg_white)
        self.window = window
        self.infoFrame = tk.Frame(self)
        self.infoFrame.config(bg=bg_white)
        # opening all the images
        self.title_image = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\cr_title.png"))
        self.searchbtn = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\cr_searchBtn.png"))
        self.continuebtn = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\c_backbtn.png"))

        titlelabel = tk.Label(self, image=self.title_image, bg=bg_white)
        titlelabel.pack(pady=20, fill="x")
        self.search_screen()

    def search_screen(self):
        for widget in self.infoFrame.winfo_children():
            widget.destroy()

        classLabel = tk.Label(self.infoFrame, text="Select Class :", bg=bg_white, font=n_font)
        subjectLabel = tk.Label(self.infoFrame, text="Select Subject :", bg=bg_white, font=n_font)

        ExamLabel = tk.Label(self.infoFrame, text="Select Exam :", bg=bg_white, font=n_font)

        ExamList = []
        c.execute(""" SELECT * FROM results_view """)

        for E in c.fetchall():
            ExamList.append(E[0])

        v_exam = tk.StringVar()
        d_exam = ttk.OptionMenu(self.infoFrame, v_exam, ExamList[0], *ExamList)
        d_exam.config(width=50)

        c.execute("SELECT * FROM class_view ")
        class_list = []
        for E in c.fetchall():
            class_list.append(E[0])

        v_class = tk.StringVar()
        d_class = ttk.OptionMenu(self.infoFrame, v_class, class_list[0], *class_list)
        d_class.config(width=50)

        c.execute("SELECT * FROM subjects_view")
        subject_list = []
        subject_dic = {}
        for E in c.fetchall():
            subject_list.append(E[1])
            subject_dic[E[1]] = E[0]
        v_subject = tk.StringVar()
        d_subject = ttk.OptionMenu(self.infoFrame, v_subject, subject_list[0], *subject_list)
        d_subject.config(width=50)

        btn_search = tk.Button(self.infoFrame, image=self.searchbtn, bg=bg_white, border=0,
                               activebackground=bg_white,
                               command=lambda: self.search_results(v_class.get(), v_subject.get(),
                                                                subject_dic[v_subject.get()], v_exam.get()))

        classLabel.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        subjectLabel.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        d_class.grid(row=0, column=1, padx=5, pady=10, ipady=5, sticky="w")
        d_subject.grid(row=1, column=1, padx=5, pady=10, ipady=5, sticky="w")
        ExamLabel.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        d_exam.grid(row=2, column=1, padx=5, pady=10, ipady=5, sticky="w")
        btn_search.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky="we")
        self.infoFrame.pack(pady=20)


    def search_results(self, class_id, subject_title, subject_id, exam):


        examTitle = exam.split(" | ")[0]
        examyear = exam.split(" | ")[1]

        exam_title = tk.Label(self.infoFrame, text="CLASS " + class_id + " " + subject_title + " " + exam, fg=r_red,
                              bg=bg_white, font=big_font)
        exam_title.grid(row=0, column=0)

        query = """SELECT S.rollNum,concat(fname,' ', lname), R.maxMarks,R.obtainedMarks
                    From student AS S JOIN result AS R ON S.rollNum = R.rollNum 
                    Where S.classID = \"{}\" AND examTitle = \"{}\" AND academicYear = {} 
                    AND subjectID = {}""".format(class_id, examTitle, examyear, subject_id)

        c.execute(query)

        for widget in self.infoFrame.winfo_children():
            widget.destroy()

        btn_search = tk.Button(self.infoFrame, image=self.continuebtn, bg=bg_white, border=0,
                               activebackground=bg_white,
                               command=lambda: self.search_screen())

        heading = tk.Label(self.infoFrame, text=class_id +" "+subject_title+ " Result " + exam, fg=r_red, bg=bg_white, font=big_font)
        heading.grid(row=0, column=0,pady=25)
        ct = CustomTable(self.infoFrame, ("Roll No", "Name", "Max Marks", "Obtained Marks"), c.fetchall(), r_red)
        ct.grid(row=1, column=0, sticky="we")
        btn_search.grid(row=2, column=0, pady=50)

            


class StudentResultScreen(tk.Frame):

    def __init__(self, parent, window):
        tk.Frame.__init__(self, parent)
        self.config(bg=bg_white)
        self.window = window
        self.infoFrame = tk.Frame(self)
        self.infoFrame.config(bg=bg_white)

        # opening all the images
        self.title_image = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\sr_title.png"))
        self.searchbtn = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\r_searchbtn.png"))

        titlelabel = tk.Label(self, image=self.title_image, bg=bg_white)
        titlelabel.pack(pady=50)
        searchbarFrame = tk.Frame(self)
        searchbarFrame.config(bg=bg_white)
        RollNoLabel = tk.Label(searchbarFrame, text="Enter RollNumber :", bg=bg_white, font=n_font)
        ExamLabel = tk.Label(searchbarFrame, text="Select Exam :", bg=bg_white, font=n_font)

        ExamList = []
        c.execute(""" SELECT * FROM results_view """)

        for E in c.fetchall():
            ExamList.append(E[0])

        v_exam = tk.StringVar()
        d_exam = ttk.OptionMenu(searchbarFrame, v_exam, ExamList[0], *ExamList)
        d_exam.config(width=75)

        e_rollno = ttk.Entry(searchbarFrame, width=40, font=n_font)

        btn_search = tk.Button(searchbarFrame, image=self.searchbtn, bg=bg_white, border=0,
                               activebackground=bg_white,
                               command=lambda: self.searchResult(e_rollno.get(), v_exam.get()))

        RollNoLabel.grid(row=1, column=0, padx=10, sticky="w")
        e_rollno.grid(row=1, column=1, padx=10, ipady=5, sticky="we")
        btn_search.grid(row=1, column=2, padx=10, pady=3, sticky="w")
        ExamLabel.grid(row=0, column=0, padx=10, sticky="w")
        d_exam.grid(row=0, column=1, padx=10, ipady=5, sticky="w")

        searchbarFrame.pack()

    def searchResult(self, rollNo, exam):
        title = exam.split(" | ")[0]
        year = exam.split(" | ")[1]

        try:
            c.execute("""SELECT rollNum,concat(fname,' ', lname), ClassID 
                                From Student Where rollNum = {}""".format(rollNo))
            self.window.show_message("", bg_white)
        except:
            self.window.show_message("Can not search, Invalid Roll Number", r_red)
            return
        q_result = c.fetchone()
        if q_result is None:
            self.window.show_message("Student Not Found, make sure Roll Number is correct", r_red)
            return

        for widget in self.infoFrame.winfo_children():
            widget.destroy()
        student = q_result

        heading = tk.Label(self.infoFrame, text=exam + " RESULT", fg=r_red, bg=bg_white, font=big_font)
        heading.grid(row=0, column=0, padx=10, pady=10, sticky="we", columnspan=3)

        rollNoLabel = tk.Label(self.infoFrame, text="Roll No :", bg=bg_white, font=n_font)
        nameLabel = tk.Label(self.infoFrame, text="Name :", bg=bg_white, font=n_font)
        classLabel = tk.Label(self.infoFrame, text="Class :", bg=bg_white, font=n_font)

        d_rollNoLabel = tk.Label(self.infoFrame, text=student[0], bg=bg_white, font=n_font)
        d_nameLabel = tk.Label(self.infoFrame, text=student[1], bg=bg_white, font=n_font)
        d_classLabel = tk.Label(self.infoFrame, text=student[2], bg=bg_white, font=n_font)

        rollNoLabel.grid(row=1, column=0, padx=10, sticky="w")
        nameLabel.grid(row=2, column=0, padx=10, sticky="w")
        classLabel.grid(row=3, column=0, padx=10, sticky="w")

        d_rollNoLabel.grid(row=1, column=1, padx=10, sticky="w")
        d_nameLabel.grid(row=2, column=1, padx=10, sticky="w")
        d_classLabel.grid(row=3, column=1, padx=10, sticky="w")


        c.execute("""SELECT S.title, R.maxMarks,R.obtainedMarks
                            FROM result AS R JOIN subjects AS S 
                            ON S.subjectID = R.subjectID
                            WHERE R.rollNum = {} AND R.examTitle = \"{}\" 
                            AND academicYear = {}""".format(rollNo, title, year))

        dataReturned = c.fetchall()
        maxNumTotal = 0
        obtNumTotal = 0
        for subject in dataReturned:
            maxNumTotal += subject[1]
            obtNumTotal += subject[2]

        totalLabel = tk.Label(self.infoFrame, text="{} / {}".format(obtNumTotal, maxNumTotal), font=n_font)

        tk.Label(self.infoFrame, text="TOTAL", bg=r_red, font=n_font).grid(row=5, column=0, pady=15, padx=10,)

        ct = CustomTable(self.infoFrame, ("Subject", " Max Marks", "Marks Obtained"), dataReturned, r_red)
        ct.grid(row=4, column=0, columnspan=3)
        totalLabel.grid(row=5, column=1, padx=10, columnspan=2, sticky="we")

        self.infoFrame.pack(pady=20)


class ExamForm(tk.Frame):

    def __init__(self, parent, window):
        tk.Frame.__init__(self, parent)
        self.config(bg=bg_white)
        self.window = window
        # opening all the images
        self.title_image = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\ef_title.png"))
        self.img_continue = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\ef_continue.png"))
        self.img_cancel = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\rf_cancel.png"))
        self.img_add = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\rf_addBtn.png"))
        titlelabel = tk.Label(self, image=self.title_image, bg=bg_white)

        # classes screen Buttons frames
        self.ButtonFrame = tk.Frame(self)
        self.ButtonFrame.config(bg=bg_white)

        self.form = tk.Frame(self)
        self.form.config(bg=bg_white)
        titlelabel.pack(pady=65, fill="x")
        self.seletionForm()

    def seletionForm(self):

        for widget in self.form.winfo_children():
            widget.destroy()

        for widget in self.ButtonFrame.winfo_children():
            widget.destroy()

        l_title = tk.Label(self.form, text="Examination Title :", bg=bg_white, font=n_font)
        l_title.grid(row=0, column=0, ipadx=10, pady=5, columnspan=2, sticky="w")
        l_year = tk.Label(self.form, text="year :", bg=bg_white, font=n_font)
        l_year.grid(row=2, column=0, ipadx=10, pady=10, sticky="W")
        l_subject = tk.Label(self.form, text="Subject :", bg=bg_white, font=n_font)
        l_subject.grid(row=3, column=2, padx=(50, 5), pady=10, sticky="W")
        l_class = tk.Label(self.form, text="Class :", bg=bg_white, font=n_font)
        l_class.grid(row=3, column=0, ipadx=10, pady=10, sticky="W")
        l_maxMarks = tk.Label(self.form, text="Max Marks: ", bg=bg_white, font=n_font)
        l_maxMarks.grid(row=2, column=2, padx=(50, 5), pady=10, sticky="W")

        e_title = ttk.Entry(self.form, width=30, font=n_font)
        e_title.grid(row=1, column=0, padx=5, ipady=3, pady=(5, 10), columnspan=4, sticky="ew")
        e_year = ttk.Entry(self.form, width=30, font=n_font)
        e_year.grid(row=2, column=1, padx=5, ipady=3)
        e_maxMarks = ttk.Entry(self.form, width=30, font=n_font)
        e_maxMarks.grid(row=2, column=3, padx=5, ipady=3)

        c.execute("SELECT title FROM subjects")
        subject_list = []
        for E in c.fetchall():
            subject_list.append(E[0])
        v_subject = tk.StringVar()
        d_subject = ttk.OptionMenu(self.form, v_subject, subject_list[0], *subject_list)
        d_subject.config(width=50)
        d_subject.grid(row=3, column=3, padx=5, ipady=3)

        c.execute("SELECT * FROM class_view ")
        class_list = []
        for E in c.fetchall():
            class_list.append(E[0])
        v_class = tk.StringVar()
        d_class = ttk.OptionMenu(self.form, v_class, class_list[0], *class_list)
        d_class.config(width=50)
        d_class.grid(row=3, column=1, padx=5, ipady=3)

        btn_continue = tk.Button(self.ButtonFrame, image=self.img_continue, bg=bg_white, border=0,
                                 activebackground=bg_white,
                                 command=lambda: self.entryForm(v_class.get(), e_title.get(), v_subject.get(),
                                                                e_year.get(), e_maxMarks.get()))
        btn_cancel = tk.Button(self.ButtonFrame, image=self.img_cancel, bg=bg_white, border=0,
                               activebackground=bg_white,
                               command=lambda: self.window.previous_screen())

        # adding the button in horizoltal grid
        btn_continue.grid(row=1, column=0, padx=10)
        btn_cancel.grid(row=1, column=1, padx=10)

        # adding the bar and buttons to the screen

        self.form.pack()
        self.ButtonFrame.pack(pady=50)

    def entryForm(self, classId, ExamTitle, subject, year, maxMarks):
        if ExamTitle == "" or year == "" or maxMarks =="":
            self.window.show_message("Can not search, invalid data", r_red)
            return
        else:
            self.window.show_message("", bg_white)
        for widget in self.form.winfo_children():
            widget.destroy()

        for widget in self.ButtonFrame.winfo_children():
            widget.destroy()

        btn_add = tk.Button(self.ButtonFrame, image=self.img_add, bg=bg_white, border=0,
                            activebackground=bg_white,
                            command=lambda: self.insertData(classId, ExamTitle, subject, year, maxMarks, e_Marks))

        btn_cancel = tk.Button(self.ButtonFrame, image=self.img_cancel, bg=bg_white, border=0,
                               activebackground=bg_white,
                               command=lambda: self.seletionForm())
        btn_cancel.grid(row=0, column=1)
        btn_add.grid(row=0, column=0)

        c.execute("SELECT rollNum, CONCAT(fname,' ',lname) FROM student WHERE classID = \"{}\"".format(classId))

        studentList = c.fetchall()
        rollNumList = []

        for student in studentList:
            rollNumList.append(student[0])

        print(rollNumList)

        stu_table = CustomTable(self.form, ("Roll NO", "Name "), studentList, r_red)
        stu_table.grid(row=0, column=0, sticky="n")
        e_frame = tk.Frame(self.form)
        e_frame.config(bg=bg_white)
        tk.Label(e_frame, text="Obtained Marks", bg=r_red, font=n_font).grid(row=0, column=0, ipadx=15, pady=10,
                                                                             sticky="WE")
        e_Marks = {}
        for i, rollNum in enumerate(rollNumList):
            e_Marks[rollNum] = ttk.Entry(e_frame, width=30, font=n_font)
            e_Marks[rollNum].grid(row=i + 1, column=0, pady=2)

        e_frame.grid(row=0, column=1, sticky="n")
        self.form.pack()
        self.ButtonFrame.pack()

    def insertData(self, classId, ExamTitle, subject, year, maxMarks, marksDic):

        subject_dic = {}
        c.execute("SELECT title,subjectID FROM subjects")

        for E in c.fetchall():
            subject_dic[E[0]] = E[1]

        for rollnum in marksDic.keys():
            query = "INSERT INTO result VALUES(\"{}\",{} ,\"{}\",\"{}\",\"{}\",\"{}\")".format(
                ExamTitle,
                year,
                rollnum,
                subject_dic[subject],
                maxMarks,
                marksDic[rollnum].get()
            )
            try:
                c.execute(query)
                self.window.show_message("Data Added sucessfully", s_green)
            except:
                self.window.show_message("Can not continue, The data entered is incorrect", r_red)
                return

        mydb.commit()


class ClassSelectScreen(tk.Frame):

    def __init__(self, parent, window):
        tk.Frame.__init__(self, parent)
        self.config(bg=bg_white)

        # opening all the images
        self.title_image = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\css_title.png"))
        self.img_continue = ImageTk.PhotoImage(Image.open("C:\\Users\\abdul\\Downloads\\Imaginary School MS\\Assets\\css_continuebtn.png"))

        titlelabel = tk.Label(self, image=self.title_image, bg=bg_white)
        btn_continue = tk.Button(self, image=self.img_continue, bg=bg_white, border=0, activebackground=bg_white)

        l_class = tk.Label(self, text="Class :", bg=bg_white, font=n_font)
        l_class.grid(row=0, column=0, ipadx=10, pady=10, sticky="W")

        c.execute("SELECT * FROM class_view ")
        class_list = []
        for E in c.fetchall():
            class_list.append(E[0])

        self.v_class = tk.StringVar()
        self.d_class = ttk.OptionMenu(self, self.v_class, class_list[0], *class_list)
        self.d_class.config(width=100)
        self.d_class.grid(row=1, column=0, ipady=3)


class CustomTable(tk.Frame):
    def __init__(self, parent, attributes, data, color):
        tk.Frame.__init__(self, parent)
        self.config(bg=bg_white)

        rows = len(data)
        columns = len(attributes)

        for i, a in enumerate(attributes):
            tk.Label(self, text=a, bg=color, font=n_font).grid(row=0, column=i, ipadx=15, pady=10, sticky="WE")

        for i, row in enumerate(data):
            for j, entry in enumerate(row):
                tk.Label(self, text=entry, bg=bg_white, font=n_font).grid(row=i + 1, column=j, ipadx=15, sticky="W")

login = Login()
login.mainloop()

if run_app is True:
    app = SchoolManagementSystem()
    app.mainloop()

