from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import random,os
from tkinter import messagebox
import tempfile
from time import strftime

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing Software")

#Variables
        self.varCustMobileNo=StringVar()
        self.varCustName=StringVar()
        self.varCustEmail=StringVar()
        self.varBillNo=StringVar()
        r=random.randint(1000,9999)
        self.varBillNo.set(r)
        self.varSearchBill=StringVar()
        self.varProudct=StringVar()
        
        self.varPrice=IntVar()
        self.varQty=IntVar()
        self.varSubTotal=StringVar()
        self.varTaxInput=StringVar()
        self.varGrandTotal=StringVar()
        self.varBillData=StringVar()

#product categoryList
        self.catlist=["select option","GlassBangle","MetalBangle","PlasticBangle"]
        self.subcatGlassBangle=["Coloured","Green"]
        self.coloured=["nonpolish","polish"]
        self.price_nonpolish=300
        self.price_polish=200
        self.green=["green_nonpolish","green_polish"]
        self.price_green_nonpolish=300
        self.price_greenpolish=200

        self.subcatMetalBangle=["small","Medium","Large"]
        self.price_small=100
        self.price_medium=150
        self.price_large=200
        self.subcatPlasticBangle=["Goat","Rubber"]
        self.goat_price=160
        self.rubber_price=125      

        #Image1
        img1=Image.open("image/glassBangles.jpg")
        img1=img1.resize((500,130),Image.AFFINE)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lbl_Img=Label(self.root,image=self.photoimg1)
        lbl_Img.place(x=0,y=0,width=500,height=130)
  
        #Image2
        img2=Image.open("image/metalBangles.jpg")
        img2=img2.resize((500,130),Image.AFFINE)
        self.photoimg2=ImageTk.PhotoImage(img2)
    
        lbl_Img2=Label(self.root,image=self.photoimg2)
        lbl_Img2.place(x=500,y=0,width=500,height=130)

       #Image3
        img3=Image.open("image/plasticBangles.jpg")
        img3=img3.resize((520,130),Image.AFFINE)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        lbl_Img3=Label(self.root,image=self.photoimg3)
        lbl_Img3.place(x=1000,y=0,width=520,height=130)
        
        #Label Title
        lbl_title=Label(self.root,text="KALIKA BANGLES AND IMITATION GWELLARY, BARSHI",font=("times new roman",35,"bold"),bg="white",fg="red")
        lbl_title.place(x=0,y=135,width=1560,height=70)

        def time():
            string  = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl = Label(lbl_title,font=('times new roman',16,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=0,width=120,height=70)

        time()
    
       #main Frame
        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y=200,width=1530,height=580)
        
        #customer LableFrame
        Cust_Frame=LabelFrame(Main_Frame,text="Customer",font=("times new roman",12,"bold"),bg="white",fg='red')
        Cust_Frame.place(x=0,y=5,width=350,height=130)

        self.lbl_mob=Label(Cust_Frame,text="Mobile No.",font=("times new roman",12,"bold"),bg="white")
        self.lbl_mob.grid(row=0,column=0,stick=W,padx=5,pady=2)
        
        self.entry_mob=ttk.Entry(Cust_Frame,textvariable=self.varCustMobileNo,font=("times new roman",12,"bold"),width=24)
        self.entry_mob.grid(row=0,column=1)

        self.lbl_custName=Label(Cust_Frame,text="Customer Name",font=("times new roman",12,"bold"),bg="white")
        self.lbl_custName.grid(row=1,column=0,stick=W,padx=5,pady=2)

        self.entry_cust=ttk.Entry(Cust_Frame,textvariable=self.varCustName,font=("times new roman",12,"bold"),width=24)
        self.entry_cust.grid(row=1,column=1)

        self.lbl_email=Label(Cust_Frame,text="Customer Email",font=("times new roman",12,"bold"),bg="white")
        self.lbl_email.grid(row=2,column=0,stick=W,padx=5,pady=2)

        self.entry_email=ttk.Entry(Cust_Frame,textvariable=self.varCustEmail,font=("times new roman",12,"bold"),width=24)
        self.entry_email.grid(row=2,column=1)

#Product LableFrame
        Product_Frame=LabelFrame(Main_Frame,text="Product",font=("times new roman",12,"bold"),bg="white",fg='red')
        Product_Frame.place(x=370,y=5,width=600,height=130)
#Category
        self.lbl_category=Label(Product_Frame,text="Select Category",font=("times new roman",12,"bold"),bg="white")
        self.lbl_category.grid(row=0,column=0,stick=W,padx=5,pady=2)
    
        self.combo_Category=ttk.Combobox(Product_Frame,value=self.catlist,font=('arial',12),width=24,state='readonly')
        self.combo_Category.current(0)
        self.combo_Category.grid(row=0,column=1,padx=5,pady=2)
        self.combo_Category.bind("<<ComboboxSelected>>",self.Categories)
#SubCategory
        self.lbl_SubCategory=Label(Product_Frame,text="Sub Category",font=("times new roman",12,"bold"),bg="white")
        self.lbl_SubCategory.grid(row=1,column=0,stick=W,padx=5,pady=2)
    
        self.combo_SubCategory=ttk.Combobox(Product_Frame,value=[""],font=('arial',12,'bold'),width=24,state='readonly')
        self.combo_SubCategory.grid(row=1,column=1,padx=5,pady=2)
        self.combo_SubCategory.bind("<<ComboboxSelected>>",self.Product_add)
#ProductName
        self.lbl_productName=Label(Product_Frame,text="Product Name",font=("times new roman",12,"bold"),bg="white")
        self.lbl_productName.grid(row=2,column=0,stick=W,padx=5,pady=2)
    
        self.combo_productName=ttk.Combobox(Product_Frame,font=('arial',12,'bold'),width=24,state='readonly')
        self.combo_productName.grid(row=2,column=1,padx=5,pady=2)
        self.combo_productName.bind("<<ComboboxSelected>>")
        self.varProudct.set(self.combo_productName.get())
#price
        self.lbl_price=Label(Product_Frame,text="Price",font=("times new roman",12,"bold"),bg="white")
        self.lbl_price.grid(row=0,column=2,stick=W,padx=5,pady=2)
    
        self.price=ttk.Entry(Product_Frame,textvariable=self.varPrice,font=('arial',12,'bold'),width=10)
        self.price.grid(row=0,column=3,padx=5,pady=2)
        self.price.bind()
        self.varPrice.set(self.price.get())
        

#quantity
        self.lbl_qty=Label(Product_Frame,text="Quantity",font=("times new roman",12,"bold"),bg="white")
        self.lbl_qty.grid(row=1,column=2,stick=W,padx=5,pady=2)
    
        self.qty=ttk.Entry(Product_Frame,textvariable=self.varQty,font=('arial',12,'bold'),width=10)
        self.qty.grid(row=1,column=3,padx=5,pady=2)
        self.varQty.set(self.qty.get())
        #messagebox.showinfo(self.qty.get())
#Middle Frame
        Middle_Frame=Frame(Main_Frame,bd=10,bg='green')
        Middle_Frame.place(x=10,y=140,width=980,height=340)

          #Image4
        img4=Image.open("image/vistingcard2.jpg")
        img4=img4.resize((400,140),Image.AFFINE)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lbl_Img4=Label(Middle_Frame,image=self.photoimg4)
        lbl_Img4.place(x=0,y=0,width=490,height=240)
  
        #Image5
        img5=Image.open("image/vistingcard2.jpg")
        img5=img5.resize((400,140),Image.AFFINE)
        self.photoimg5=ImageTk.PhotoImage(img5)
    
        lbl_Img5=Label(Middle_Frame,image=self.photoimg5)
        lbl_Img5.place(x=490,y=0,width=490,height=240)


#Search Frame
        Search_Frame=Frame(Main_Frame,bd=2,bg='white')
        Search_Frame.place(x=980,y=10,width=500,height=40)

        self.lblBill=Label(Search_Frame,font=('arial',10,'bold'),bg='red',text="Bill Number", fg="white")
        self.lblBill.grid(row=0,column=0,sticky=W,padx=2)

        self.txt_Entry_Search=ttk.Entry(Search_Frame,textvariable=self.varSearchBill,font=('arial',10,'bold'),width=24)
        self.txt_Entry_Search.grid(row=0,column=1,sticky=W,pady=2)


        self.btnSearch=Button(Search_Frame,command=self.find_bill,text="Search",font=('arial',10,'bold'),bg="orangered",fg='white',width=8,cursor='hand2')
        self.btnSearch.grid(row=0,column=2,padx=2)

#RightFrame Bill Area
        RightLabelFrame=LabelFrame(Main_Frame,text="Bill Section",font=('arial',12,"bold"),bg="white",fg="blue")
        RightLabelFrame.place(x=975,y=45,width=520,height=407)

        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=('arial',13,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

#Bill counter
        Bottom_Frame=LabelFrame(Main_Frame,text="Bill Counter",font=('arial',12,'bold'),bg='white',fg='blue')
        Bottom_Frame.place(x=0,y=450,width=1520,height=125)      

        self.lbl_subTotal=Label(Bottom_Frame,text="Sub Total",font=("times new roman",12,"bold"),bg="white")
        self.lbl_subTotal.grid(row=0,column=0,stick=W,padx=5,pady=2)
        
        self.entry_mob=ttk.Entry(Bottom_Frame,textvariable=self.varSubTotal,font=("times new roman",12,"bold"),width=24)
        self.entry_mob.grid(row=0,column=1)

        self.lbl_tax=Label(Bottom_Frame,text="Tax",font=("times new roman",12,"bold"),bd=4)
        self.lbl_tax.grid(row=1,column=0,stick=W,padx=5,pady=2)
        
        self.entry_tax=ttk.Entry(Bottom_Frame,textvariable=self.varTaxInput,font=("times new roman",12,"bold"),width=24)
        self.entry_tax.grid(row=1,column=1)

        self.lbl_totAmount=Label(Bottom_Frame,text="Total Amount",font=("times new roman",12,"bold"),bd=4)
        self.lbl_totAmount.grid(row=2,column=0,stick=W,padx=5,pady=2)
        
        self.entry_totAmount=ttk.Entry(Bottom_Frame,textvariable=self.varGrandTotal,font=("times new roman",12,"bold"),width=24)
        self.entry_totAmount.grid(row=2,column=1)

#Button Frame
        Btn_Frame =Frame(Bottom_Frame,height=2,bd=2,bg='white')
        Btn_Frame.place(x=320,y=0)

        self.btnAddtoCart=Button(Btn_Frame,command=self.AddItem,text="Add to Cart",font=('arial',15,'bold'),bg="orangered",fg='white',width=15,cursor='hand2')
        self.btnAddtoCart.grid(row=0,column=0)

        self.btnGenBill=Button(Btn_Frame,text="Generate Bill",command=self.gen_bill,font=('arial',15,'bold'),bg="orangered",fg='white',width=15,cursor='hand2')
        self.btnGenBill.grid(row=0,column=1)

        self.btnSave=Button(Btn_Frame,text="Save Bill",command=self.save_bill,font=('arial',15,'bold'),bg="orangered",fg='white',width=15,cursor='hand2')
        self.btnSave.grid(row=0,column=2)

        self.btnPrint=Button(Btn_Frame,text="Print",command=self.print_bill,font=('arial',15,'bold'),bg="orangered",fg='white',width=15,cursor='hand2')
        self.btnPrint.grid(row=0,column=3)

        self.btnClear=Button(Btn_Frame,text="Clear",command=self.clear_all,font=('arial',15,'bold'),bg="orangered",fg='white',width=15,cursor='hand2')
        self.btnClear.grid(row=0,column=4)

        self.btnExit=Button(Btn_Frame,command=self.root.destroy,text="Exit",font=('arial',15,'bold'),bg="orangered",fg='white',width=15,cursor='hand2')
        self.btnExit.grid(row=0,column=5)
        
        self.Welcome()
        
    def Categories(self,event=""):
        if self.combo_Category.get()=="GlassBangle":
            self.combo_SubCategory.config(value=self.subcatGlassBangle)
            self.combo_SubCategory.current(0)

        if self.combo_Category.get()=="MetalBangle":
            self.combo_SubCategory.config(value=self.subcatMetalBangle)
            self.combo_SubCategory.current(0)

        if self.combo_Category.get()=="PlasticBangle":
            self.combo_SubCategory.config(value=self.subcatPlasticBangle)
            self.combo_SubCategory.current(0)

    def Product_add(self,event=""):
        if self.combo_SubCategory.get()=="Coloured":
            self.combo_productName.config(value=self.coloured)
            self.combo_productName.current(0)
        if self.combo_SubCategory.get()=="Green":
            self.combo_productName.config(value=self.green)
            self.combo_productName.current(0)
    
    def Welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t\t Welcome Kalika Bangles Store")
        self.textarea.insert(END,f"\n Bill Number:{self.varBillNo.get()}")
        self.textarea.insert(END,f"\n Customer Name:{self.varCustName.get()}")
        self.textarea.insert(END,f"\n Phone Number:{self.varCustMobileNo.get()}")
        self.textarea.insert(END,f"\n Customer Eamil:{self.varCustEmail.get()}")
        
        self.textarea.insert(END,"\n =================================================")
        self.textarea.insert(END,f"\n Products \t\t QTY \tPrice \t\tAmout")
        self.textarea.insert(END,"\n =================================================")
        
        self.l=[]
    #======= Functions ==================
    def AddItem(self):
        Tax=1
        #self.varPrice.set(self.price.get())
        #self.varQty.set(self.qty.get())
        self.n=self.varPrice.get()
        self.m = self.varQty.get() * self.n #### Qty * price e.g. 5 * 200 = 1000
        self.l.append(self.m)

        if self.combo_productName.get()=="":
            messagebox.showerror("Error","Please select product")
          
        else:
           self.textarea.insert(END,f"\n {self.combo_productName.get()} \t\t{self.qty.get()} \t{self.price.get()} \t\t{self.m}")
           self.varSubTotal.set(str('Rs.%.2f'%(sum(self.l))))
           self.varTaxInput.set(str('Rs.%.2f'%(((sum(self.l))- (self.varPrice.get())) * Tax/100)))
           self.varGrandTotal.set(str('Rs.%.2f'%(((sum(self.l)) + ((((sum(self.l))-(self.varPrice.get()))*Tax/100))))))

 
    def gen_bill(self):
        if self.combo_productName.get()=="":
            messagebox.showerror("Error","Please add Products to Bill")
        else:
            text=self.textarea.get(10.0,(10.0+float(len(self.l))))
            
            self.Welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END,"\n =================================================")
            self.textarea.insert(END,f"\n Sub Amount:\t\t\t{self.varSubTotal.get()}")
            self.textarea.insert(END,f"\n Tax Amount:\t\t\t{self.varTaxInput.get()}")
            self.textarea.insert(END,f"\n Total Amount:\t\t\t{self.varGrandTotal.get()}")
            self.textarea.insert(END,"\n =================================================")

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill..")
        if op>0:
            self.varBillData=self.textarea.get(1.0,END)
            f1=open('bills/'+str(self.varBillNo.get())+".txt",W)
            f1.write(self.varBillData)
            f1.close
            op=messagebox.showinfo("Saved",f"Bill No:{self.varBillNo.get()} Saved successfully")
    
    def print_bill(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")

    def find_bill(self):
        found="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.varSearchBill.get():
                f1=open(f'bills/{i}','r')
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                    found='yes'

                f1.close()

        if found=='no':
            messagebox.showerror("Error","Invalid Bill Number")              
             
    def clear_all(self):
        self.textarea.delete(1.0,END)
        self.varCustEmail.set("")
        self.varCustMobileNo.set("")
        self.varCustName.set("")
        self.varProudct.set("")
        self.varTaxInput.set('')
        self.l=[0]
        self.varPrice.set(0)
        self.varQty.set(0)
        self.varSearchBill.set("")
        self.varTaxInput.set("")
        self.varSubTotal.set("")
        self.varGrandTotal.set("")
        self.Welcome()


if __name__ == '__main__':
    root = Tk()
    obj = Bill_App(root)
    root.mainloop()

