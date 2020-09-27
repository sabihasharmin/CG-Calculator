from tkinter import*

def btnClick(numbers):
    global operator
    operator=operator+str(numbers)
    text_Input.set(operator)
def btncgpaInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=''
def btnClearDisplay():
    global operator
    operator=''
    text_Input.set('')
def btnEqualsInput():
    global operator
    result = str(eval(operator))
    text_Input.set(result)
    operator = result

cal=Tk()
cal.title('CGPA calculator for 7th semester')
operator=''
text_Input=StringVar()
txtDisplay=Entry(cal,font=('arial',20,'bold'),textvariable=text_Input,bd=20,insertwidth=4,
                 bg='powder blue',justify='right').grid(columnspan=10)
subject1=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),
            text='Hum 4721',command=lambda:btnClick("3")).grid(row=1,column=0)
subject2=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),
            text='EEE 4700',command=lambda:btnClick("+3")).grid(row=1,column=1)
subject3=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),
            text='EEE 4701',command=lambda:btnClick("+3")).grid(row=1,column=2)
subject4=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),
            text='EEE 4702',command=lambda:btnClick("+.75")).grid(row=1,column=3)
subject5=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),
            text='EEE 4703',command=lambda:btnClick("+3")).grid(row=2,column=0)
subject6=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),
            text='EEE 4704 ',command=lambda:btnClick("+.75")).grid(row=2,column=1)
subject7=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),
            text='EEE 4705',command=lambda:btnClick("+3")).grid(row=2,column=2)
subject8=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),
            text='EEE 4705',command=lambda:btnClick("+.75")).grid(row=2,column=3)
subject9=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),
            text='EEE 4790',command=lambda:btnClick("+1")).grid(row=3,column=0)
subject10=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),
            text='Elec.with lab',command=lambda:btnClick("+3.75")).grid(row=3,column=1)
subject11=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),
            text='Elec.without lab',command=lambda:btnClick("+3")).grid(row=3,column=2)

nxt=Button(cal,padx=16,bd=8,fg='green',font=('arial',20,'bold'),
            text='NEXT',command=lambda:btnEqualsInput()).grid(row=4,column=1)
done=Button(cal,padx=16,bd=8,fg='blue',font=('arial',20,'bold'),
            text='done',command=lambda:btnEqualsInput()).grid(row=7,column=3)
btn7=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),
            text='A+',command=lambda:btnClick("*4.00")).grid(row=5,column=0)
btn8=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),
            text='A',command=lambda:btnClick("*3.75")).grid(row=5,column=1)
btn9=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),
            text='A-',command=lambda:btnClick("*3.50")).grid(row=5,column=2)


#=====================================================================
btn4=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),
            text='B+',command=lambda:btnClick("*3.25")).grid(row=5,column=3)
btn5=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),
            text='B',command=lambda:btnClick("*3.00")).grid(row=6,column=0)
btn6=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),
            text='B-',command=lambda:btnClick("*2.75")).grid(row=6,column=1)

#====================================================================
btn1=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),
            text='C+',command=lambda:btnClick("*2.50")).grid(row=6,column=2)
btn2=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),
            text='C',command=lambda:btnClick("*2.25")).grid(row=6,column=3)
btn3=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),
            text='D',command=lambda:btnClick("*2.00")).grid(row=7,column=0)
addition=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),
            text='F',command=lambda:btnClick("*0.00")).grid(row=7,column=1)
#===========================================================================
add=Button(cal,padx=16,bd=8,fg='maroon',font=('arial',20,'bold'),
            text='GPA',command=lambda:btnClick("/25")).grid(row=7,column=2)
add=Button(cal,padx=16,bd=8,fg='red',font=('arial',20,'bold'),
            text='CE',command=btnClearDisplay).grid(row=4,column=3)
add=Button(cal,padx=16,bd=8,fg='red',font=('arial',20,'bold'),
            text='END',command=lambda:btnEqualsInput()).grid(row=4,column=2)
cal.mainloop()

