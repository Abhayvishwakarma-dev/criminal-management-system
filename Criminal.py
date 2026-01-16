from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox


class Criminal:
    def __init__(self,root): 
        self.root=root
        self.root.geometry('1530x790+0+0')
        self.root.title("CRIMINAL MANAGEMENT SYSTEM")

        # variables
        self.var_case_id=StringVar()
        self.var_criminal_no=StringVar()
        self.var_name=StringVar()
        self.var_nickname=StringVar()
        self.var_arrest=StringVar()
        self.var_date_of_crime=StringVar()
        self.var_address=StringVar()
        self.var_age=StringVar()
        self.var_occupation=StringVar()
        self.var_birthMark=StringVar()
        self.var_crime_type=StringVar()
        self.var_father_name=StringVar()
        self.var_gender=StringVar()
        self.var_wanted=StringVar()
        self.var_Criminal_name=StringVar()


        # ncr logo
        lbl_title=Label(self.root,text="CRIMINAL MANAGEMENT SYSTEM SOFTWARE" ,font=('times new roman',35, "bold"),bg="black",fg='gold')
        lbl_title.place(x=0,y=0,width=1530,height=60)
        img_logo=Image.open('logo.png')
        img_logo=img_logo.resize((60,60),Image.Resampling.LANCZOS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=100,y=5,width=60,height=50)

        # Img_Frame
        img_frame=Label(self.root,bd=2,relief=RIDGE,bg="white")
        img_frame.place(x=0,y=60,width=1530,height=130)

        #frist img
        #Resampling.LANCZOS means--reduce the number of pixel and 	Resize with high quality
        img1=Image.open('first.png')
        img1=img1.resize((480,160),Image.Resampling.LANCZOS)
        self.photo1=ImageTk.PhotoImage(img1)

        self.img_1=Label(img_frame,image=self.photo1)
        self.img_1.place(x=0,y=0,width=480,height=160)

        # second img
        img2=Image.open('second.png')
        img2=img2.resize((480,160),Image.Resampling.LANCZOS)
        self.photo2=ImageTk.PhotoImage(img2)

        self.img_2=Label(img_frame,image=self.photo2)
        self.img_2.place(x=480,y=0,width=480,height=160)

        # third img.
        img3=Image.open('third.png')
        img3=img3.resize((480,160),Image.Resampling.LANCZOS)
        self.photo3=ImageTk.PhotoImage(img3)

        self.img_3=Label(img_frame,image=self.photo3)
        self.img_3.place(x=960,y=0,width=480,height=160)

        # main frame
        main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        main_frame.place(x=10,y=190,width=1340,height=560)

        #upper Frame
        upper_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="CRIMINAL INFORMATION " ,font=('times new roman',11, "bold"),fg='red',bg='white')
        upper_frame.place(x=10,y=10,width=1300,height=240)

        # Labels Entry

        # Case id
        caseid=Label(upper_frame,text='Case ID:',font=('ariel',11, "bold"),bg='white')
        caseid.grid(row=0,column=0,padx=2,sticky=W)

        caseentry=ttk.Entry(upper_frame,textvariable=self.var_case_id,width=22,font=('ariel',11, "bold"))
        caseentry.grid(row=0,column=1,padx=2,sticky=W)
        
        # Criminal no.
        lbl_criminal_no=Label(upper_frame,text='Criminal No:',font=('ariel',11, "bold"),bg='white')
        lbl_criminal_no.grid(row=0,column=2,sticky=W,padx=2,pady=7)

        txt_criminal_no=ttk.Entry(upper_frame,textvariable=self.var_criminal_no,width=22,font=('ariel',11, "bold"))
        txt_criminal_no.grid(row=0,column=3,padx=2,sticky=W,pady=7)

        # Criminal Name
        lbl_Name=Label(upper_frame,text='Criminal Name:',font=('ariel',11, "bold"),bg='white')
        lbl_Name.grid(row=1,column=0,padx=2,sticky=W,pady=7)

        txt_Name=ttk.Entry(upper_frame,textvariable=self.var_Criminal_name,width=22,font=('ariel',11, "bold"))
        txt_Name.grid(row=1,column=1,padx=2,sticky=W,pady=7)

        #Nick Name
        lbl_nickname=Label(upper_frame,text='NickName:',font=('ariel',11, "bold"),bg='white')
        lbl_nickname.grid(row=1,column=2,padx=2,sticky=W,pady=7)

        txt_nickname=ttk.Entry(upper_frame,textvariable=self.var_nickname ,width=22,font=('ariel',11, "bold"))
        txt_nickname.grid(row=1,column=3,padx=2,sticky=W,pady=7)

        # Arrest Date
        lbl_arrestDate=Label(upper_frame,text='Arrest Date:',font=('ariel',11, "bold"),bg='white')
        lbl_arrestDate.grid(row=2,column=0,padx=2,sticky=W,pady=7)

        txt_arrestDate=ttk.Entry(upper_frame,textvariable=self.var_arrest,width=22,font=('ariel',11, "bold"))
        txt_arrestDate.grid(row=2,column=1,padx=2,sticky=W,pady=7)

        #Date of crime
        lbl_dateofcrime=Label(upper_frame,text='Date of Crime:',font=('ariel',11, "bold"),bg='white')
        lbl_dateofcrime.grid(row=2,column=2,padx=2,sticky=W,pady=7)

        txt_crimeofdate=ttk.Entry(upper_frame,textvariable=self.var_date_of_crime,width=22,font=('ariel',11, "bold"))
        txt_crimeofdate.grid(row=2,column=3,padx=2,sticky=W,pady=7)

        #Address
        lbl_address=Label(upper_frame,text='Address:',font=('ariel',11, "bold"),bg='white')
        lbl_address.grid(row=3,column=0,padx=2,sticky=W ,pady=7)

        txt_address=ttk.Entry(upper_frame,textvariable=self.var_address,width=22,font=('ariel',11, "bold"))
        txt_address.grid(row=3,column=1,padx=2,sticky=W,pady=7)

        # Age
        lbl_age=Label(upper_frame,text='Age:',font=('ariel',11, "bold"),bg='white')
        lbl_age.grid(row=3,column=2,padx=2,sticky=W)

        txt_age=ttk.Entry(upper_frame,textvariable=self.var_age,width=22,font=('ariel',11, "bold"))
        txt_age.grid(row=3,column=3,padx=2,sticky=W)

        # occupution
        lbl_occupution=Label(upper_frame,text='Occupution:',font=('ariel',11, "bold"),bg='white')
        lbl_occupution.grid(row=4,column=0,padx=2,sticky=W)

        txt_occupution=ttk.Entry(upper_frame,textvariable=self.var_occupation,width=22,font=('ariel',11, "bold"))
        txt_occupution.grid(row=4,column=1,padx=2,sticky=W)

        # birthmark
        lbl_birthmark=Label(upper_frame,text='Birth Mark:',font=('ariel',11, "bold"),bg='white')
        lbl_birthmark.grid(row=4,column=2,padx=2,sticky=W)

        caseentry=ttk.Entry(upper_frame,textvariable=self.var_birthMark,width=22,font=('ariel',11, "bold"))
        caseentry.grid(row=4,column=3,padx=2,sticky=W)

        #crime type
        lbl_crimetype=Label(upper_frame,text='Crime Type:',font=('ariel',11, "bold"),bg='white')
        lbl_crimetype.grid(row=0,column=4,padx=2,sticky=W,pady=7)

        txt_crimetype=ttk.Entry(upper_frame,textvariable=self.var_crime_type,width=22,font=('ariel',11, "bold"))
        txt_crimetype.grid(row=0,column=5,padx=2,sticky=W,pady=7)

        # father name
        lbl_fathername=Label(upper_frame,text='Father Name:',font=('ariel',11, "bold"),bg='white')
        lbl_fathername.grid(row=1,column=4,padx=2,sticky=W,pady=7)

        txt_fathername=ttk.Entry(upper_frame,textvariable=self.var_father_name,width=22,font=('ariel',11, "bold"))
        txt_fathername.grid(row=1,column=5,padx=2,sticky=W,pady=7)

        #gender
        lbl_gender=Label(upper_frame,text='Gender:',font=('ariel',11, "bold"),bg='white')
        lbl_gender.grid(row=2,column=4,padx=2,sticky=W,pady=7)

       
        # Most wanted
        lbl_wanted=Label(upper_frame,text='Most Wanted:',font=('ariel',11, "bold"),bg='white')
        lbl_wanted.grid(row=3,column=4,padx=2,sticky=W,pady=7)

        # Radio button gender
        radio_frame_gender=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        radio_frame_gender.place(x=700,y=80,width=190,height=30)

        male=Radiobutton(radio_frame_gender,variable=self.var_gender,text='Male',value='male',font=('ariel',8, "bold"),bg='white')
        male.grid(row=0,column=0,pady=2,padx=5,sticky=W)
        self.var_gender.set('male')
        
        # radio button for female
        male=Radiobutton(radio_frame_gender,variable=self.var_gender,text='female',value='female',font=('ariel',8, "bold"),bg='white')
        male.grid(row=0,column=1,pady=2,padx=5,sticky=W)
        self.var_gender.set('female')

         # Radio button wanted
        radio_frame_wanted=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        radio_frame_wanted.place(x=700,y=120,width=190,height=30)

        
        yes=Radiobutton(radio_frame_wanted,variable=self.var_wanted,text='Yes',value='yes',font=('ariel',8, "bold"),bg='white')
        yes.grid(row=0,column=0,pady=2,padx=5,sticky=W)
        self.var_wanted.set('yes')
        
        # radio button no
        no=Radiobutton(radio_frame_wanted,variable=self.var_wanted,text='No',value='no',font=('ariel',8, "bold"),bg='white')
        no.grid(row=0,column=1,pady=2,padx=5,sticky=W)
        self.var_wanted.set('no')

        #Button
        button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=5,y=185,width=620,height=30)

        # add button

        btn_add=Button(button_frame,command=self.add_date,text='Record save',font=('ariel',13, "bold"),widt=14,bg='blue',fg='white')
        btn_add.grid(row=0,column=0,padx=2,pady=1)
        
        # Update button

        btn_update=Button(button_frame,command=self.update_data,text='Update',font=('ariel',13, "bold"),widt=14,bg='blue',fg='white')
        btn_update.grid(row=0,column=1,padx=2,pady=1)
 
        # Delete button

        btn_delete=Button(button_frame,command=self.delete_data,text='Delete',font=('ariel',13, "bold"),widt=14,bg='blue',fg='white')
        btn_delete.grid(row=0,column=2,padx=2,pady=1)
        
         # Clear button

        btn_clear=Button(button_frame,command=self.clear_data,text='Clear',font=('ariel',13, "bold"),widt=14,bg='blue',fg='white')
        btn_clear.grid(row=0,column=3,padx=2,pady=1)

        # background right side img
        img4=Image.open('fourth.png')
        img4=img4.resize((480,280),Image.Resampling.LANCZOS)
        self.photo4=ImageTk.PhotoImage(img4)

        self.img_4=Label(upper_frame,image=self.photo4)
        self.img_4.place(x=1000,y=0,width=470,height=160)

 







        # Down frame
        down_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="CRIMINAL INFORMATION TABLE" ,font=('times new roman',11, "bold"),fg='red',bg='white')
        down_frame.place(x=10,y=250,width=1300,height=240)

        # search frame
        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,text="SEARCH CRIMINAL RECORD" ,font=('times new roman',11, "bold"),fg='red',bg='white')
        search_frame.place(x=0,y=0,width=1290,height=60)

        search_by=Label(search_frame,text='Search By:',font=('ariel',11, "bold"),bg='red',fg='white')
        search_by.grid(row=0,column=0,padx=5,sticky=W)

        self.var_com_search=StringVar()
        combo_search_box=ttk.Combobox(search_frame,textvariable=self.var_com_search,font=('ariel',11, "bold"),width=18,state='readonly')
        combo_search_box['value']=('Select Option','Case_id','Criminal_no')
        combo_search_box.current(0)
        combo_search_box.grid(row=0,column=1,padx=5,sticky=W)

        self.var_search=StringVar()
        search_txt=ttk.Entry(search_frame,textvariable=self.var_search,width=18,font=('ariel',11, "bold"))
        search_txt.grid(row=0,column=2,padx=5,sticky=W)

         # search button

        btn_search=Button(search_frame,command=self.search_data,text='Search',font=('ariel',13, "bold"),widt=14,bg='blue',fg='white')
        btn_search.grid(row=0,column=3,padx=5,sticky=W)
        
         # all button

        btn_all=Button(search_frame,command=self.fetch_data,text='Show All',font=('ariel',13, "bold"),widt=14,bg='blue',fg='white')
        btn_all.grid(row=0,column=4,padx=5,sticky=W)

        crimeagency=Label(search_frame,text='NATIONAL CRIME AGENCY',font=('ariel',30, "bold"),bg='white',fg='crimson')
        crimeagency.grid(row=0,column=6,sticky=W,padx=5,pady=1 )        


        # Table frame
        table_frame=Frame(down_frame,bd=2,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1290,height=150)
        
        # scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.criminal_table=ttk.Treeview(table_frame,columns=('1','2','3','4','5','6','7','8','9','10','11','12','13','14'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side='right',fill=Y)

        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)

        self.criminal_table.heading('1',text='CaseId')
        self.criminal_table.heading('2',text='CrimeNo')
        self.criminal_table.heading('3',text='Criminal Name')
        self.criminal_table.heading('4',text='NickName')
        self.criminal_table.heading('5',text='ArrestDate')
        self.criminal_table.heading('6',text='CrimeOfDate')
        self.criminal_table.heading('7',text='Address')
        self.criminal_table.heading('8',text='Age')
        self.criminal_table.heading('9',text='Occupation')
        self.criminal_table.heading('10',text='Birth Mark')
        self.criminal_table.heading('11',text='Crime Type')
        self.criminal_table.heading('12',text='Father Name')
        self.criminal_table.heading('13',text='Gender')
        self.criminal_table.heading('14',text='Wanted')

        self.criminal_table['show']='headings'
        self.criminal_table.column('1',width=100)
        self.criminal_table.column('2',width=100)
        self.criminal_table.column('3',width=100)
        self.criminal_table.column('4',width=100)
        self.criminal_table.column('5',width=100)
        self.criminal_table.column('6',width=100)
        self.criminal_table.column('7',width=100)
        self.criminal_table.column('8',width=100)
        self.criminal_table.column('9',width=100)
        self.criminal_table.column('10',width=100)
        self.criminal_table.column('11',width=100)
        self.criminal_table.column('12',width=100)
        self.criminal_table.column('13',width=100)
        self.criminal_table.column('14',width=100)
        self.criminal_table.pack(fill=BOTH,expand=1)

        self.criminal_table.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()


   # #Add function 
    def add_date(self):
        if self.var_case_id.get()=='':
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='Abhay@123',database='management')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into criminal values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',( self.var_case_id.get(),
                                self.var_criminal_no.get(),
                                self.var_Criminal_name.get(),
                                #self.var_name.get(),
                                self.var_nickname.get(),
                                self.var_arrest.get(),
                                self.var_date_of_crime.get(),
                                self.var_address.get(),
                                self.var_age.get(),
                                self.var_occupation.get(),
                                self.var_birthMark.get(),
                                self.var_crime_type.get(),
                                self.var_father_name.get(),
                                self.var_gender.get(),
                                self.var_wanted.get(),
                                ))
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('success','criminal record has been added')
            except Exception as es:
                messagebox.showerror('Error',f'Due To {str(es)}')


    # fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='Abhay@123',database='management')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from criminal')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.criminal_table.delete(*self.criminal_table.get_children())
            for i in data:
                self.criminal_table.insert("",END,value=i)
            conn.commit()
        conn.close()

    # get cursor
    def get_cursor(self,event=""):
        cursur_row=self.criminal_table.focus()
        content=self.criminal_table.item(cursur_row)
        data=content['values']
        
        self.var_case_id.set(data[0])
        self.var_criminal_no.set(data[1])
        self.var_Criminal_name.set(data[2])
        self.var_nickname.set(data[3])
        self.var_arrest.set(data[4])
        self.var_date_of_crime.set(data[5])
        self.var_address.set(data[6])
        self.var_age.set(data[7])
        self.var_occupation.set(data[8])
        self.var_birthMark.set(data[9])
        self.var_crime_type.set(data[10])
        self.var_father_name.set(data[11])
        self.var_gender.set(data[12])
        self.var_wanted.set(data[13])


    #Update
    
    def update_data(self):
        if self.var_case_id.get() == '':
            messagebox.showerror('Error', 'All Fields are required')
        else:
            try:
                update = messagebox.askyesno('Update', 'Are you sure you want to update this criminal record?')
                if update > 0:
                    conn = mysql.connector.connect(
                        host='localhost',
                        username='root',
                        password='Abhay@123',
                        database='management'
                    )
                    my_cursor = conn.cursor()
                    my_cursor.execute('''
                        UPDATE criminal 
                        SET Criminal_no=%s,
                            Criminal_name=%s,
                            Nick_name=%s,
                            arrest_date=%s,
                            dateOfcrime=%s,
                            address=%s,
                            age=%s,
                            occupation=%s,
                            BirthMark=%s,
                            crimeType=%s,
                            fatherName=%s,
                            gender=%s,
                            wanted=%s
                        WHERE Case_id=%s
                    ''', (
                        self.var_criminal_no.get(),
                        self.var_Criminal_name.get(),
                        self.var_nickname.get(),
                        self.var_arrest.get(),
                        self.var_date_of_crime.get(),
                        self.var_address.get(),
                        self.var_age.get(),
                        self.var_occupation.get(),
                        self.var_birthMark.get(),
                        self.var_crime_type.get(),
                        self.var_father_name.get(),
                        self.var_gender.get(),
                        self.var_wanted.get(),
                        self.var_case_id.get()
                    ))
                    conn.commit()
                    self.fetch_data()
                    self.clear_data()
                    conn.close()
                    messagebox.showinfo('Success', 'Criminal record successfully updated')
                else:
                    return
            except Exception as es:
                messagebox.showerror('Error', f'Due To {str(es)}')


    # delete
    def delete_data(self):
        if self.var_case_id.get() == '':
            messagebox.showerror('Error', 'All Fields are required')
        else:
             try:
                Delete= messagebox.askyesno('delete', 'Are you sure you want to delete this criminal record?')
                if Delete > 0:
                      conn=mysql.connector.connect(host='localhost',username='root',password='Abhay@123',database='management')
                      my_cursor=conn.cursor()
                      sql='delete from criminal where Case_id=%s'
                      value=(self.var_case_id.get(),)
                      my_cursor.execute(sql,value)
                #       conn.commit()   
                #       self.fetch_data()
                #       conn.close()
                #       messagebox.showinfo('Sucess','Criminal record successfully delete')
                else:
                    if not Delete:
                        return
                conn.commit()   
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('Sucess','Criminal record successfully delete')
                 
             except Exception as es:
                messagebox.showerror('Error',f'Due To {str(es)}')

     #clear
    def clear_data(self):
        self.var_case_id.set("")
        self.var_criminal_no.set("")
        self.var_Criminal_name.set("")
        self.var_nickname.set("")
        self.var_arrest.set("")
        self.var_date_of_crime.set("")
        self.var_address.set("")
        self.var_age.set("")
        self.var_occupation.set("")
        self.var_birthMark.set("")
        self.var_crime_type.set("")
        self.var_father_name.set("")
        self.var_gender.set("")
        self.var_wanted.set("")

                 
    # search
    def search_data(self):
        if self.var_com_search.get()=="":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='Abhay@123',database='management')
                my_cursor=conn.cursor()
                my_cursor.execute('select * from criminal where ' +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.criminal_table.delete(*self.criminal_table.get_children())
                    for i in rows:
                        self.criminal_table.insert("",END,value=i)
              

                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror('Error',f'Due To {str(es)}')

    















        

        



if __name__=='__main__':
    root=Tk()
    obj=Criminal(root)
    root.mainloop()



