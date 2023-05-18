from tkinter import*
from PIL import Image, ImageTk #pip install pillow

import pyodbc
from sqlConnect import database_QLBH

from admin_package.taiKhoan import taiKhoan_win
from admin_package.thongKe import thongKe_win
from admin_package.qlDonHang import qlDonHang_win
from admin_package.qlDanhMuc import qlDM_win
from user_package.khachHang import khachHang_win
from admin_package.duyetTaiKhoan import duyet_win


bgColor = "#89cff0"
fgColor = "#000000"
f = font=("times new roman", 16, "bold")


class adminView():
  def __init__(self,  frame, userID):
    
    self.frame = frame
    self.userID = userID
    
    
    self.thongke_frame = Frame(self.frame,  bg=bgColor, borderwidth=0,)
    self.thongke_frame.place(x=200, y=0, width=1000, height=650)
    #==================== MENU ===================
    menu_frame = Frame(self.frame,  bg=bgColor, borderwidth=0,)
    menu_frame.place(x=0, y=0, width=200, height=620)
    
    #==================== cat =====================
    info = self.info_personLogin(self.userID)
    name=info[0]
    path=info[1]
    img_person = Image.open(path)
    img_person = img_person.resize((100, 100), Image.ANTIALIAS)
    self.photoimg_cat = ImageTk.PhotoImage(img_person)

    lbimg = Label(menu_frame, image=self.photoimg_cat, bg=bgColor)
    lbimg.place(x=0, y=20, width=200, height=100)
    
    # name ='anhthu'
    lb_name = Label(menu_frame, text=name, bg=bgColor, font=("times new roman", 16))
    lb_name.place(x=0, y=120,width=200,height=50)
    #=================== btn =======================
    self.btn_frame = Frame(menu_frame, borderwidth=0, bg=bgColor)
    self.btn_frame.place(x=5, y=170, width=190, height=350)
    
    self.menu_btn = Button(self.btn_frame, text="Trang Chủ", command=self.menu, font=f, bg=bgColor,fg=fgColor, borderwidth=0)
    self.menu_btn.place(x=0, y=0, width=190, height=50)
    self.load_tk()
    
    self.qLyTaiKhoan_btn = Button(self.btn_frame, text="Tài Khoản", command=self.taiKhoan, font=f, fg=fgColor, bg=bgColor, borderwidth=0)
    self.qLyTaiKhoan_btn.place(width=190, height=50, x=0, y=50)
    
    self.qLyDonHang_btn = Button(self.btn_frame, text="Đơn Hàng", command=self.donhang, font=f, bg=bgColor, fg=fgColor, borderwidth=0)
    self.qLyDonHang_btn.place(width=190, height=50, x=0, y=100)
    
    self.qLyDanhMuc_btn = Button(self.btn_frame, text="Danh Mục", command=self.danhmuc, font=f, bg=bgColor, fg=fgColor, borderwidth=0)
    self.qLyDanhMuc_btn.place(width=190, height=50, x=0, y=150)
    
    self.qLyKhachHang_btn = Button(self.btn_frame, text="Khách Hàng", command=self.khachhang, font=f, bg=bgColor, fg=fgColor, borderwidth=0)
    self.qLyKhachHang_btn.place(width=190, height=50, x=0, y=200)
    
    self.duyet_TaiKhoan()
    
    #==================== +++ ==============
    logout_btn = Button(menu_frame, text="Đăng Xuất", command=self.log, font=f, bg=bgColor, fg=fgColor,borderwidth=0)
    logout_btn.pack(side=BOTTOM, pady=50)
    

  def info_personLogin(self, id):
    conn = pyodbc.connect(database_QLBH[0])
    my_cursor = conn.cursor()
    my_cursor.execute('select TEN, HINHANH, PHANQUYEN from TAIKHOAN where USER_ID=?', id)
    rows = my_cursor.fetchall()
    list=[]
    if len(rows)!=0:
      if rows[0][0]=='' or rows[0][0]==None:
        list.append("")
      else:
        list.append(rows[0][0])
      if rows[0][1] != None and rows[0][1] != "": 
        list.append(rows[0][1])
      else:
        list.append('.//img//user.png')
      list.append(rows[0][2])
    return list
  
  def log(self):
    from login import login_windown
    login_windown(self.frame, False)
  
  def taiKhoan(self):
    self.reset_btn()
    self.qLyTaiKhoan_btn.config(bg='#c3effc', fg='red',font=("times new roman", 12, "bold"))
    taiKhoan_win(self.thongke_frame)
    
  def load_tk(self):
    self.menu_btn.config(bg='#c3effc', fg='red',font=("times new roman", 12, "bold"))
    thongKe_win(self.thongke_frame)
    
  def menu(self):
    self.reset_btn()
    self.menu_btn.config(bg='#c3effc', fg='red',font=("times new roman", 12, "bold"))
    thongKe_win(self.thongke_frame)
    
    
  def donhang(self):
    self.reset_btn()
    self.qLyDonHang_btn.config(bg='#c3effc', fg='red',font=("times new roman", 12, "bold"))
    qlDonHang_win(self.thongke_frame, self.userID)
  
  def danhmuc(self):
    self.reset_btn()
    self.qLyDanhMuc_btn.config(bg='#c3effc', fg='red',font=("times new roman", 12, "bold"))
    qlDM_win(self.thongke_frame)
  
  def khachhang(self):
    self.reset_btn()
    self.qLyKhachHang_btn.config(bg='#c3effc', fg='red',font=("times new roman", 12, "bold"))
    khachHang_win(self.thongke_frame, self.userID)
  
  def duyet(self):
    self.reset_btn()
    self.qlDuyetTK_btn.config(bg='#c3effc', fg='red',font=("times new roman", 12, "bold"))
    duyet_win(self.thongke_frame)
    
  def duyet_TaiKhoan(self):
    if self.info_personLogin(self.userID)[2]=='Admin':
      self.qlDuyetTK_btn = Button(self.btn_frame, text="Duyệt", command=self.duyet, font=f, bg=bgColor, fg=fgColor, borderwidth=0)
      self.qlDuyetTK_btn.place(width=200, height=50, x=0, y=250)
  
  def reset_btn(self):
    self.menu_btn.config(bg=bgColor, fg=fgColor,font=f)
    self.qLyTaiKhoan_btn.config(bg=bgColor, fg=fgColor,font=f)
    self.qLyDonHang_btn.config(bg=bgColor, fg=fgColor,font=f)
    self.qLyDanhMuc_btn.config(bg=bgColor, fg=fgColor,font=f)
    self.qLyKhachHang_btn.config(bg=bgColor, fg=fgColor,font=f)
    self.qlDuyetTK_btn.config(bg=bgColor, fg=fgColor,font=f)
    
if __name__ == "__main__": #nếu tập lệnh là hàm main thì thực thi
  root = Tk()
  ojb=adminView(root, 'AD_00002')
  root.mainloop()