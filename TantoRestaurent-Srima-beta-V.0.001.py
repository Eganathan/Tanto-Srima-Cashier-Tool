from tkinter import *

total = 0
pre_total = []
saletotal = 0
#=========================Events
def add_ev(event):
	x = float(current_Price_str.get())
	global total
	global pre_total

	total += x
	total_int.set(round(total))
	current_Price_str.set("")
	note_str.set(str(round(x))+" Sucessfully added!")

def calculate_ev(event):
        global total
        global saletotal
        global pre_total
        y = total
        gst= (y/100)*5
        withGST = gst + y
        saletotal += withGST
        total_with_Gst_str.set(str(round(withGST)))

        av_off = (y/100)*20
        av_price = y - av_off
        av_Price_str.set(str(av_price))
        note_str.set(" Sucessfully Calculated! "+ "Today's Sale: " +str(round(saletotal)))


        pre_total.insert(0,str(round(withGST)))
        print(pre_total)
        pass

def sub_ev(event):
        x = float(current_Price_str.get())
        global total
        total -=x
        total_int.set(round(total))
        current_Price_str.set("")
        note_str.set(str(round(x))+" Sucessfully Subtracted!")
        pass
def reset_ev(event):
        current_Price_str.set("")
        total_int.set("")
        total_with_Gst_str.set("")
        av_Price_str.set("")
        global total
        total = 0
        init()
        note_str.set(" Sucessfully Reset! ")
        pass
#=============================END of Events
def init():
        total_int.set("0")
        total_with_Gst_str.set("0")
        av_Price_str.set("0")
        note_str.set("Created by Eknath")
        pass
    
def short_tp():
    top = Toplevel()
    top.title("The Short Cut")
    msg = Message(top, text="Enter: Adding Item Price \n Ctrl+ - : for Reducing the Amount \n Ctrl+ Shift + +: Add \n Crl+r : Reset")
    msg.pack()

    button = Button(top, text="Dismiss", command=top.destroy)
    button.pack()
    pass

def add():
	x = float(current_Price_str.get())
	global total
	total += x
	total_int.set(round(total))
	current_Price_str.set("")
	note_str.set(str(round(x))+" Sucessfully added!")
	pass
def sub():
        x = float(current_Price_str.get())
        global total
        total -=x
        total_int.set(round(total))
        current_Price_str.set("")
        note_str.set(str(round(x))+" Sucessfully Subtracted!")
        pass

def calculate():
        global total
        global saletotal
        y = total
        gst= (y/100)*5
        withGST = gst + y
        total_with_Gst_str.set(str(round(withGST)))

        av_off = (y/100)*20
        av_price = y - av_off
        av_Price_str.set(str(av_price))
        saletotal += withGST
        note_str.set(" Sucessfully Calculated! " + "Today's Sale: " +str(round(saletotal)))
        pass
def reset():
        current_Price_str.set("")
        total_int.set("")
        total_with_Gst_str.set("")
        av_Price_str.set("")
        global total
        total = 0
        init()
        note_str.set("Reset Sucessfull! ")
        pass
#==============test
def quitm():
        r.destroy()
        pass
#===============

r = Tk()
r.title("Tanto -Cashier Tool V0.001 beta-V 0.01")
r.geometry("400x250")
r.wm_iconbitmap('tantoapp.ico')

#=====================================String Variables
current_Price_str = StringVar()
total_int = StringVar()
total_with_Gst_str = StringVar()
av_Price_str = StringVar()
note_str = StringVar()
#=====================================End String Variables

#=======================FileMenu
menubar = Menu(r)
menubar.add_command(label="Short-Cut",command=short_tp)
menubar.add_command(label="Quit!",command=quitm)
r.config(menu=menubar)
#=======================

f= Frame(r,relief=FLAT,bd=0)

lblh1 = Label(r,text="Tanto Srima-Cashier Tool ",font=("Helvetica", "20","bold"),fg="forestgreen",bg="white").pack(fill=X)

#====Current Price===============
entry_currentPrice_lbl = Label(f,text="Current Item Price : ",bd=0).grid(row="1",column="0",sticky="nsew")
entry_currentPrice_entry = Entry(f,textvariable=current_Price_str,takefocus="Takefocus",font=("Helvetica", "12")).grid(row="1",column="1")
#add button for current price
current_add_btn = Button(f,text="+",command=add ,width="5",height="1").grid(row="1",column="2")
current_sub_btn = Button(f,text="-",command=sub,width="5",height="1").grid(row="1",column="3",sticky="ns")
#=====================Total Price
total_Price_lbl = Label(f,text="Total Price : ").grid(row="2",column="0",sticky="E")
entry_totalPrice_label = Label(f,textvariable=total_int,font=("Helvetica", "20")).grid(row="2",column="1")
total_add_btn = Button(f,text="Calculate",command=calculate,).grid(row="2",column="2",sticky="EWNS",columnspan="2",rowspan="2")
#========== price with GST
total_Price_with_GST_lbl = Label(f,text="Grand Total",bg="green",font=("Helvetica", "12"),width="10").grid(row="3",column="0",sticky="EWNS")
total_Price_with_GST_entry = Label(f,textvariable=total_with_Gst_str,font=("Helvetica", "20","bold")).grid(row="4",column="0",sticky="E")

total_Price_Av = Label(f,text="Aurovillie Amount",bg="orange",font=("Helvetica", "12")).grid(row="3",column="1",sticky="E")
total_Price_Av_lable = Label(f,textvariable=av_Price_str,font=("Helvetica", "20","bold"),fg="orange").grid(row="4",column="1",sticky="E")

#=============Note
warning_lbl = Label(f,textvariable=note_str,bg="lightgreen",width="54").grid(row="5",column="0",columnspan="5")
#====================reset Button
reset_btn = Button(f,text="Reset",command=reset,width="10").grid(row="4",column="2",sticky="nswe",columnspan="2")
#=============Event Button
r.bind("<Return>",add_ev)
r.bind("<Control-plus>",add_ev)
r.bind("<Control-Return>",calculate_ev)
r.bind("<Control-minus>",sub_ev)
r.bind("<Control-r>",reset_ev)
#binding event======

#packing the Frame
f.pack()


init()
r.mainloop()
