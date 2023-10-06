from tkinter import *

def add_t():
    task = entry.get()
    my_tasks.insert(END, task)
    print()
    
def del_t():
    selected_item = my_tasks.curselection()
    my_tasks.delete(selected_item)
    

# Create the root window
window = Tk()

window.geometry("500x500")

window.title("To Do GUI")
label1 = Label(window,text="TO DO",bd=10)

label1.pack(side=TOP)

entry = Entry(window,font=("Arial",50))

entry.pack(side=BOTTOM)

my_tasks = Listbox(window,font="Arial",width=25,height=5,bg="SystemButtonFace",bd=0,fg="#464646",highlightthickness=0,activestyle="none")
my_tasks.pack(side="left",fill=BOTH)
#demo list

tasks = ["Study for Analysis of algo","Walk the dog","Take a nap"]

for item in tasks:
    my_tasks.insert(END, item)

myscroll = Scrollbar(window)
myscroll.pack(side="right",fill=BOTH)

my_tasks.config(yscrollcommand=myscroll.set)
myscroll.config(command=my_tasks.yview)


button_frame = Frame(window)
button_frame.pack(pady=20)
button1 = Button(button_frame,text="ADD TASK",command=add_t)
button1.pack(side=BOTTOM)
button2 = Button(button_frame,text="REMOVE TASK",command=del_t)
button2.pack(side=BOTTOM)
button3 = Button(button_frame,text="FINISH A TASK",command=add_t)
button3.pack(side=BOTTOM)
button4 = Button(button_frame,text="RESTART A TASK",command=del_t)
button4.pack(side=BOTTOM)
window.mainloop()