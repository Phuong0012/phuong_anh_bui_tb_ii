import tkinter as tk
from tkinter import messagebox
import time
from PIL import Image, ImageTk
import random
from playsound import playsound

root = tk.Tk()
root.title("Study Buddy")
root.configure(background="black")
root.minsize(height=700, width=500)
root.resizable(False, False)

break_hrs = hrs = tk.StringVar()
break_mins = mins = tk.StringVar()
break_sec = sec = tk.StringVar()

task_list=[]

def destroy_window(name):
    name.destroy()

def place_image(x, y, file):
    img = Image.open(file)
    img = img.resize((200, 200), Image.ANTIALIAS)

    black_background = Image.new("RGB", img.size, "black")
    black_background.paste(img, (0, 0), img)

    # Convert the image to PhotoImage
    test = ImageTk.PhotoImage(black_background)

    # Create a label with the black background
    label1 = tk.Label(image=test, bg="black")
    label1.image = test

    # Position image
    label1.place(relx=x, rely=y, anchor=tk.CENTER)

def clear_widgets(place):
    # loops through all the widgets and kills them
    for i in place.winfo_children():
        i.destroy()

def play(x):
    #plays sound
    playsound(x)

def home_button(k, l):
    homepage = tk.Button(root,
                        text="🏠",
                         font=30,
                        command=create_homepage
                        )
    homepage.place(relx=k, rely=l)


def to_instructions():
#creates INSTRUCIONS PAGE
    clear_widgets(root)
    instructions_header = tk.Label(root,
                   text="How to use this app",
                   fg = "white",
                   bg ="black",
                   font =("Arial",40))
    instructions_header.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

    text1 = tk.Label(root,
                    text="1. Open your To-do list and add your To-Dos"
                         "\n 2. Click on 'Let's start' and choose your timer \n"
                         "3. When your timer finishes either restart\n or check off your finished task"
                         "\n 4. HAVE FUN \n",
                    fg="black",
                    bg="grey",
                    font=("Arial", 15))
    text1.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    home_button(0.5, 0.7)

def timer_window_button(m, n):
    next = tk.Button(root,
                        text="⏭",
                         font=30,
                        command=timer_window
                        )
    next.place(relx=m, rely=n)

def recieve_message():
#AFTER MARKING A MESSAGE AS DONE THE PET GIVES YOU A NICE MESSAGE
    messages=["You're doing great!", "I'm so proud of you!", "You can be proud of yourself!",
              "Your tasks will be finished in no time", "You deserve a break tonight", "Wow you're so fast!"]
    random_pick = random.randrange(len(messages))
    output=messages[random_pick]

    pet=tk.Label(root,
             text=output,
             bg="grey", fg="black",
             font="arial 20")
    pet.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

    root.after(3000, lambda: pet.destroy())


def add_task():
#LETS YOU ADD TASK TO TO-DO LIST
    task=task_entry.get()
    task_entry.delete(0, tk.END)
    if task:
        with open("tasklist.txt", "a") as taskfile:
            taskfile.write(f"\n{task}")
            task_list.append(task)
            listbox.insert(tk.END, task)

def taskDone():
#MARKS SELECTED TASK AS DONE

    selected_task_index = listbox.curselection()

    if selected_task_index:
        selected_task_index = selected_task_index[0]
        selected_task = listbox.get(selected_task_index)

        # Check if "DONE" is already present in the task
        if "DONE" not in selected_task:
            # Add "DONE" after the selected task in the listbox
            play("sounds/trumpet.mp3")
            updated_task = selected_task + " DONE"

            # Update the task_list with the modified task
            task_list[selected_task_index] = updated_task

            # Update the listbox with the modified task
            listbox.delete(selected_task_index)
            listbox.insert(selected_task_index, updated_task)

            # Update the tasklist.txt file
            with open("tasklist.txt", "w") as taskfile:
                for task in task_list:
                    taskfile.write(task + "\n")
            recieve_message()
        else:
            tk.messagebox.showwarning("Warning", "Task is already done")

def deleteTask():
#DELETES ALL TASKS
    task_list.clear()

    # Clear the listbox
    listbox.delete(0, tk.END)

    # Update the tasklist.txt file
    with open("tasklist.txt", "w") as taskfile:
        for task in task_list:
            taskfile.write(task + "\n")

def open_task_file():
#OPENS .TXT FILE
    try:
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()
            task_list.clear()
            listbox.delete(0, tk.END)
        for task in tasks:
            task = task.strip()  # Remove leading and trailing whitespace characters
            if task:  # Check if the line is not empty after stripping
                task_list.append(task)
                listbox.insert(tk.END, task)

    except:
        file = open_task_file("tasklist.txt", "w")
        file.close()


def to_do():
#CREATES TO-DO PAGE

    global listbox, task_entry

    clear_widgets(root)

    header=tk.Label(root,
                    text="Your TO-DO list",
                    bg="black",
                    fg="white",
                    font="Arial 25 bold")
    header.place(x=130, y=40)

    task_entry=tk.Entry(root,
                        bg="white",
                        fg="black",
                        font="Arial 15",
                        bd=0)
    task_entry.place(x=100, y=140)
    task_entry.focus()

    add_button=tk.Button(root,
                         text="ADD",
                         bg="grey",fg="white",
                         font="arial 17",
                         command=add_task)
    add_button.place(x=340, y=130)

    frame1= tk.Frame(root,
                     width=310,
                     height=340,
                     bg="white", )
    frame1.pack(pady=200, padx=100)

    listbox=tk.Listbox(frame1,
                       font="arial 15",
                       width=25, height=14,
                       bg="white",
                       fg="black")
    listbox.pack(side=tk.LEFT, fill=tk.BOTH, padx=2)

    scrollbar= tk.Scrollbar(frame1)
    scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)

    open_task_file()

    delete_button=tk.Button(root,
                            text="🗑️",
                            bg="red",
                            fg="white",
                            font="arial 18",
                            command=deleteTask)
    delete_button.place(x=160, y=550)

    home_button(0.5, 0.75)

def to_doNewWindow():
#OPENS POP-UP TO-DO LIST AFTER TIMER FINISHES

    global listbox, task_entry

    new_to_do = tk.Toplevel(root)
    new_to_do.title("To-Do List")
    new_to_do.geometry("300x470")
    new_to_do.resizable(False, False)
    new_to_do.configure(bg="black")

    header=tk.Label(new_to_do,
                    text="Your TO-DO list",
                    bg="black",
                    fg="white",
                    font="Arial 20 bold")
    header.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

    frame1= tk.Frame(new_to_do,
                     width=250,
                     height=250,
                     bg="white", )
    frame1.pack(pady=90, padx=10)

    listbox=tk.Listbox(frame1,
                       font="arial 15",
                       bg="white",
                       fg="black")
    listbox.pack(side=tk.LEFT, fill=tk.BOTH, padx=2)

    scrollbar= tk.Scrollbar(frame1)
    scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)

    open_task_file()

    delete_button=tk.Button(new_to_do,
                            text="🗑️",
                            bg="red",
                            fg="white",
                            font="arial 15",
                            command= deleteTask)
    delete_button.place(x=85, y=370)

    done_button=tk.Button(new_to_do,
                          text="✔",
                          bg="green",
                          fg="white",
                          font="arial 15",
                          command=taskDone)
    done_button.place(x=175, y=370)


def timer_window():
#CREATES TIMER SELECTION PAGE
    global header, new_window, pomodoro, animedoro
    new_window = tk.Toplevel(root)
    new_window.title("Timer")
    new_window.geometry("400x500")
    new_window.resizable(False, False)
    new_window.configure(bg="black")

    header = tk.Label(new_window, text="Study time",
                     font="Arial 25 bold",
                     bg="black", fg="white")
    header.place(x=90, y =100)

    pomodoro=tk.Button(new_window,
                       text="Pomodoro",
                       font="Arial 15",
                       bg="grey", fg="white",
                       command=pomodoro_tech
                       )
    pomodoro.place(x=70, y=300)

    animedoro=tk.Button(new_window,
                       text="Animedoro",
                       font="Arial 15",
                       bg="grey", fg="white",
                        command=animedoro_tech
                       )
    animedoro.place(x=230, y=300)

    custom=tk.Button(new_window,
                       text="Custom",
                       font="Arial 15",
                       bg="grey", fg="white",
                       command=custom_tech)
    custom.place(x=200, y=390, anchor=tk.CENTER)

def timer():
#DISPLAYS TIMER AS TEXTVARIABLE > FOR PRE-SET TIMERS (ANIME- & POMODORO)

    hour_label = tk.Label(new_window,
                          textvariable=hrs,
                          width=2,
                          font="arial 50",
                          bg="black",
                          fg="white",
                          bd=0)
    hour_label.place(x=30, y=155)
    hrs.set("00")

    min_label = tk.Label(new_window,
                         textvariable=mins,
                         width=2,
                         font="arial 50",
                         bg="black",
                         fg="white",
                         bd=0)
    min_label.place(x=150, y=155)
    mins.set("00")

    sec_label = tk.Label(new_window,
                         textvariable=sec,
                         width=2,
                         font="arial 50",
                         bg="black",
                         fg="white",
                         bd=0)
    sec_label.place(x=270, y=155)
    sec.set("00")

    tk.Label(new_window,
             text="hours",
             font="arial 12",
             bg="black",
             fg="white").place(x=45, y=240)

    tk.Label(new_window,
             text="minutes",
             font="arial 12",
             bg="black",
             fg="white").place(x=155, y=240)

    tk.Label(new_window,
             text="seconds",
             font="arial 12",
             bg="black",
             fg="white").place(x=275, y=240)

def Break_Timer(s, f, t):
#FUNCTION OF BREAK TIMER
    break_times = int(s) * 3600 + int(f) * 60 + int(t)

    while break_times > -1:
        minute, second = (break_times // 60, break_times % 60)
        hour=0
        if minute > 60:
            hour, minute = (minute // 60, minute % 60)

        sec.set("{:02d}".format(second))
        mins.set("{:02d}".format(minute))
        hrs.set("{:02d}".format(hour))

        time.sleep(1)
        root.update()

        break_times -= 1

        if (break_times==0):
            play("sounds/bell.mp3")
            new_window.destroy()
            choice_window()

def Work_Timer(work_hrs, work_mins, work_sec):
#FUNCTION OF WORK TIMER
    work_times = int(work_hrs) * 3600 + int(work_mins) * 60 + int(work_sec)
    while work_times > -1:
        minute, second =(work_times // 60, work_times % 60)
        hour =0
        if minute>60:
            hour, minute=(minute//60, minute%60)

        sec.set(second)
        mins.set(minute)
        hrs.set(hour)

        root.update()
        time.sleep(1)

        work_times -= 1
        if (work_times==0):
            play("sounds/bell.mp3")


def pomodoro_tech():
#PRE-SET VARIABLES OF POMODORO TIMER
    print("pomodoro")
    clear_widgets(new_window)

    pomodoro_label=tk.Label(new_window, text="Pomodoro running...", fg="orange", bg="black", font="arial 20")
    pomodoro_label.place(x=50, y=45)
    timer()
    Work_Timer(0, 25, 0)
    Break_Timer(0, 5, 0)

def animedoro_tech():
#PRE-SET VARIABLES OF ANIMEDORO TIMER

    print("animedoro")
    clear_widgets(new_window)

    animedoro_label = tk.Label(new_window, text="Animedoro running...", fg="blue", bg="black", font="arial 20 bold")
    animedoro_label.place(x=50, y=45)
    timer()
    Work_Timer(0, 0, 4)
    Break_Timer(0, 0, 4)


def custom_tech2():
#CREATES WIDGETS FOR BREAK SECTION OF A CUSTOM TIMER
    clear_widgets(new_window)

    tk.Label(new_window,
             text="Input your break time:",
             bg="black", fg="white",
             font="arial 20 bold").place(x=70, y= 150)

    hour_entry = tk.Entry(new_window,
                          textvariable=hrs,
                          width=2,
                          font="arial 25",
                          bg="white",
                          fg="black",
                          bd=0)
    hour_entry.place(x=115, y=235)
    hrs.set("00")

    min_entry = tk.Entry(new_window,
                         textvariable=mins,
                         width=2,
                         font="arial 25",
                         bg="white",
                         fg="black",
                         bd=0)
    min_entry.place(x=175, y=235)
    mins.set("00")

    sec_entry = tk.Entry(new_window,
                         textvariable=sec,
                         width=2,
                         font="arial 25",
                         bg="white",
                         fg="black",
                         bd=0)
    sec_entry.place(x=235, y=235)
    sec.set("00")

    tk.Label(new_window,
             text="hours",
             font="arial 8",
             bg="black",
             fg="white").place(x=115, y=275)

    tk.Label(new_window,
             text="minutes",
             font="arial 8",
             bg="black",
             fg="white").place(x=175, y=275)

    tk.Label(new_window,
             text="seconds",
             font="arial 8",
             bg="black",
             fg="white").place(x=235, y=275)

    button1 = tk.Button(new_window,
                       text="Start",
                       bg="red",
                       fg="white",
                       bd=0,
                       width=20,
                       height=1,
                       font="arial 10 bold",
                       command=lambda: [Break_Timer(hour_entry.get(), min_entry.get(), sec_entry.get())])
    button1.pack(padx=5, pady=40, side=tk.BOTTOM)

def custom_tech():
#CREATES WIDGERS FO WORK SECTION OF A CUSTOM TIMER
    clear_widgets(new_window)

    tk.Label(new_window,
             text="Input your work time:",
             bg="black", fg="white",
             font="arial 20 bold").place(x=70, y= 150)

    hour_entry = tk.Entry(new_window,
                          textvariable=hrs,
                          width=2,
                          font="arial 25",
                          bg="white",
                          fg="black",
                          bd=0)
    hour_entry.place(x=115, y=235)
    hrs.set("00")

    min_entry = tk.Entry(new_window,
                         textvariable=mins,
                         width=2,
                         font="arial 25",
                         bg="white",
                         fg="black",
                         bd=0)
    min_entry.place(x=175, y=235)
    mins.set("00")

    sec_entry = tk.Entry(new_window,
                         textvariable=sec,
                         width=2,
                         font="arial 25",
                         bg="white",
                         fg="black",
                         bd=0)
    sec_entry.place(x=235, y=235)
    sec.set("00")

    tk.Label(new_window,
             text="hours",
             font="arial 8",
             bg="black",
             fg="white").place(x=115, y=275)

    tk.Label(new_window,
             text="minutes",
             font="arial 8",
             bg="black",
             fg="white").place(x=175, y=275)

    tk.Label(new_window,
             text="seconds",
             font="arial 8",
             bg="black",
             fg="white").place(x=235, y=275)

    button1 = tk.Button(new_window,
                       text="Start",
                       bg="red",
                       fg="white",
                       bd=0,
                       width=20,
                       height=1,
                       font="arial 10 bold",
                       command=lambda: [Work_Timer(hour_entry.get(), min_entry.get(),sec_entry.get()),
                                        custom_tech2()])
    button1.pack(padx=5, pady=40, side=tk.BOTTOM)


def start_page():
#CREATES MAIN PAGE AFTER HOMEPAGE

    print("hello")
    clear_widgets(root)

    place_image(0.5, 0.6, "images/lil_guy.png")
    home_button(0.8, 0.3)
    timer_window_button(0.8, 0.5)

def create_homepage():
#CREATES HOMEPAGE

    clear_widgets(root)

    welcome = tk.Label(root,
                       text="Welcome",
                       fg = "white",
                       bg ="black",
                       font =("Arial", 40))
    welcome.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

    instructions_button = tk.Button(root,
                                    text = "Instructions page",
                                    fg="white",
                                    bg="grey",
                                    font=("Arial", 15),
                                    command=to_instructions)
    instructions_button.place(relx=0.5,
                              rely=0.7,
                              anchor=tk.CENTER)

    todo_button = tk.Button(root,
                                    text = "To-Do List",
                                    fg="white",
                                    bg="grey",
                                    font=("Arial", 15),
                            command=to_do)
    todo_button.place(relx=0.5,
                              rely=0.77,
                              anchor=tk.CENTER)

    start_button = tk.Button(root,
                                    text = "Lets's start",
                                    fg="grey",
                                    bg="white",
                                    font=("Arial", 15),
                                    command=start_page)
    start_button.place(relx=0.5,
                              rely=0.84,
                              anchor=tk.CENTER)

    place_image(0.5, 0.5, "images/lil_guy.png")

def choice_window():
#POP-UP WINDOW AFTER BREAK TIMER FINISHES
    choice = tk.Toplevel(root)
    choice.title("Choose")
    choice.geometry("300x300")
    choice.resizable(False, False)
    choice.configure(bg="grey")

    choice_label = tk.Label(choice,
             text="What do you want to do",
             fg="black", bg="grey",
             font="arial 15 bold")
    choice_label.place(x=15,y=30)

    button1=tk.Button(choice,
                      text="restart timer",
                      fg="white", bg="grey",
                      font="arial 15",
                      command=lambda: [timer_window(), destroy_window(choice)])
    button1.place(x=100, y=150)

    button2=tk.Button(choice,
                      text="open to-do list",
                      fg="white", bg="grey",
                      font="arial 15",
                      command= lambda: [to_doNewWindow(), destroy_window(choice)])
    button2.place(x=90, y=200)

create_homepage()
root.mainloop()
