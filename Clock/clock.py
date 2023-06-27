from tkinter import *
from time import *
def show():
    t=strftime('%H:%M:%S')
    tlb.config(text=t)
    d = strftime('%Y-%m-%d')
    dlb.config(text=d)
    wd.after(500,show)
wd =Tk()
wd.title='Đồng hồ'
#wd.iconbitmap('clock.ico')
wd.wm_attributes('-topmost', True)
tlb= Label(wd,font=('Arial',50),fg='#FFFFFF',bg='#0D8A42')
tlb.pack()
dlb =Label(wd,font=('Ink Free',50),fg='#0D8A42')
dlb.pack()
show()
wd.mainloop()