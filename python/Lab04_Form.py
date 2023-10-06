import re
from tkinter import *
import tkinter.messagebox as mbox
from tkinter import ttk


date_pattern = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$"
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
def checkEmailField(email: str):
 
    if(re.fullmatch(regex, email)):
        return True
    else:
        mbox.showerror("Error","Invalid Email field")


        
def checkIDField(id):
	if len(id) != 7:
		
		mbox.showerror("Error","Invalid ID field")
	else:
		return True

def checkContactField(id):
	if len(id) != 10:
		
		mbox.showerror("Error","Invalid ID field")
	else:
		return True

def checkSemField(id):
	hk = ['1','2','3']
	for h in hk:
		if id ==h:
			return True
	mbox.showerror("Error","Invalid Sem field")
 
def is_valid_date(date_string):
    return re.match(date_pattern, date_string) is not None

if __name__ == "__main__":
	
	
	root = Tk()

	
	root.configure(background='light green')
	
	root.title("Đăng kí học phần")

	
	root.geometry("640x480")

	

	
	heading = Label(root, text="THONG TIN DANG KY HOC PHAN", bg="pink",font=('consolas','16'))
	heading.grid(row=0, column=1,columnspan=2)
	
	name = Label(root, text="Ho ten", bg="light green")
	name.grid(row=1, column=0, sticky='W')

	id = Label(root, text="MSSV", bg="light green")
	id.grid(row=2, column=0, sticky='W')
	
	dateofbirth = Label(root, text="Ngay sinh", bg="light green")
	dateofbirth.grid(row=3, column=0, sticky='W')
	
	email = Label(root, text="Email", bg="light green")
	email.grid(row=4, column=0, sticky='W')
	
	contact_no = Label(root, text="So dien thoai", bg="light green")
	contact_no.grid(row=5, column=0, sticky='W')

	sem = Label(root, text="Hoc ky", bg="light green")
	sem.grid(row=6, column=0, sticky='W')
	
	years = Label(root, text="Nam hoc", bg="light green")
	years.grid(row=7, column=0, sticky='W')

	
	
	
	name_field = Entry(root)
	name_field.grid(row=1, column=1, ipadx="100",pady=4)
 
	id_field = Entry(root)
	id_field.grid(row=2, column=1, ipadx="100",pady=4)
 
	dateofbirth_field = Entry(root)
	dateofbirth_field.grid(row=3, column=1, ipadx="100",pady=4)
	
 
	email_field = Entry(root)
	email_field.grid(row=4, column=1, ipadx="100",pady=4)
 
	contact_no_field = Entry(root)
	contact_no_field.grid(row=5, column=1, ipadx="100",pady=4)
 
 
	sem_field = Entry(root)
	sem_field.grid(row=6, column=1, ipadx="100",pady=4)
 
	years_field = ttk.Combobox(root,values=["2022-2023","2023-2024","2024-2025"])
	years_field.grid(row=7, column=1, ipadx="96",pady=4) 
	
	checkbox = Label(root,text="Chon hoc phan",bg="light green",)
	cb_python = Checkbutton(root, text="Lap trinh Python",fg="Black",bg="light gray")
	cb_pm = Checkbutton(root, text="Cong nghe phan mem",fg="Black",bg="light gray")
	cb_java = Checkbutton(root, text="Lap trinh java",fg="Black",bg="light gray")
	cb_web = Checkbutton(root, text="Phat trien ung dung web",fg="Black",bg="light gray")

	
	submit = Button(root, text="Submit", fg="Black",
							bg="light gray",command= lambda: checkSemField(sem_field.get()))
	submit.grid(row=11, column=1,pady=4)
						
	exit = Button(root, text="Exit", fg="Black",
					bg="light gray",command=lambda: root.destroy())
	exit.grid(row=11, column=2,pady=4)
	cb_python.grid(row=9, column=1,sticky='W',pady=4)
	cb_java.grid(row=9, column=2,sticky='W',pady=4)
	cb_pm.grid(row=10, column=1,sticky='W',pady=4)
	cb_web.grid(row=10, column=2,sticky='W',pady=4)
	checkbox.grid(row=8, column=0,sticky='W')
 
	
	# start the GUI
	root.mainloop()
