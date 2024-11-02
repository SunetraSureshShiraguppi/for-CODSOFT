#from tkinter import*
import customtkinter 
from tkinter import END
from tkinter import messagebox
import math

def clear():
    entryfield.delete(0,END)

def button_click(value):
    entryfield.insert(END,value)
    
def answer():
    expression=entryfield.get()
    try:
      result=eval(expression)
      entryfield.delete(0,END)
      entryfield.insert(0,result)
    except SyntaxError:
        messagebox.showerror("error","invalid expression,check the entered data")
    except ZeroDivisionError:
        messagebox.showerror('Error','zero cannot be devided by zero')



def backspace():
    data= entryfield.get()
    entryfield.delete(0, END)
    entryfield.insert(END, data[:-1])

def squareroot():
    data=entryfield.get()
    entryfield.delete(0,END)
    entryfield.insert(END,str(math.sqrt(float(data))))



root=customtkinter.CTk()
root.title("calculator")
root.geometry('400x420')
root.config(bg='white')

entryfield=customtkinter.CTkEntry(root, font=('arial', 20,'bold'), text_color='white', fg_color='black', border_color='white',width=380,height=50)
entryfield.grid(row=0,column=0,padx=10,pady=10, columnspan=5)

button_7=customtkinter.CTkButton(root,text='7',font=('arial', 20,'bold'),width=80,bg_color='black',text_color='black',hover_color='yellow',command=lambda :button_click('7'))
button_7.grid(row=1,column=0,pady=15)

button_8=customtkinter.CTkButton(root,text='8',font=('arial', 20,'bold'),width=80,bg_color='black',text_color='black',hover_color='yellow',command=lambda:button_click('8'))
button_8.grid(row=1,column=1)

button_9=customtkinter.CTkButton(root,text='9',font=('arial', 20,'bold'),width=80,bg_color='black',text_color='black',hover_color='yellow',command=lambda:button_click('9'))
button_9.grid(row=1,column=2)

button_plus=customtkinter.CTkButton(root,text='+',font=('arial', 20,'bold'),width=80,bg_color='black',text_color='white',fg_color='black',hover_color='orange3',command=lambda:button_click('+'))
button_plus.grid(row=1,column=3)

button_4=customtkinter.CTkButton(root,text='4',font=('arial', 20,'bold'),width=80,bg_color='black',text_color='black',hover_color='yellow',command=lambda:button_click('4'))
button_4.grid(row=2,column=0,pady=15)

button_5=customtkinter.CTkButton(root,text='5',font=('arial', 20,'bold'),width=80,bg_color='black',text_color='black',hover_color='yellow',command=lambda:button_click('5'))
button_5.grid(row=2,column=1)

button_6=customtkinter.CTkButton(root,text='6',font=('arial', 20,'bold'),width=80,bg_color='black',text_color='black',hover_color='yellow',command=lambda:button_click('6'))
button_6.grid(row=2,column=2)

button_sub=customtkinter.CTkButton(root,text='-',font=('arial', 20,'bold'),width=80,bg_color='black',text_color='white',fg_color='black',hover_color='orange3',command=lambda:button_click('-'))
button_sub.grid(row=2,column=3)

button_1=customtkinter.CTkButton(root,text='1',font=('arial', 20,'bold'),width=80,bg_color='black',text_color='black',hover_color='yellow',command=lambda:button_click('1'))
button_1.grid(row=3,column=0,pady=15)

button_2=customtkinter.CTkButton(root,text='2',font=('arial', 20,'bold'),width=80,bg_color='black',text_color='black',hover_color='yellow',command=lambda:button_click('2'))
button_2.grid(row=3,column=1)

button_3=customtkinter.CTkButton(root,text='3',font=('arial', 20,'bold'),width=80,bg_color='black',text_color='black',hover_color='yellow',command=lambda:button_click('3'))
button_3.grid(row=3,column=2)

button_mul=customtkinter.CTkButton(root,text='*',font=('arial', 20,'bold'),width=80,bg_color='black',text_color='white',fg_color='black',hover_color='orange3',command=lambda:button_click('*'))
button_mul.grid(row=3,column=3)

button_0=customtkinter.CTkButton(root,text='0',font=('arial', 20,'bold'),width=80,bg_color='black',text_color='black',hover_color='yellow',command=lambda:button_click('0'))
button_0.grid(row=4,column=0,pady=15)

button_dot=customtkinter.CTkButton(root,text='.',font=('arial', 20,'bold'),width=80,bg_color='black',text_color='black',hover_color='yellow',command=lambda:button_click('.'))
button_dot.grid(row=4,column=1)

button_squareroot=customtkinter.CTkButton(root,text='sqrt',font=('arial', 20,'bold'),width=80,bg_color='black',text_color='white',fg_color='black',hover_color='orange3',command=squareroot)
button_squareroot.grid(row=4,column=2,pady=15)



button_slash=customtkinter.CTkButton(root,text='/',font=('arial', 20,'bold'),width=80,bg_color='black',text_color='white',fg_color='black',hover_color='orange3',command=lambda:button_click('/'))
button_slash.grid(row=4,column=3)

button_openbracket=customtkinter.CTkButton(root,text='(',font=('arial', 20,'bold'),width=80,bg_color='black',text_color='white',fg_color='black',hover_color='orange3',command=lambda:button_click('('))
button_openbracket.grid(row=5,column=0,pady=15)

button_closebracket=customtkinter.CTkButton(root,text=')',font=('arial', 20,'bold'),width=80,bg_color='black',text_color='white',fg_color='black',hover_color='orange3',command=lambda:button_click(')'))
button_closebracket.grid(row=5,column=1,pady=15)
                                     


button_backspace=customtkinter.CTkButton(root,text='bs',font=('arial', 20,'bold'),width=80,bg_color='black',text_color='white',fg_color='black',hover_color='orange3',command=backspace)
button_backspace.grid(row=5,column=2,pady=15)


button_clear=customtkinter.CTkButton(root,text='clear',font=('arial', 20,'bold'),width=80,bg_color='black',text_color='black',fg_color='red',hover_color='red4',command=clear)
button_clear.grid(row=5,column=3,pady=15)


button_equal=customtkinter.CTkButton(root,text='=',font=('arial', 20,'bold'),width=240,bg_color='black',text_color='black',fg_color='green',hover_color='dark green',command=answer)
button_equal.grid(row=6,column=0,columnspan=4,pady=15)


root.mainloop()
