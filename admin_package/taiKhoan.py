from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk #pip install pillow
from datetime import datetime
from tkinter import messagebox

import pyodbc
import sys
sys.path.append('E:\hk2_namII\TuHoc\QuanLiBanHang')
from sqlConnect import*



f = font=("times new roman", 12)
bgColor = '#f3d8d6'
fgColor = "#fefffa"


class taiKhoan_win:
  def __init__(self, root):
    self.root = root
    
    taiKhoan_frame = Frame(root, bg=bgColor)
    taiKhoan_frame.place(x=0, y=0, width=1000, height=620)
    
     #===================== title ===================
    title_lb = Label(taiKhoan_frame, text="Tài Khoản", font=("times newroman", 24, "bold"), fg='red', bg=bgColor)
    title_lb.place(x=0, y=0, width=200, height=50)
    
    # ==================== variables ==============
    self.var_radio=StringVar()
    
    self.var_maTK = StringVar()
    
    self.var_hoTen = StringVar()
    self.var_tenDN = StringVar()
    self.var_sdt = StringVar()
    self.var_cmnd = StringVar()
    self.var_email = StringVar()
    self.var_diaChi = StringVar()
    self.var_quyen = StringVar()
    
    self.var_ngayDK = StringVar()
    self.var_search = StringVar()
    
    #===================== lable frame =============
    lb_frame = LabelFrame(taiKhoan_frame, text="Chi Tiết Tài Khoản", font=("times newroman", 18, "bold"), bg=bgColor, padx=2, bd=4, relief=RIDGE)
    lb_frame.place(x=10, y=50, width=330, height=565)
    
    #====================lables and entrys =================
    
    
    #Mã khách hàng
    maTK_lb = Label(lb_frame, text="Mã Tài Khoản:", bg=bgColor,font=f, padx=2, pady=6)
    maTK_lb.grid(row=0, column=0, sticky=W, pady=6)
    
    maTK_txt = ttk.Entry(lb_frame, textvariable=self.var_maTK, state='readonly', width=25, font=f)
    maTK_txt.grid(row=0, column=1, pady=6)
    
    #name
    ten_lb = Label(lb_frame, text="Họ Và Tên:", bg=bgColor,font=f, padx=2, pady=6)
    ten_lb.grid(row=1, column=0, sticky=W, pady=6)
    
    ten_txt = ttk.Entry(lb_frame, textvariable=self.var_hoTen, width=25, font=f)
    ten_txt.grid(row=1, column=1, pady=6)
    
    #name login
    tenDN_lb = Label(lb_frame, text="Tên Đăng Nhập:", bg=bgColor,font=f, padx=2, pady=6)
    tenDN_lb.grid(row=2, column=0, sticky=W, pady=6)
    
    ten_txt = ttk.Entry(lb_frame, textvariable=self.var_tenDN, width=25, font=f)
    ten_txt.grid(row=2, column=1, pady=6)
    
    # quyen_lb = Label(lb_frame, text="Quyền", bg=bgColor, font=f, padx=2, pady=6)
    # quyen_lb.grid(row=3, column=0, sticky=W, pady=6)
    # quyen_txt=ttk.Entry(lb_frame, textvariable=self.var_quyen, width=25, font=f)
    # quyen_txt.grid(row=3, column=1, pady=6)
    #sdt
    sdt_lb = Label(lb_frame, text="Số Điện Thoại:", bg=bgColor,font=f, padx=2, pady=6)
    sdt_lb.grid(row=4, column=0, sticky=W, pady=6)
    
    sdt_txt = ttk.Entry(lb_frame, textvariable=self.var_sdt , width=25, font=f)
    sdt_txt.grid(row=4, column=1, pady=6)
    
    #định danh
    cmnd_lb = Label(lb_frame, text="CMND/CCCD:", bg=bgColor,font=f, padx=2, pady=6)
    cmnd_lb.grid(row=5, column=0, sticky=W, pady=6)
    
    cmnd_txt = ttk.Entry(lb_frame, textvariable=self.var_cmnd, width=25, font=f)
    cmnd_txt.grid(row=5, column=1, pady=6)
    
    #định danh
    email_lb = Label(lb_frame, text="Email:", bg=bgColor,font=f, padx=2, pady=6)
    email_lb.grid(row=6, column=0, sticky=W, pady=6)
    
    email_txt = ttk.Entry(lb_frame, textvariable=self.var_email, width=25, font=f)
    email_txt.grid(row=6, column=1, pady=6)
    
    #địa chỉ
    diaChi_lb = Label(lb_frame, text="Địa Chỉ:", bg=bgColor,font=f, padx=2, pady=6)
    diaChi_lb.grid(row=7, column=0, sticky=W, pady=6)
    
    diaChi_txt = ttk.Entry(lb_frame, textvariable=self.var_diaChi, width=25, font=f)
    diaChi_txt.grid(row=7, column=1, pady=6)
    
  
    #quyền
    quyen_lb = Label(lb_frame, text="Quyền:", bg=bgColor,font=f, padx=2, pady=6)
    quyen_lb.grid(row=8, column=0, sticky=W, pady=6)
    
    quyen_txt = ttk.Entry(lb_frame, textvariable=self.var_quyen, width=25, font=f)
    quyen_txt.grid(row=8, column=1, pady=6)
    
    #Quyền
    ngayDK_lb = Label(lb_frame, text="Ngày Đăng Ký:", bg=bgColor,font=f, padx=2, pady=6)
    ngayDK_lb.grid(row=9, column=0, sticky=W, pady=6)
    
    ngayDK_txt = ttk.Entry(lb_frame, textvariable=self.var_ngayDK, state='readonly', width=25, font=f)
    ngayDK_txt.grid(row=9, column=1, pady=6)
    
    
    #==================== frame btn ==================
    btn_frame = Frame(lb_frame, bg=bgColor)
    btn_frame.place(x=40, y=460, width=260, height=50)
    
    #==================== btn ==================
    
    update_btn = Button(btn_frame, text="Cập Nhật", command=self.update, font=f, bg='#89cff0', width=7)
    update_btn.grid(row=0, column=0, padx=2)
    
    del_btn = Button(btn_frame, text="Xóa", command=self.delete_data, font=f, bg='#89cff0', width=7)
    del_btn.grid(row=0, column=1, padx=2)
    
    reser_btn = Button(btn_frame, text="Làm Mới", command=self.reset_data, font=f, bg='#89cff0', width=7)
    reser_btn.grid(row=0, column=2, padx=2)
    
    
  # ==================== frame table =======================
    table_frame = LabelFrame(taiKhoan_frame, bg=bgColor, text="Danh Sách Tài Khoản", font=("times new roman", 18, "bold"), bd=4, relief=RIDGE)
    table_frame.place(x=360,y=50, width=625, height=565)
    
    # ================== search ============================
    search_lb = Label(table_frame, text="Tìm Kiếm", bg='#89cff0', font=f)
    search_lb.place(x=5, y=20, width=70,height=40)
    
    self.var_searchCombobox = StringVar()
    search_combo = ttk.Combobox(table_frame,textvariable=self.var_searchCombobox, state='readonly', font=f, width=23)
    search_combo["value"]=('USER_ID', 'SDT', 'CMND')
    search_combo.current(0)
    search_combo.place(x=80, y=20, width=75, height=40)
 
    
    search_txt = ttk.Entry(table_frame, textvariable=self.var_search, font=f)
    search_txt.place(x=160, y=20, width=230, height=40)
    search_txt.bind("<KeyPress>", self.search)

    # =================== show data table ===============
    dstaiKhoan_tableFrame = Frame(table_frame, bg='white', bd=2, relief=RIDGE)
    dstaiKhoan_tableFrame.place(x=10, y=75, width=600, height=450)
    
    scroll_x = ttk.Scrollbar(dstaiKhoan_tableFrame,orient=HORIZONTAL)
    scroll_y = ttk.Scrollbar(dstaiKhoan_tableFrame,orient=VERTICAL)
    
    self.thongTinTK_table = ttk.Treeview(dstaiKhoan_tableFrame, column=('maTK', 'hoTen', 'tenDN', 'sdt', 'cmnd', 'email', 'diaChi', 'quyen',
                                                                      'ngayDK'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
    
    scroll_x.pack(side=BOTTOM, fill=X)
    scroll_y.pack(side=RIGHT, fill=Y)
    
    scroll_x.config(command=self.thongTinTK_table.xview)
    scroll_y.config(command=self.thongTinTK_table.yview)
    
    self.thongTinTK_table.heading('maTK', text="Mã Tài Khoản")
    self.thongTinTK_table.heading('hoTen', text="Họ Tên")
    self.thongTinTK_table.heading('tenDN', text="Tên Đăng Nhập")
    self.thongTinTK_table.heading('sdt', text="SDT")
    self.thongTinTK_table.heading('cmnd', text="CMND/CCCD")
    self.thongTinTK_table.heading('email', text="Email")
    self.thongTinTK_table.heading('diaChi', text="Địa Chỉ")
    self.thongTinTK_table.heading('quyen', text="Quyền")
    self.thongTinTK_table.heading('ngayDK', text="Ngày Đăng Ký")
    
    self.thongTinTK_table['show']='headings'
    
    self.thongTinTK_table.column('maTK', width=100)
    self.thongTinTK_table.column('hoTen', width=100)
    self.thongTinTK_table.column('tenDN', width=100)
    self.thongTinTK_table.column('sdt', width=100)
    self.thongTinTK_table.column('cmnd', width=100)
    self.thongTinTK_table.column('email', width=100)
    self.thongTinTK_table.column('diaChi', width=100)
    self.thongTinTK_table.column('quyen', width=100)
    self.thongTinTK_table.column('ngayDK', width=100)
    
    
    self.thongTinTK_table.pack(fill=BOTH, expand=1)
    self.thongTinTK_table.bind("<ButtonRelease-1>", self.get_cursor)


    self.load_data()
  
    

  def load_data(self):
    try:
      conn = pyodbc.connect(database_QLBH[0])
      my_cursor = conn.cursor()
      my_cursor.execute("select* from TAIKHOAN where TRANGTHAI='ACTION'")
      rows = my_cursor.fetchall()
      
      self.thongTinTK_table.delete(*self.thongTinTK_table.get_children())
      if len(rows)!=0:
        for i in rows:
          list = []
          for j in range (0, len(i)):
            if j == 2:
              my_cursor = conn.cursor()
              my_cursor.execute("select USER_NAME from ACCOUNT where USER_ID=?", list[0])
              tenDN = my_cursor.fetchall()
              list.append(tenDN[0][0])
            list.append(i[j])
          self.thongTinTK_table.insert("", END, values=list)
          conn.commit()
      conn.close()
    except Exception as e:
      messagebox.showwarning('Warning', f'Xuất hiện một số vấn đề: {str(e)}', parent = self.root)
       
  def get_cursor(self, event=""):
    cursor_row= self.thongTinTK_table.focus()
    content=self.thongTinTK_table.item(cursor_row)
    row=content['values']
    if row != "":
      self.var_maTK.set(row[0]),
      self.var_hoTen.set(row[1]),
      self.var_tenDN.set(row[2])
      self.var_sdt.set(row[3]),
      self.var_cmnd.set(row[4]),
      self.var_email.set(row[5]),
      self.var_diaChi.set(row[6]),
      self.var_quyen.set(row[7])
      self.var_ngayDK.set(row[8])
      
  def update(self):
    if self.var_maTK.get()=="":
      messagebox.showerror('Error', 'Hiện chưa có mã tài khoản!', parent=self.root)
    else: 
      try:
        conn = pyodbc.connect (database_QLBH[0])
        my_cursor = conn.cursor()
        my_cursor.execute('update TAIKHOAN set TEN=?, SDT=?, CMND=?, EMAIL=?, DIACHI=?, PHANQUYEN=?, NGAYDK=? where USER_ID=?', 
                          (
                          self.var_hoTen.get(),
                          self.var_sdt.get(),
                          self.var_cmnd.get(),
                          self.var_email.get(),
                          self.var_diaChi.get(),
                          self.var_quyen.get(),
                          self.var_ngayDK.get(),
                          self.var_maTK.get()
                          ))
        my_cursor = conn.cursor()
        my_cursor.execute('update ACCOUNT set USER_NAME=? where USER_ID=?', 
                          (self.var_tenDN.get(),
                          self.var_maTK.get()))
        conn.commit()
        self.load_data()
        conn.close()        
        messagebox.showinfo('Update', 'Cập nhật thành công!', parent=self.root)
      except Exception as e:
        messagebox.showwarning('Warning', f'Xuất hiện một số vấn đề: {str(e)}', parent = self.root)
     
  def delete_data(self):
    try:
      delete_data= messagebox.askyesno('Hệ Thống Quản Lý Bán Hàng', 'Bạn có chắc muốn xóa khách hàng này?', parent=self.root)
      if delete_data>0:
        conn = pyodbc.connect(database_QLBH[0])
        my_cursor = conn.cursor()
        my_cursor.execute("update TAIKHOAN set TRANGTHAI='DELETED' where USER_ID=?", self.var_maTK.get())
        messagebox.showinfo('Delete', 'Xóa thành công!',parent=self.root)
        conn.commit()
        self.load_data()
        conn.close()
    except Exception as e:
      messagebox.showwarning('Warning', f'Xuất hiện một số vấn đề: {str(e)}', parent = self.root)
          
  def reset_data(self):
    self.var_hoTen.set(''),
    self.var_sdt.set(''),
    self.var_tenDN.set(''),
    self.var_email.set(''),
    self.var_diaChi.set(''),
    self.var_cmnd.set(''),
    self.var_maTK.set(''),
    self.var_ngayDK.set('')
      
  def search(self, event):
    try:
      #======================= Tìm kiếm admin ===================
      if self.var_searchCombobox.get()=="USER_ID":
        select_column=0
      elif self.var_searchCombobox.get()=="SDT":
        select_column=2
      else:
        select_column=3
      
      select_from= "TAIKHOAN"
      if event.keysym == 'BackSpace':
          query=self.var_search.get()[:-1]
      else:
        query=self.var_search.get()+event.char
      ds = get_dataSQL(select_from)
      
      options=[i[select_column] for i in ds]
      ds_index=search_index(query, options)
      
      if len(ds_index)!=0:
        self.thongTinTK_table.delete(*self.thongTinTK_table.get_children())
        conn = pyodbc.connect(database_QLBH[0])
        for i in ds_index:
          list = []
          for j in range (0, 10):
            if j == 2:
              my_cursor = conn.cursor()
              my_cursor.execute("select USER_NAME from ACCOUNT where USER_ID=?", list[0])
              tenDN = my_cursor.fetchall()
              list.append(tenDN[0][0])
              
            list.append(ds[i][j])
          self.thongTinTK_table.insert("", END, values=list)
          conn.commit()
        conn.close()
      elif len(query)<1:
        self.load_data()
    except Exception as e:
        messagebox.showwarning('Warning', f'Xuất hiện một số vấn đề: {str(e)}', parent = self.root)
    
if __name__ == "__main__":
  root = Tk()
  ojb = taiKhoan_win(root)
  root.mainloop()
    
     