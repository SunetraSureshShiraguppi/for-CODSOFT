import tkinter as tk
from tkinter import messagebox

root=tk.Tk()
root.title("TO-DO-LIST ")
root.configure(bg='black')
tasks=[]


def add():
        data=entry.get()
        if data:                     
            tasks.append(data)             
            update()          
            entry.delete(0,tk.END)
        else:
            tk.messagebox.showwarning(title="Attention !!", message="warning you must enter a task.")
            
def delete():
        selected_data=listbox.curselection()
        if selected_data:
            del tasks[selected_data[0]]
            update()
        else:
            tk.messagebox.showwarning(title="Attention", message="warning you must select a task.")


def save():
      with open("saveddata.txt", "w") as file:
        for data in tasks:
            file.write(data + "\n")
      tk.messagebox.showinfo(title="attention",message=" Tasks saved successfully.")

def update():
       listbox.delete(0,tk.END)
       for data in tasks:
            listbox.insert(tk.END,task)




entry=tk.Entry(root,width=80)
entry.pack(pady=20)

add_button=tk.Button(root, text="Add Task", font=("arial",13,"bold"),background="blue",width=35, command=add)
add_button.pack(pady=20)

frame=tk.Frame(root)
frame.pack()

listbox=tk.Listbox(frame,width=70,height=15)
listbox.pack(side=tk.LEFT, fill=tk.BOTH,pady=50)


delete_button=tk.Button(root,text="Delete Task",font=("arial",13,"bold"),background="yellow",width=35, command=delete)
delete_button.pack(pady=20)

save_button = tk.Button(root, text="Save Tasks",font=("arial",13,"bold"),background="green",width=35, command=save)
save_button.pack(pady=20)


scrollbar=tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT,fill=tk.Y)

listbox.config(yscrollbarcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

    
root.mainloop
