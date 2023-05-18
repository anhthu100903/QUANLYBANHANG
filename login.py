from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import pyodbc
from sqlConnect import database_QLBH

from dangKy import register_windown
from user import userView
from admin import adminView

class login_windown():#userView
  def __init__(self, root, flag):
    
    f = font=(("times new roman", 11, "bold"))
    
    self.root = root
    
    
    
    # ==================== task bar ===================
    if flag==True:
      self.root.geometry("1200x650+50+10")
      self.root.overrideredirect(True)
      taskbar_frame = Frame(root)
      taskbar_frame.place(x=0, y=0, width=1200, height=30)
    
      lb_title = Label(taskbar_frame, text="QUẢN LÝ BÁN HÀNG",  font=("times new roman", 10, "bold"), borderwidth=0)
      lb_title.place(x=0, y=0, width=150, height=30)
      
      btn_exit = Button(taskbar_frame, text="✖", command=root.destroy, font= ("times new roman", 16, "bold"), bd=3, fg='red')
      btn_exit.place(x=1150, y=0, width=50, height=30)
      
      self.content_frame = Frame(root)
      self.content_frame.place(x=0, y=30, width=1200, height=620)
    else:
    #============== content frame
      self.content_frame = Frame(root)
      self.content_frame.place(x=0, y=0, width=1200, height=620)
    #==================== login =================== 
    
    self.var_user = StringVar()
    self.var_pass = StringVar()
    
    lb_bgLogin =Label(self.content_frame,bg='#89cff0')
    lb_bgLogin.place(x=0, y=0, width=1200, height=650)
    
    frame_login = Frame(self.content_frame, bg="black")
    frame_login.place(x=450, y=70, width=300, height=450)
    
    img_user = Image.open(r".\\img\\user_login.jpg")
    lb_imgUser = Label(frame_login)
    img_user = img_user.resize((100, 100), Image.ANTIALIAS)
    self.photoimg_user = ImageTk.PhotoImage(img_user)
    lb_imgUser = Label(self.content_frame, image=self.photoimg_user, bg="black", borderwidth=0)
    lb_imgUser.place(x=550, y=75, width=100, height=100)
    
    get_str = Label(frame_login, text="Get Started", font=("times new roman", 20, "bold"), fg='white', bg="black")
    get_str.place(x=85, y=100)
    
    #============== Lable ===========
    username = Label(frame_login, text="Tên đăng nhập", font=f, fg= 'white', bg='black')
    username.place(x=50, y=160)
    self.txtuser = ttk.Entry(frame_login, textvariable=self.var_user, font=f)
    self.txtuser.place(x=50, y=190, width=230)
    self.txtuser.bind("<KeyPress>", self.user_name_event)

    password = Label(frame_login, text="Mật khẩu", font=f, fg= 'white', bg='black')
    password.place(x=50, y=230)
    self.txtpass = ttk.Entry(frame_login, textvariable=self.var_pass, font=f)
    self.txtpass.place(x=50, y=260, width=230)
    self.txtpass.bind("<KeyPress>", self.log_event)
    # ==========login ===================
    btn_login = Button(frame_login,command=self.login, text="Đăng Nhập", font=f, fg='white', bg='red', bd=3, relief=RIDGE)
    btn_login.place(x=100, y=310, width=125, height=30)
    
    register = Button(frame_login, text="Đăng ký tài khoản", command=self.dky, font=f, fg= 'white', bg='black')
    register.place(x=150, y=400)
    
    #================== +++ ===============
  def user_name_event(self, event):
    if event.keysym == 'Return' or event.keysym == 'KP_Enter':
        self.txtpass.focus_set()
  
  def log_event(self, event):
    if event.keysym == 'Return' or event.keysym == 'KP_Enter':
        self.login()

  
  def login(self):
    if self.txtuser.get()=="" or self.txtpass.get()=="":
      messagebox.showerror("Error", "Vui Lòng Nhập Thông Tin!")
    else:
      try:
        conn = pyodbc.connect(database_QLBH[0])
        my_cursor = conn.cursor()
        my_cursor.execute('select* from ACCOUNT')
        rows = my_cursor.fetchall()
        
        flag = False #cờ hiệu xem đang nhập thành công chưa
        if len(rows) != 0:
          for i in  rows:
            if self.txtuser.get() == i[0] and self.txtpass.get() == i[1]:
              messagebox.showinfo("Success", "Đăng Nhập Thành Công!")
              flag = True
              if i[2].split('_')[0] == 'NV':
                userView(self.content_frame, i[2])
                self.var_pass.set('')
                self.var_user.set('')
              elif i[2].split('_')[0] =='AD':
                adminView(self.content_frame, i[2])
                self.var_pass.set('')
                self.var_user.set('')
          if flag == False:
            messagebox.showerror("Invalid", "Tên Đăng Nhập Hoặc Mật Khẩu Sai!")
              
      except Exception as e:
        messagebox.showwarning('Warning', f'Xuất hiện một số vấn đề: {str(e)}', parent = self.root)

  def dky(self):
    new_window=Toplevel(self.root)
    dk = register_windown(new_window)
    
if __name__ == "__main__":
  root = Tk()
  ojb = login_windown(root, True)
  root.mainloop()