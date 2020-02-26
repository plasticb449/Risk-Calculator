from tkinter import *

root = Tk()
root.title("Risk Calculator")
root.geometry("300x300")

#functions
def risk_cal():
    balance = b_e.get()
    percent = p_e.get()
    answer_e.delete(0, END)
    answer_e.insert(0, float(balance) * float(percent))
def size_cal():
    balance = b_e.get()
    average_price = a_e.get()
    answer_e.delete(0, END)
    answer_e.insert(0, float(balance) / float(average_price))
def stop_cal2():
    average_price = a_e.get()
    balance = b_e.get()
    percent = p_e.get()
    risk = float(balance) * float(percent)
    size = float(balance) / float(average_price)
    answer_e.delete(0, END)
    answer_e.insert(0, float(average_price) - (float(risk) / float(size)))
def clear():
    b_e.delete(0, END)
    p_e.delete(0, END)
    a_e.delete(0, END)
    answer_e.delete(0, END)

#hover
def rbon_button(e):
    r_b['fg'] = 'white'
    r_b['bg'] = 'black'
def rbleave_button(e):
    r_b['fg'] = 'black'
    r_b['bg'] = 'white'

def sbon_button(e):
    s_b [ 'fg'] = 'white'
    s_b ['bg'] = 'black'
def sbleave_button(e):
    s_b['fg'] = 'black'
    s_b['bg'] = 'white'

def spbon_button(e):
    sp_b['fg'] = 'white'
    sp_b['bg'] = 'black'
def spbleave_button(e):
    sp_b['fg'] = 'black'
    sp_b['bg'] = 'white'

def clon_button(e):
    cl_b['fg'] = 'white'
    cl_b['bg'] = 'black'

def clleave_button(e):
    cl_b['fg'] = 'black'
    cl_b['bg'] = 'white'

#entry
b_e = Entry(root,fg='black',bg='white',font=20)
b_e.place(relx=0.5, rely=0.02, relheight=0.1, relwidth=0.45)
p_e = Entry(root,fg='black',bg='white',font=20)
p_e.place(relx=0.5, rely=0.13, relheight=0.1, relwidth=0.45)
a_e = Entry(root,fg='black',bg='white',font=20)
a_e.place(relx=0.5, rely=0.24, relheight=0.1, relwidth=0.45)
answer_e= Entry(root,fg='black',bg='white',font=20,justify='cente'
                                                                 'r')
answer_e.place(relx=0.04, rely=0.57, relheight=0.4, relwidth=0.909)
# label
b_l = Label(root, fg='black', bg='white', text="Balance :",font=20,relief='raised')
b_l.place(relx=0.04, rely=0.02, relheight=0.1, relwidth=0.45)
p_l = Label(root, fg='black', bg='white', text="Percent :",font=20,relief='raised')
p_l.place(relx=0.04, rely=0.13, relheight=0.1, relwidth=0.45)
a_l = Label(root, fg='black', bg='white', text="Average :",font=20,relief='raised')
a_l.place(relx=0.04, rely=0.24, relheight=0.1, relwidth=0.45)

#buttons

r_b = Button(root, text=" Risk ", fg='black', bg='white', activebackground='white', command= risk_cal,font=20)
r_b.place(relx=0.04, rely=0.35, relheight=0.1, relwidth=0.45)
r_b.bind('<Enter>',rbon_button)
r_b.bind('<Leave>',rbleave_button)

s_b = Button(root, text=" Size ", fg='black', bg='white', command= size_cal,font=20)
s_b.place(relx=0.04, rely=0.46, relheight=0.1, relwidth=0.45)
s_b.bind('<Enter>',sbon_button)
s_b.bind('<Leave>',sbleave_button)

sp_b = Button(root, text=" Stop ", fg='black', bg='white', command= stop_cal2,font=20)
sp_b.place(relx=0.5, rely=0.35, relheight=0.1, relwidth=0.45)
sp_b.bind('<Enter>',spbon_button)
sp_b.bind('<Leave>',spbleave_button)


cl_b = Button(root, text=" Clear ", fg='black', bg='white', activebackground='white', command=clear,font=20)
cl_b.place(relx=0.5, rely=0.46, relheight=0.1, relwidth=0.45)
cl_b.bind('<Enter>', clon_button)
cl_b.bind('<Leave>', clleave_button)

root.mainloop()