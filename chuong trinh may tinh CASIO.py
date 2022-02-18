from tkinter import *
from playsound import playsound
def btnClick(numbers):
    global operator
   
    operator=operator+str(numbers)
    nhapvao.set(operator)
def btnClear():
    global operator
  
    operator=""
    nhapvao.set("")
def daubang():
    global operator
    result=str(eval(operator))
    nhapvao.set(result)

cal=Tk() # Tạo cửa sổ
cal.title("MÁY TÍNH CASIO") # Tạo tiêu đề cho cửa sổ
operator=""
nhapvao=StringVar() # Nội dung hiển thị trên máy tính
hienthi=Entry(cal,width=30,font=('arial',20,'bold'),textvariable=nhapvao,bd=30,insertwidth=4,bg='light green',justify='right').grid(columnspan=4)
so7=Button(cal,padx=30,bd=8,fg="black",font=('arial',20,'bold'),text="7",command=lambda:btnClick(7),bg="silver").grid(row=1,column=0)
so8=Button(cal,padx=30,bd=8,fg="black",font=('arial',20,'bold'),text="8",command=lambda:btnClick(8),bg="silver").grid(row=1,column=1)
so9=Button(cal,padx=30,bd=8,fg="black",font=('arial',20,'bold'),text="9",command=lambda:btnClick(9),bg="silver").grid(row=1,column=2)
chia=Button(cal,padx=30,bd=8,fg="black",font=('arial',20,'bold'),text="/",command=lambda:btnClick("/"),bg="silver").grid(row=1,column=3)
#-------------------------------------------------------------------------------------------------------------------------------
so4=Button(cal,padx=30,bd=8,fg="black",font=('arial',20,'bold'),text="4",command=lambda:btnClick(4),bg="silver").grid(row=2,column=0)
so5=Button(cal,padx=30,bd=8,fg="black",font=('arial',20,'bold'),text="5",command=lambda:btnClick(5),bg="silver").grid(row=2,column=1)
so6=Button(cal,padx=30,bd=8,fg="black",font=('arial',20,'bold'),text="6",command=lambda:btnClick(6),bg="silver").grid(row=2,column=2)
nhan=Button(cal,padx=30,bd=8,fg="black",font=('arial',20,'bold'),text="*",command=lambda:btnClick("*"),bg="silver").grid(row=2,column=3)
#------------------------------------------------------------------------------------------------------------------------------
so1=Button(cal,padx=30,bd=8,fg="black",font=('arial',20,'bold'),text="1",command=lambda:btnClick(1),bg="silver").grid(row=3,column=0)
so2=Button(cal,padx=30,bd=8,fg="black",font=('arial',20,'bold'),text="2",command=lambda:btnClick(2),bg="silver").grid(row=3,column=1)
so3=Button(cal,padx=30,bd=8,fg="black",font=('arial',20,'bold'),text="3",command=lambda:btnClick(3),bg="silver").grid(row=3,column=2)
tru=Button(cal,padx=30,bd=8,fg="black",font=('arial',20,'bold'),text="-",command=lambda:btnClick("-"),bg="silver").grid(row=3,column=3)
#------------------------------------------------------------------------------------------------------------------------------
xoa=Button(cal,padx=30,bd=8,fg="black",font=('arial',20,'bold'),text="C",command=btnClear,bg="silver").grid(row=4,column=0)
phay=Button(cal,padx=30,bd=8,fg="black",font=('arial',20,'bold'),text=".",command=lambda:btnClick("."),bg="silver").grid(row=4,column=1)
so0=Button(cal,padx=30,bd=8,fg="black",font=('arial',20,'bold'),text="0",command=lambda:btnClick(0),bg="silver").grid(row=4,column=2)
cong=Button(cal,padx=30,bd=8,fg="black",font=('arial',20,'bold'),text="+",command=lambda:btnClick("+"),bg="silver").grid(row=4,column=3)
#-------------------------------------------------------------------------------------------------------------
ngoacmo=Button(cal,padx=30,bd=8,fg="black",font=('arial',20,'bold'),text="(",command=lambda:btnClick("("),bg="silver").grid(row=5,column=0)
ngoacdong=Button(cal,padx=30,bd=8,fg="black",font=('arial',20,'bold'),text=")",command=lambda:btnClick(")"),bg="silver").grid(row=5,column=1)
bang=Button(cal,padx=100,bd=8,fg="black",font=('arial',20,'bold'),text="=",command=daubang,bg="silver").grid(row=5,column=2,columnspan=2)


cal.mainloop()