from tkinter import*

plus_var1=0
minus_var1=0
mul_var1=0
div_var1=0
clear_var1=0
function_name=0

root=Tk()
root.title("Real Calculator")
root.geometry("300x450")

main_label=Label(root,text="Input : ")    
main_label.grid(row=0,column=0)

entry1=Entry(root,width=35)
entry1.grid(row=0,column=1,columnspan=4)




def buttonpressed_add(input_number):
    global function_name
    global plus_var1
    global minus_var1
    global mul_var1
    global div_var1
    global clear_var1
    first_number=entry1.get()
    entry1.delete(0,END)
    
    if (input_number=="plus"):
        plus_var1=first_number
        text_box.insert(END,str(plus_var1) + "+")
        function_name="plus"

    elif (input_number=="minus"):
        minus_var1=first_number
        text_box.insert(END,str(minus_var1) + "-")
        function_name="minus"

    elif (input_number=="mul"):
        mul_var1=first_number
        text_box.insert(END,str(mul_var1) + "x")
        function_name="mul"
    
    elif (input_number=="div"):
        div_var1=first_number
        text_box.insert(END,str(div_var1) + "/")
        function_name="div"
    
    elif (input_number=="clear"):
        entry1.delete(0,END)
        text_box.delete(1.0,END)
        
 

    elif (input_number=="equal"):
        if(function_name=="plus"):
            plus_var2=first_number
            entry1.delete(0,END)
            total=int(plus_var1)+int(plus_var2)
            string_1=str(plus_var1) + "+" + str(plus_var2) + "=" + str(total)
            text_box.delete(1.0,END)
            text_box.insert(END,string_1)
        if (function_name=="minus"):
            minus_var2=first_number
            entry1.delete(0,END)
            total=int(minus_var1)-int(minus_var2)
            string_1=str(minus_var1) + "-" + str(minus_var2) + "=" + str(total)
            text_box.delete(1.0,END)
            text_box.insert(END,string_1)
        

        if (function_name=="mul"):
            mul_var2=first_number
            entry1.delete(0,END)
            total=int(mul_var1)*int(mul_var2)
            string_1=str(mul_var1) + "x" + str(mul_var2) + "=" + str(total)
            text_box.delete(1.0,END)
            text_box.insert(END,string_1)
        if (function_name=="div"):
            div_var2=first_number
            entry1.delete(0,END)
            total=int(div_var1)/int(div_var2)
            string_1=str(div_var1) + "/" + str(div_var2) + "=" + str(total)
            text_box.delete(1.0,END)
            text_box.insert(END,string_1)
        
        

        

    
    
    else:
        second_number=str(first_number) + str(input_number)
        entry1.insert(0,second_number)

    


button_7=Button(root,text="7",padx=20,pady=20,command=lambda: buttonpressed_add(7))
button_8=Button(root,text="8",padx=20,pady=20,command=lambda: buttonpressed_add(8))
button_9=Button(root,text="9",padx=20,pady=20,command=lambda: buttonpressed_add(9))
button_div=Button(root,text="/",padx=20,pady=20,command=lambda: buttonpressed_add("div"))

button_4=Button(root,text="4",padx=20,pady=20,command=lambda: buttonpressed_add(4))
button_5=Button(root,text="5",padx=20,pady=20,command=lambda: buttonpressed_add(5))
button_6=Button(root,text="6",padx=20,pady=20,command=lambda: buttonpressed_add(6))
button_plus=Button(root,text="+",padx=20,pady=20,command=lambda: buttonpressed_add("plus"))

button_1=Button(root,text="1",padx=20,pady=20,command=lambda: buttonpressed_add(1))
button_2=Button(root,text="2",padx=20,pady=20,command=lambda: buttonpressed_add(2))
button_3=Button(root,text="3",padx=20,pady=20,command=lambda: buttonpressed_add(3))
button_sub=Button(root,text="-",padx=20,pady=20,command=lambda: buttonpressed_add("minus"))

button_zero=Button(root,text="0",padx=20,pady=20,command=lambda: buttonpressed_add(0))
button_equal=Button(root,text="=",padx=20,pady=20,command=lambda: buttonpressed_add("equal"))
button_clear=Button(root,text="C",padx=20,pady=20,command=lambda: buttonpressed_add("clear"))
button_mul=Button(root,text="X",padx=20,pady=20,command=lambda: buttonpressed_add("mul"))





button_7.grid(row=1,column=1)
button_8.grid(row=1,column=2)
button_9.grid(row=1,column=3)
button_div.grid(row=1,column=4)

button_4.grid(row=2,column=1)
button_5.grid(row=2,column=2)
button_6.grid(row=2,column=3)
button_plus.grid(row=2,column=4)

button_1.grid(row=3,column=1)
button_2.grid(row=3,column=2)
button_3.grid(row=3,column=3)
button_sub.grid(row=3,column=4)

button_zero.grid(row=4,column=1)
button_equal.grid(row=4,column=2)
button_clear.grid(row=4,column=3)
button_mul.grid(row=4,column=4)


main_label2=Label(root,text="Output : ")    
main_label2.grid(row=5,column=0)

text_box=Text(root,width=25,height=8)
text_box.grid(row=5,column=1,columnspan=4)


root.mainloop()