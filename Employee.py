import tkinter as tk 
from tkinter import ttk

class employee():
    def __init__(self, root ):
        self.root = root
        self.root.title("Employee Management System")
        #Creates Geometry :
        self.root.geometry("1400x650+0+0")
        # Creates Label for Employee for Employee management system:
        self.Label = tk.Label(self.root, text="Employee Management System",
                              bg="cyan" , fg ="black",
                              font=("italic" ,40 , "bold"),bd=4, relief="groove")
        self.Label.pack(side = tk.TOP , fill="x")

        # Creates Frame1 in left side :
        self.frame1= tk.Frame(self.root, bg="skyblue", bd=4, relief="ridge")
        self.frame1.place(x=10, y=80 ,width=370 ,height=550)

        #Creates Employeeid Label in frame1:
        self.idLabel=tk.Label(self.frame1,  text="Employee's ID: ",
                              bg="red", fg="White", font=("Arial",14,"bold"))
                       
        self.idLabel.grid(row=0, column=0 )

        #Creates Entry widgets in id label:
        self.idInp= tk.Entry(self.frame1, font=("Arial, 14"), width=15)
        self.idInp.grid(row=0, column=1 ,pady=10)

        #1Creates  Name Label in frame1:
        self.NameLabel=tk.Label(self.frame1,  text="Employee's Name: ",
                                      bg="red", fg="White",
                                        font=("Arial",14,"bold"))                                  
        self.NameLabel.grid(row=1, column=0 )
        
        #1Creates Entry widgets in Name label:
        self.NameInp= tk.Entry(self.frame1, font=("Arial, 14"), width=15)
        self.NameInp.grid(row=1, column=1 ,pady=10)


        #2Creates  Designation Label in frame1:
        self.desigLabel=tk.Label(self.frame1, text="Designation:",
                                      bg="red", fg="White",
                                        font=("Arial",14,"bold"))                                  
        self.desigLabel.grid(row=2, column=0 )
        
        #2Creates Entry widgets in desig label:
        self.desigInp= tk.Entry(self.frame1, font=("Arial, 14"), width=15)
        self.desigInp.grid(row=2, column=1 ,pady=10)


        #3Creates  Salary Label in frame1:
        self.salaryLabel=tk.Label(self.frame1,  text="Employee's Salary: ",
                                      bg="red", fg="White",
                                      font=("Arial",14,"bold"))                                  
        self.salaryLabel.grid(row=3, column=0)
        
        #3Creates Entry widgets for salary label:
        self.salaryInp= tk.Entry(self.frame1, font=("Arial, 14"), width=15)
        self.salaryInp.grid(row=3, column=1 ,pady=10)
     

        #4Creates  gender Label in frame1:
        self.genderLabel=tk.Label(self.frame1,  text="Gender: ",
                                      bg="red", fg="White",
                                        font=("Arial",14,"bold"))                                  
        self.genderLabel.grid(row=4, column=0 )
        
        #4Creates combobox for choose Gender:- state is use for taking option.
        self.genInp= ttk.Combobox(self.frame1, font=("Arial",14)
                                  ,width=13, state="readonly") 
        self.genInp['values']=("Male" , "Female","other")
        self.genInp.grid(row=4, column=1, pady=10)       

        #5Creates label of Address :
        self.AddLabel=tk.Label(self.frame1, text="Employee Address:",
                               bg="red", fg="white",font=("Arial",14,"bold"))

        self.AddLabel.grid(row=5, column=0)

        #5 Take input  in address field from user by text:
        self.AddInp= tk.Text(self.frame1, width=15, height=3
                             ,font=("Arial",14), pady=10 )
        self.AddInp.grid(row=5, column=1 ,pady=10)

        # ---Creates nested frame inside frame1----
        self.btnFrame=tk.Frame(self.frame1,bd=4, relief="raised")
        self.btnFrame.place(x=6, y=360 , width=350,height=170)

        # Creates Buttons Inside Nested Frame :
        #1.ADD BUTTON
        self.Addbtn=tk.Button(self.btnFrame, text="ADD",bg="red",fg="white",
                              width=10, font=("Arial",14,"bold"))
        self.Addbtn.grid(row=0,column=0,padx=20, pady=20)
        #2.UPDATE BUTTON
        self.updbtn= tk.Button(self.btnFrame,text="UPDATE" ,bg="red",fg="white"
                           , font=("Arial",14,"bold"),width=10)
        self.updbtn.grid(row=0,column=1,padx=20,pady=20)

        #3.DELETE BUTTONS:
        self.delbtn=tk.Button(self.btnFrame,text="DELETE",bg="red",fg="white"
                              ,font=("Arial",14,"bold"),width=10)
        self.delbtn.grid(row=1,column=0, padx=20,pady=20)

        #4.CLEAR BUTTON:
        self.clearbtn=tk.Button(self.btnFrame,text="CLEAR",bg="red",fg="white"
                                      ,font=("Arial",14,"bold"),width=10)
        self.clearbtn.grid(row=1,column=1, padx=20,pady=20)
        
        
        #-------Creates Frame2 in right side-------- 53:16
        self.frame2 = tk.Frame(self.root,bg="skyblue", bd=6, relief="ridge")
        self.frame2.place(x=390 , y= 80 ,width=970, height=550)

        #1Creates search label in second frame:
        self.searchLabel=tk.Label(self.frame2,text="Search By:",bg="red"
                                  ,fg="white",font=("Arial",14,"bold"))
        self.searchLabel.grid(row=0,column=0,padx=3)

        #Creates combobox in frame2:
        self.searchtype= ttk.Combobox(self.frame2, font=("arial",14),
                                     width=15, state="readonly")
        self.searchtype['values']=("Id" ,"Name")
        self.searchtype.grid(row=0, column=1, padx=10,pady=10) 

        self.searchinp=tk.Entry(self.frame2, font=("Arial",15),width=15)
        self.searchinp.grid(row=0,column=2, pady=10)

        #Creates Buttons in frame2:
        self.searchbtn=tk.Button(self.frame2, text="Search",bg="red",fg="white",
                                 font=("arial",13,"bold"),width=12)
        self.searchbtn.grid(row=0, column=3,padx=5,pady=10)

       #Creates show Buttons in frame2:
        self.showbtn=tk.Button(self.frame2, text="Display All",bg="red",fg="white",
                                       font=("arial",13,"bold"),width=12)
        self.showbtn.grid(row=0, column=4,padx=15,pady=10)

        #------Creates Table frame inside frame2-----
        self.tabframe=tk.Frame(self.frame2,bg="cyan",bd=7,relief="sunken")
        self.tabframe.place(x=5,y=50, width=950,height=480 )

        #Creates Scrollbar:
        self.x_scroll= tk.Scrollbar(self.tabframe, orient="horizontal")
        self.x_scroll.pack(side="bottom", fill="x")

        self.y_scroll=  tk.Scrollbar(self.tabframe, orient="vertical")
        self.y_scroll.pack(side="right", fill="y")

        self.table=ttk.Treeview(self.tabframe, columns=("Id", "Name",
                                                        "Desig","Salary",
                                                        "Gender","Addr"),
                                               xscrollcommand=self.x_scroll,
                                              yscrollcommand=self.y_scroll)
        self.x_scroll.config(command=self.table.xview)
        self.y_scroll.config(command=self.table.yview)

        self.table.heading("Id",text="Emp_Id")
        self.table.heading("Name", text="Emp_Name")
        self.table.heading("Desig",text="Designation")
        self.table.heading("Salary",text="Emp_Salary")
        self.table.heading("Gender",text="Emp_Gender")
        self.table.heading("Addr",text="Emp_Address")
        self.table['show']="headings"

        self.table.column("Id",width=100)
        self.table.column("Name",width=100)
        self.table.column("Desig",width=100)
        self.table.column("Salary",width=100)
        self.table.column("Gender",width=100)
        self.table.column("Addr",width=100)
       
        self.table.pack(fill="both", expand=1)
 
root = tk.Tk()
obj = employee(root) # creates obj for cons.
root.mainloop()    


    
