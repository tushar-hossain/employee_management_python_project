
from tkinter import*
from tkinter import ttk
from PIL import ImageTk, Image
import PIL
import mysql.connector
from tkinter import messagebox

class Employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x789+0+0")
        self.root.title('Employee Management System')

        # Variable
        self.var_dep=StringVar()
        self.var_name=StringVar()
        self.var_designition=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_married=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_idproofcomd=StringVar()
        self.var_idproof=StringVar()
        self.var_gender=StringVar()
        self.var_phone=StringVar()
        self.var_country=StringVar()
        self.var_salary=StringVar()


        lbl_title=Label(self.root,text='EMPLOYEE MANAGEMENT SYSTEM',font=('times new roman',15,'bold'),fg='darkblue',bg='white')
        lbl_title.place(x=0,y=0,width=1000,height=50)

        # logo
        img_logo=Image.open('image/logo.png')
        img_logo=img_logo.resize((50, 50), PIL.Image.Resampling.LANCZOS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=270,y=0,width=50,height=50)

        # image frame
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=50,width=1530,height=160)

        # 1st
        img1=Image.open('image/happy.jpg')
        img1=img1.resize((500, 120), PIL.Image.Resampling.LANCZOS)
        self.photo1=ImageTk.PhotoImage(img1)

        self.img_1=Label(img_frame,image=self.photo1)
        self.img_1.place(x=0,y=30,width=500,height=120)

        # 2nd
        img2=Image.open('image/employee.png')
        img2=img2.resize((500, 140), PIL.Image.Resampling.LANCZOS)
        self.photo2=ImageTk.PhotoImage(img2)

        self.img_2=Label(img_frame,image=self.photo2)
        self.img_2.place(x=500,y=0,width=500,height=140) 

        # Main Frame
        Main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        Main_frame.place(x=10,y=215,width=995,height=460)

        # Upper Frame
        upper_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,bg='white',text='Employee Information',font=('times new roman',12,'bold'),fg='red')
        upper_frame.place(x=10,y=10,width=975,height=220)

        # Labels and Entry fields
        lbl_dep=Label(upper_frame,text='Department',font=('arial',11,'bold'),bg='white')
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)

        # combo box
        combo_dep=ttk.Combobox(upper_frame,textvariable=self.var_dep,font=('arial',10,'bold'),width=18,state='readonly')
        combo_dep['value']=('select Department','Software Engineer','Web-Developer','HR','Manager')
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # Name
        lbl_Name=Label(upper_frame,font=('arial',10,'bold'),text='Name:',bg='white')
        lbl_Name.grid(row=0,column=2,sticky=W,padx=2,pady=7)

        txt_name=ttk.Entry(upper_frame,textvariable=self.var_name,width=20,font=('arial',10,'bold'))
        txt_name.grid(row=0,column=3,padx=2,pady=7)

        # lbl_Designition
        lbl_Designition=Label(upper_frame,font=('arial',10,'bold'),text='Designition:',bg='white')
        lbl_Designition.grid(row=1,column=0,sticky=W,padx=2,pady=7)

        txt_Designition=ttk.Entry(upper_frame,textvariable=self.var_designition,width=20,font=('arial',10,'bold'))
        txt_Designition.grid(row=1,column=1,sticky=W,padx=2,pady=7)

        # Email
        lbl_email=Label(upper_frame,font=('arial',10,'bold'),text='Email:',bg='white')
        lbl_email.grid(row=1,column=2,sticky=W,padx=2,pady=7)

        txt_email=ttk.Entry(upper_frame,textvariable=self.var_email,width=20,font=('arial',10,'bold'))
        txt_email.grid(row=1,column=3,sticky=W,padx=2,pady=7)

        # Address
        lbl_address=Label(upper_frame,font=('arial',10,'bold'),text='Address:',bg='white')
        lbl_address.grid(row=2,column=0,sticky=W,padx=2,pady=7)

        txt_address=ttk.Entry(upper_frame,textvariable=self.var_address,width=20,font=('arial',10,'bold'))
        txt_address.grid(row=2,column=1,sticky=W,padx=2,pady=7)

        # Married 
        lbl_married_status=Label(upper_frame,font=('arial',11,'bold'),text='Married Status:',bg='white')
        lbl_married_status.grid(row=2,column=2,padx=2,pady=7,sticky=W)
        
        # combo box
        com_txt_married=ttk.Combobox(upper_frame,textvariable=self.var_married,font=('arial',10,'bold'),width=18,state='readonly')
        com_txt_married['value']=('Married','Un-married')
        com_txt_married.current(0)
        com_txt_married.grid(row=2,column=3,padx=2,pady=7,sticky=W)

        # Dob
        lbl_dob=Label(upper_frame,font=('arial',10,'bold'),text='DOB:',bg='white')
        lbl_dob.grid(row=3,column=0,sticky=W,padx=2,pady=7)

        txt_dob=ttk.Entry(upper_frame,textvariable=self.var_dob,width=20,font=('arial',10,'bold'))
        txt_dob.grid(row=3,column=1,sticky=W,padx=2,pady=7)

        # Doj
        lbl_doj=Label(upper_frame,font=('arial',10,'bold'),text='DOJ:',bg='white')
        lbl_doj.grid(row=3,column=2,sticky=W,padx=2,pady=7)

        txt_doj=ttk.Entry(upper_frame,textvariable=self.var_doj,width=20,font=('arial',10,'bold'))
        txt_doj.grid(row=3,column=3,sticky=W,padx=2,pady=7)

        # Id proof               
        # combo box
        com_txt_proof=ttk.Combobox(upper_frame,textvariable=self.var_idproofcomd,font=('arial',10,'bold'),width=18,state='readonly')
        com_txt_proof['value']=('Select ID Proof','NID Card','Passport')
        com_txt_proof.current(0)
        com_txt_proof.grid(row=4,column=0,padx=2,pady=7,sticky=W)

        txt_proof=ttk.Entry(upper_frame,textvariable=self.var_idproof,width=18,font=('arial',10,'bold'))
        txt_proof.grid(row=4,column=1,padx=2,pady=7)

        # Gender 
        lbl_gender=Label(upper_frame,font=('arial',11,'bold'),text='Gender:',bg='white')
        lbl_gender.grid(row=4,column=2,padx=2,pady=7,sticky=W)
        
        # combo box
        com_txt_gender=ttk.Combobox(upper_frame,textvariable=self.var_gender,font=('arial',10,'bold'),width=18,state='readonly')
        com_txt_gender['value']=('Male','Female')
        com_txt_gender.current(0)
        com_txt_gender.grid(row=4,column=3,padx=2,pady=7,sticky=W)

        # Phone
        lbl_phone=Label(upper_frame,font=('arial',10,'bold'),text='Phone No:',bg='white')
        lbl_phone.grid(row=0,column=4,sticky=W,padx=2,pady=7)

        txt_phone=ttk.Entry(upper_frame,textvariable=self.var_phone,width=20,font=('arial',10,'bold'))
        txt_phone.grid(row=0,column=5,sticky=W,padx=2,pady=7)

        # country
        lbl_country=Label(upper_frame,font=('arial',10,'bold'),text='Country:',bg='white')
        lbl_country.grid(row=1,column=4,sticky=W,padx=2,pady=7)

        txt_country=ttk.Entry(upper_frame,textvariable=self.var_country,width=20,font=('arial',10,'bold'))
        txt_country.grid(row=1,column=5,sticky=W,padx=2,pady=7)

        # ctc
        lbl_doj=Label(upper_frame,font=('arial',10,'bold'),text='Salary(CTC):',bg='white')
        lbl_doj.grid(row=2,column=4,sticky=W,padx=2,pady=7)

        txt_ctc=ttk.Entry(upper_frame,textvariable=self.var_salary,width=20,font=('arial',10,'bold'))
        txt_ctc.grid(row=2,column=5,sticky=W,padx=2,pady=7)

        # button frame
        button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=820,y=10,width=150,height=133)

        btn_add=Button(button_frame,text='Save',command=self.add_data,font=('arial',10,'bold'),width=20,bg='blue',fg='white')
        btn_add.grid(row=0,column=0,padx=1,pady=2)

        btn_update=Button(button_frame,command=self.update_date,text='Update',font=('arial',10,'bold'),width=20,bg='blue',fg='white')
        btn_update.grid(row=1,column=0,padx=1,pady=2)
        
        btn_delete=Button(button_frame,command=self.delete_data,text='Delete',font=('arial',10,'bold'),width=20,bg='blue',fg='white')
        btn_delete.grid(row=2,column=0,padx=1,pady=2)

        btn_clear=Button(button_frame,command=self.reset_data,text='Clear',font=('arial',10,'bold'),width=20,bg='blue',fg='white')
        btn_clear.grid(row=3,column=0,padx=1,pady=2)


        # Down Frame
        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,bg='white',text='Employee Information Table',font=('times new roman',12,'bold'),fg='red')
        down_frame.place(x=10,y=230,width=975,height=220)

        # search frame
        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,bg='white',text='Search Employee Information',font=('times new roman',12,'bold'),fg='black')
        search_frame.place(x=0,y=0,width=970,height=60)

        # search text
        search_by=Label(search_frame,font=('arial',10,'bold'),text='Search By',fg='white',bg='red')
        search_by.grid(row=0,column=0,padx=5,sticky=W)

        # search
        self.var_com_search=StringVar()
        com_text_search=ttk.Combobox(search_frame,textvariable=self.var_com_search,state='readonly',font=('arial',11,'bold'),width=18)
        com_text_search['value']=('Select Option','phone','id_proof')
        com_text_search.current(0)
        com_text_search.grid(row=0,column=1,padx=5)

        self.var_search=StringVar()
        txt_search=ttk.Entry(search_frame,textvariable=self.var_search,width=18,font=('arial',11,'bold'))
        txt_search.grid(row=0,column=2,padx=5)

        btn_search=Button(search_frame,command=self.search_data,text='Search',font=('arial',11,'bold'),width=14,bg='blue',fg='white')
        btn_search.grid(row=0,column=3,padx=5)

        btn_showAll=Button(search_frame,command=self.fetch_data,text='Show All',font=('arial',11,'bold'),width=14,bg='blue',fg='white')
        btn_showAll.grid(row=0,column=4,padx=5)

        # mask image
        img_logo=Image.open('image/mask.jpg')
        img_logo=img_logo.resize((50, 50), PIL.Image.Resampling.LANCZOS)
        self.photo_mask_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(search_frame,image=self.photo_mask_logo)
        self.logo.place(x=730,y=0,width=60,height=38)


        # ==========Employee Table===========

        # Table Frame
        table_frame=Frame(down_frame,bd=3,relief=RIDGE)
        table_frame.place(x=0,y=70,width=970,height=125)

        # scrool bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)

        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.employee_table=ttk.Treeview(table_frame,column=('dep','name','degi','email','address','married','dob','doj','idproofcomb','idproof','gender','phone','country','salary',),xscrollcommand=scroll_x,yscrollcommand=scroll_y)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading('dep',text='Department')
        self.employee_table.heading('name',text='Name')
        self.employee_table.heading('degi',text='Degignition')
        self.employee_table.heading('email',text='Email')
        self.employee_table.heading('address',text='Address')
        self.employee_table.heading('married',text='Married Status')
        self.employee_table.heading('dob',text='DOB')
        self.employee_table.heading('doj',text='DOJ')
        self.employee_table.heading('idproofcomb',text='ID Type')
        self.employee_table.heading('idproof',text='ID Proof')
        self.employee_table.heading('gender',text='Gender')
        self.employee_table.heading('phone',text='Phone')
        self.employee_table.heading('country',text='Country')
        self.employee_table.heading('salary',text='Salary')

        self.employee_table['show']='headings'

        self.employee_table.column('dep',width=100)
        self.employee_table.column('name',width=100)
        self.employee_table.column('degi',width=100)
        self.employee_table.column('email',width=100)
        self.employee_table.column('address',width=100)
        self.employee_table.column('married',width=100)
        self.employee_table.column('dob',width=100)
        self.employee_table.column('doj',width=100)
        self.employee_table.column('idproofcomb',width=100)
        self.employee_table.column('idproof',width=100)
        self.employee_table.column('gender',width=100)
        self.employee_table.column('phone',width=100)
        self.employee_table.column('country',width=100)
        self.employee_table.column('salary',width=100)

        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.bind('<ButtonRelease>',self.get_cursor)
        self.fetch_data()
    
    # ********function declaration********

    def add_data(self):
        if self.var_dep.get=="" or self.var_email.get()=="":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='123456789',database='mydata')
                my_curser=conn.cursor()
                my_curser.execute('insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(

                                    self.var_dep.get(),
                                    self.var_name.get(),
                                    self.var_designition.get(),
                                    self.var_email.get(),
                                    self.var_address.get(),
                                    self.var_married.get(),
                                    self.var_dob.get(),
                                    self.var_doj.get(),
                                    self.var_idproofcomd.get(),
                                    self.var_idproof.get(),
                                    self.var_gender.get(),
                                    self.var_phone.get(),
                                    self.var_country.get(),
                                    self.var_salary.get()
                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('success','Employee has been added',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)
    
    # fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='123456789',database='mydata')
        my_curser=conn.cursor()
        my_curser.execute('select * from employee')
        data=my_curser.fetchall()
        if len(data)!=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert('',END,values=i)
            conn.commit()
            conn.close()

    # get cursor
    def get_cursor(self,event=''):
        cursor_row=self.employee_table.focus()
        content=self.employee_table.item(cursor_row)
        data=content['values']


        self.var_dep.set(data[0])
        self.var_name.set(data[1])
        self.var_designition.set(data[2])
        self.var_email.set(data[3])
        self.var_address.set(data[4])
        self.var_married.set(data[5])
        self.var_dob.set(data[6])
        self.var_doj.set(data[7])
        self.var_idproofcomd.set(data[8])
        self.var_idproof.set(data[9])
        self.var_gender.set(data[10])
        self.var_phone.set(data[11])
        self.var_country.set(data[12])
        self.var_salary.set(data[13])
    
    # Update button
        
    def update_date(self):
        if self.var_dep.get=="" or self.var_email.get()=="":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                update=messagebox.askyesno('Update','Are you sure update this employee data')

                if update>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='123456789',database='mydata')
                    my_curser=conn.cursor()
                    my_curser.execute('update employee set Department=%s,Name=%s,Designition=%s,Email=%s,Address=%s,Married_status=%s,DOB=%s,DOJ=%s,id_proof_type=%s,Gender=%s,Phone=%s,Country=%s,Salary=%s where id_proof=%s',(
                                    self.var_dep.get(),
                                    self.var_name.get(),
                                    self.var_designition.get(),
                                    self.var_email.get(),
                                    self.var_address.get(),
                                    self.var_married.get(),
                                    self.var_dob.get(),
                                    self.var_doj.get(),
                                    self.var_idproofcomd.get(),
                                    self.var_gender.get(),
                                    self.var_phone.get(),
                                    self.var_country.get(),
                                    self.var_salary.get(),
                                    self.var_idproof.get(),

                                ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('success','Employee Successfully update',parent=self.root)

            except Exception as es:
                messagebox.showerror('Error',f'Due to:{str(es)}',parent=self.root)


    # delete button
                
    def delete_data(self):
        if self.var_idproof.get()=="":
            messagebox.showerror('Error','All fields are required')
        else:
            try:
                Delete=messagebox.askyesno('Delete','Are you sure delete this employee',parent=self.root)
                if Delete>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='123456789',database='mydata')
                    my_curser=conn.cursor()
                    sql='delete from employee where id_proof=%s'
                    value=(self.var_idproof.get(),)
                    my_curser.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Delete','Employee Successfully Delete',parent=self.root)

            except Exception as es:
                messagebox.showerror('Error',f'Due to:{str(es)}',parent=self.root)
            


    # clear button
    def reset_data(self):
        self.var_dep.set('Select Department')
        self.var_name.set('')
        self.var_designition.set('')
        self.var_email.set('')
        self.var_address.set('')
        self.var_married.set('Married')
        self.var_dob.set('')
        self.var_doj.set('')
        self.var_idproofcomd.set('Select ID Proof')
        self.var_idproof.set('')
        self.var_gender.set('')
        self.var_phone.set('')
        self.var_country.set('')
        self.var_salary.set('')


    # Search 
    def search_data(self):
        if self.var_com_search.get()=='' or self.var_search.get()=='':
            messagebox.showerror('Error','Please select option')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='123456789',database='mydata')
                my_curser=conn.cursor()
                my_curser.execute('select * from employee where ' +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get()+"%'"))
                rows=my_curser.fetchall()
                if len(rows)!=0:
                    self.employee_table.delete(*self.employee_table.get_children())
                    for i in rows:
                        self.employee_table.insert("",END,values=i)
                conn.commit
                conn.close()
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)



if __name__=="__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()