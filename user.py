from tkinter import*
from PIL import Image, ImageTk #pip install pillow

from sqlConnect import database_QLBH
from user_package.hoaDon import hoaDon_win
from user_package.khachHang import khachHang_win
from user_package.sanPham import sanPham_win
from admin import adminView
from user_package.thongKe_NV import thongKe_NV_win


bgColor = "#89cff0"
fgColor = "#000000"
f = font=("times new roman", 16, "bold")


class userView:
  def __init__(self, root, userID):
    self.root = root
    self.userID = userID
    
    
    self.contentFrame = Frame(root,  bg=bgColor, borderwidth=0,)
    self.contentFrame.place(x=200, y=0, width=1000, height=650)
    #==================== MENU ===================
    menu = Frame(root,  bg=bgColor, borderwidth=0,)
    menu.place(x=0, y=0, width=200, height=650)
    
    #==================== cat =====================
    info = adminView.info_personLogin(self,userID)
    name = info[0]
    path=info[1]
    
    img_cat = Image.open(path)
    img_cat = img_cat.resize((100, 100), Image.ANTIALIAS)
    self.photoimg_cat = ImageTk.PhotoImage(img_cat)

    lbimg = Label(menu, image=self.photoimg_cat, bg=bgColor)
    lbimg.place(x=0, y=20, width=200, height=100)
    lb_name = Label(menu, text=name, bg=bgColor, font=("times new roman", 16))
    lb_name.place(x=0, y=120,width=200,height=50)
    #=================== btn =======================
    btn_frame = Frame(menu, borderwidth=0, bg=bgColor)
    btn_frame.place(x=0, y=200, width=200, height=250)
    
    self.menu_btn = Button(btn_frame, text="Trang Chủ", command=self.menu, font=f, bg=bgColor,fg=fgColor, borderwidth=0)
    self.menu_btn.place(x=0, y=0, width=200, height=50)
    self.load_tk()
    
    self.cus_btn = Button(btn_frame, text="Khách Hàng", command=self.khachHang, font=f, fg=fgColor, bg=bgColor, borderwidth=0)
    self.cus_btn.place(width=200, height=50, x=0, y=50)
    
    self.bill_btn = Button(btn_frame, text="Hóa Đơn", command=self.hoaDon, font=f, bg=bgColor, fg=fgColor, borderwidth=0)
    self.bill_btn.place(width=200, height=50, x=0, y=100)
    
    self.warehouse_btn = Button(btn_frame, text="Sản Phẩm", command=self.sanPham, font=f, bg=bgColor, fg=fgColor, borderwidth=0)
    self.warehouse_btn.place(width=200, height=50, x=0, y=150)
    #==================== +++ ==============
    logout_btn = Button(menu, text="Đăng Xuất",command=self.log, font=f, bg=bgColor, fg=fgColor,borderwidth=0)
    logout_btn.pack(side=BOTTOM, pady=50)
    
  
  def log(self):
    from login import login_windown
    login_windown(self.root, False)
    
  def load_tk(self):
    self.menu_btn.config(bg='#c3effc', fg='red',font=("times new roman", 12, "bold"))
    thongKe_NV_win(self.contentFrame, self.userID)
    
  def khachHang(self):
    self.reset_btn()
    khachHang_win(self.contentFrame, self.userID)
    self.cus_btn.config(bg='#c3effc', fg='red',font=("times new roman", 12, "bold"))
  
  def hoaDon(self):
    self.reset_btn()
    hoaDon_win(self.contentFrame, self.userID)
    self.bill_btn.config(bg='#c3effc', fg='red',font=("times new roman", 12, "bold"))
  
  def sanPham(self):
    self.reset_btn()
    sanPham_win(self.contentFrame)
    self.warehouse_btn.config(bg='#c3effc', fg='red',font=("times new roman", 12, "bold"))
    
  def menu(self):
    self.reset_btn()
    self.menu_btn.config(bg='#c3effc', fg='red',font=("times new roman", 12, "bold"))
    thongKe_NV_win(self.new_windows, self.userID)
  
  def reset_btn(self):
    self.menu_btn.config(bg=bgColor, fg=fgColor,font=f)
    self.bill_btn.config(bg=bgColor, fg=fgColor,font=f)
    self.cus_btn.config(bg=bgColor, fg=fgColor,font=f)
    self.warehouse_btn.config(bg=bgColor, fg=fgColor,font=f)
