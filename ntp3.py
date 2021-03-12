from tkinter import *
from time import *
m=time()
root=Tk(className='Ntp3')
def b1s():
    root.quit()
    print('病毒注入成功！')
b1=Button(root,text='点我有惊喜',fg='green',command=b1s)
def b2s():
    root2=Tk(className='第二窗口')
    def b3s():
        root.quit()
        print('病毒注入成功！')
    b3=Button(root2,text='退出',fg='green',command=b3s)
    b3.pack()
b2=Button(root,text='进入新界面',fg='pink',command=b2s)
ls1=Label(root,text='欢迎您使用npt3')
ls1.pack()
b1.pack()
b2.pack()
root.mainloop()