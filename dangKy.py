from tkinter import*
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import pyodbc
from sqlConnect import database_QLBH


class register_windown():
  def __init__(self, root):
    f = font=(("times new roman", 11, "bold"))
    
    self.root = root
    self.root.title("Register")
    self.root.geometry("1000x600+150+30")
    
    
    
    #==================== dky =================== 
    self.var_username = StringVar()
    self.var_pass = StringVar()
    self.var_fullname =StringVar()
    self.var_sdt = StringVar()
    self.var_permission = StringVar()
    self.var_address = StringVar()
    self.var_email = StringVar()
    self.var_cmnd = StringVar()
    
    #màu nền xanh
    lb_bgRegister =Label(self.root,bg='#89cff0')
    lb_bgRegister.place(x=0, y=0, width=1000, height=600)
    
    self.frame_Register = Frame(self.root, bg="black")
    self.frame_Register.place(x=300, y=25, width=400, height=550)
    
    #anh
    self.var_anh = StringVar()
    path='.//img//user.png'
    self.load_img(path)
    
    img_lb = Label(self.frame_Register, text='Image File', font=f, bg="black", fg='white')
    img_lb.place(x=160, y=75, width=75, height=30)
    
    file_img_txt = ttk.Entry(self.frame_Register, textvariable=self.var_anh, font=f)
    file_img_txt.place(x=160, y=105, width=140, height=30)
    
    img_btn = Button(self.frame_Register, text='Browse', command=self.open_file, bg='#89cff0',font=f)
    img_btn.place(x=310, y=105, width=60, height=30)
    
    #============== Lable ===========
    username = Label(self.frame_Register, text="Tên Đăng Nhập", font=f, fg= 'white', bg='black')
    username.place(x=20, y=160)
    self.txtuser = ttk.Entry(self.frame_Register, textvariable=self.var_username, font=f)
    self.txtuser.place(x=140, y=160, width=230)
    
    password = Label(self.frame_Register, text="Mật Khẩu", font=f, fg= 'white', bg='black')
    password.place(x=20, y=200)
    self.txtpass = ttk.Entry(self.frame_Register, textvariable=self.var_pass, font=f)
    self.txtpass.place(x=140, y=200, width=230)

    fullname = Label(self.frame_Register, text="Họ Tên", font=f, fg= 'white', bg='black')
    fullname.place(x=20, y=240)
    self.txtFullName = ttk.Entry(self.frame_Register, textvariable=self.var_fullname, font=f)
    self.txtFullName.place(x=140, y=240, width=230)
    
    lb_power = Label(self.frame_Register, text='Quyền', font=f, fg= 'white', bg='black')
    lb_power.place(x=20, y=280)
    power_combo = ttk.Combobox(self.frame_Register, state='readonly', textvariable=self.var_permission, font=f)
    power_combo["value"]=('Nhân Viên','Quản Lý', 'Admin')
    power_combo.current(0)
    power_combo.place(x=140, y=280, width=230)
    
    sdt = Label(self.frame_Register, text="SDT", font=f, fg= 'white', bg='black')
    sdt.place(x=20, y=320)
    self.txtSdt = ttk.Entry(self.frame_Register, textvariable=self.var_sdt, font=f)
    self.txtSdt.place(x=140, y=320, width=230)
    
    cmnd = Label(self.frame_Register, text="CMND", font=f, fg= 'white', bg='black')
    cmnd.place(x=20, y=360)
    self.txtcmnd = ttk.Entry(self.frame_Register, textvariable=self.var_cmnd, font=f)
    self.txtcmnd.place(x=140, y=360, width=230)
    
    email = Label(self.frame_Register, text="Email", font=f, fg= 'white', bg='black')
    email.place(x=20, y=400)
    self.txtEmail = ttk.Entry(self.frame_Register, textvariable=self.var_email, font=f)
    self.txtEmail.place(x=140, y=400, width=230)
    
    
    address = Label(self.frame_Register, text="Địa Chỉ", font=f, fg= 'white', bg='black')
    address.place(x=20, y=440)
    self.txtAddress = ttk.Entry(self.frame_Register, textvariable=self.var_address, font=f)
    self.txtAddress.place(x=140, y=440, width=230)
    
    # ==========login ===================
    btn_register = Button(self.frame_Register, text="Gửi yêu cầu", command=self.registe, font=f, fg='white', bg='red', bd=3, relief=RIDGE)
    btn_register.place(x=150, y=490, width=125, height=30)
    
    #================== +++ ===============
 
 
  def registe(self):
    if self.var_username.get() == '' or self.var_pass.get() == '' or self.var_fullname.get() == '' or self.var_permission.get() =='':
      messagebox.showerror('Error', 'Vui lòng nhập đủ thông tin!', parent=self.root)
    else:
      try:
        ngay = datetime.now()
        conn = pyodbc.connect(database_QLBH[0])
        my_cursor = conn.cursor()
        my_cursor.execute('insert into REGISTER values(?,?,?,?,?,?,?,?,?,?)',
                          (self.var_username.get(),
                           self.var_pass.get(),
                           self.var_fullname.get(),
                           self.var_sdt.get(),
                           self.var_cmnd.get(),
                           self.var_email.get(),
                           self.var_address.get(),
                           self.var_permission.get(),
                           ngay,
                           self.var_anh.get()))
        conn.commit()
        conn.close()
        messagebox.showinfo('Success', 'Gửi yêu cầu thành công')
        self.reset()
      except Exception as e:
        messagebox.showwarning('Warning',f'Xuất hiện một số vấn đề: {str(e)}', parent = self.root)
  
  def reset(self):
    self.var_username.set('')
    self.var_address.set('')
    self.var_cmnd.set('')
    self.var_email.set('')
    self.var_fullname.set('')
    self.var_pass.set('')
    self.var_permission.set('Nhân Viên')
    self.var_sdt.set('')
    self.var_anh.set('')
    self.load_img(".//img//user.png")
    
  def load_img(self, path):
    if path == 'None' or path == "":
      path = './/img//user.png'
    try: 
      img_import = Image.open(path)
      img_import = img_import.resize((120, 120), Image.ANTIALIAS)
      self.import_photo = ImageTk.PhotoImage(img_import)
      img_lb = Label(self.frame_Register, image=self.import_photo)
      img_lb.place(x=20, y=15, width=120, height=120)
    except Exception as e:
      messagebox.showwarning('Warning', f'Xuất hiện một số vấn đề: {str(e)}', parent=self.root)
       
  def open_file(self):
    p = filedialog.askopenfilenames(parent=self.root, initialdir='/', initialfile='', filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg"), ("All files", "*")])
    if len(p) != 0:
      path = p[0].replace('/', '//')
    else:
      path=""
    self.var_anh.set(path)
    self.load_img(path)
    
if __name__ == "__main__":
  root = Tk()
  ojb = register_windown(root)
  root.mainloop()