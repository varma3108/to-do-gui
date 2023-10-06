from tkinter import *

def add_t():
    task = entry.get()
    my_tasks.insert(END, task)
    print()
    
def del_t():
    selected_item = my_tasks.curselection()
    my_tasks.delete(selected_item)
    
def fin_t():
    my_tasks.itemconfig(my_tasks.curselection(),fg="#0F9D58")
    #slection bar clear
    my_tasks.select_clear(0,END)

def re_t():
    my_tasks.itemconfig(my_tasks.curselection(),fg="#464646")
    #slection bar clear
    my_tasks.select_clear(0,END)
    
def refin_t():
    count =0 
    while count < my_tasks.size():
        if my_tasks.itemcget(count,"fg") =="#0F9D58":
            my_tasks.delete(my_tasks.index(count))
        count+=1
        
        
def save_list():
    with open("tasks.txt","w") as f:
        list_tuple = my_tasks.get(0,END)
        for item in list_tuple:
            if item.endswith("\n"):
                f.write(item)
            else:
                f.write(item+"\n")
                
def open_list():
    try:
        with open("tasks.txt","r") as f:
            for line in f:
                my_tasks.insert(END,line)
    except:
        return

def clear_list():
    my_tasks.delete(0,END)

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
#file save options
my_menu = Menu(window)
window.config(menu=my_menu)     
  
  #add items to the menu
file_menu = Menu(my_menu,tearoff=False)
#add dropdown items
file_menu.add_command(label="Save List",command= save_list)
file_menu.add_command(label="Open List",command= open_list)
file_menu.add_separator()
file_menu.add_command(label="Clear List",command= clear_list)
my_menu.add_cascade(label="File",menu=file_menu)    

#button frame
button_frame = Frame(window)
button_frame.pack(pady=20)
button1 = Button(button_frame,text="ADD TASK",command=add_t)
button1.pack(side=TOP)
button2 = Button(button_frame,text="REMOVE TASK",command=del_t)
button2.pack(side=TOP)
button3 = Button(button_frame,text="FINISH A TASK",command=fin_t)
button3.pack(side=TOP)
button4 = Button(button_frame,text="RESTART A TASK",command=re_t)
button4.pack(side=TOP)
button5 =  Button(button_frame,text="REMOVE FINISHED TASKS",command=refin_t)
button5.pack(side=TOP)
window.mainloop()