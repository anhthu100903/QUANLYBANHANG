
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from datetime import datetime

import pyodbc
import sys
sys.path.append('E:\hk2_namII\TuHoc\QuanLiBanHang')
from sqlConnect import*

f = font=("times new roman", 12)
bgColor = '#f3d8d6'
fgColor = "#fefffa"


class khachHang_win:
  def __init__(self, root, userID):
    self.root = root
    
    self.userID = userID
    
    
    kh_frame = Frame(root, bg=bgColor)
    kh_frame.place(x=0, y=0, width=1000, height=620)
    
    # ==================== variables ==============
    self.var_maKH = StringVar()
    self.var_maKH.set(self.set_maKH())
    
    self.var_hoTen = StringVar()
    self.var_ngaySinh = StringVar()
    self.var_GioiTinh = StringVar()
    self.var_diaChi = StringVar()
    
    self.var_ngayDK = StringVar()
    current_datetime = datetime.now()
    current_date = str(current_datetime.day)+'-'+str(current_datetime.month)+'-'+str(current_datetime.year)
    self.var_ngayDK.set(current_date)
    
    self.var_sdt = StringVar()
    self.var_search = StringVar()
  
    
    #===================== title ===================
    title_lb = Label(kh_frame, text="Khách Hàng", font=("times newroman", 24, "bold"), fg='red', bg=bgColor)
    title_lb.place(x=0, y=0, width=200, height=50)
    
    #===================== lable frame =============
    lb_frame = LabelFrame(kh_frame, text="Chi Tiết Khách Hàng", font=("times newroman", 18, "bold"), bg=bgColor, padx=2, bd=4, relief=RIDGE)
    lb_frame.place(x=10, y=50, width=330, height=565)
    
    #====================lables and entrys =================
    
    #Mã khách hàng
    maKH_lb = Label(lb_frame, text="Mã Khách Hàng:", bg=bgColor,font=f, padx=2, pady=5)
    maKH_lb.grid(row=0, column=0, sticky=W, pady=10)
    
    maKH_txt = ttk.Entry(lb_frame, textvariable=self.var_maKH, state='readonly', width=25, font=f)
    maKH_txt.grid(row=0, column=1, pady=10)
    
    #name
    tenKh_lb = Label(lb_frame, text="Họ Và Tên:", bg=bgColor,font=f, padx=2, pady=5)
    tenKh_lb.grid(row=1, column=0, sticky=W, pady=10)
    
    tenKh_txt = ttk.Entry(lb_frame, textvariable=self.var_hoTen, width=25, font=f)
    tenKh_txt.grid(row=1, column=1, pady=10)
    
    #sdt
    sdtKh_lb = Label(lb_frame, text="Số Điện Thoại:", bg=bgColor,font=f, padx=2, pady=5)
    sdtKh_lb.grid(row=2, column=0, sticky=W, pady=10)
    
    sdtKh_txt = ttk.Entry(lb_frame, textvariable=self.var_sdt , width=25, font=f)
    sdtKh_txt.grid(row=2, column=1, pady=10)
    
    #ngày sinh
    ngaySinhKh_lb = Label(lb_frame, text="Ngày sinh:", bg=bgColor,font=f, padx=2, pady=5)
    ngaySinhKh_lb.grid(row=3, column=0, sticky=W, pady=10)
    
    ngaySinhKh_txt = ttk.Entry(lb_frame, textvariable=self.var_ngaySinh, width=25, font=f)
    ngaySinhKh_txt.grid(row=3, column=1, pady=10)
    
    #giới tính
    gioiTinhKh_lb = Label(lb_frame, text="Giới Tính:", bg=bgColor,font=f, padx=2, pady=5)
    gioiTinhKh_lb.grid(row=4, column=0, sticky=W, pady=10)
    
    gioiTinh_combo = ttk.Combobox(lb_frame,textvariable=self.var_GioiTinh, font=f, width=23)
    gioiTinh_combo["value"]=('Nam', 'Nữ')
    gioiTinh_combo.grid(row=4, column=1, pady=10)
 
    #địa chỉ
    diaChiKh_lb = Label(lb_frame, text="Địa Chỉ:", bg=bgColor,font=f, padx=2, pady=5)
    diaChiKh_lb.grid(row=5, column=0, sticky=W, pady=10)
    
    diaChiKh_txt = ttk.Entry(lb_frame, textvariable=self.var_diaChi, width=25, font=f)
    diaChiKh_txt.grid(row=5, column=1, pady=10)
 
    #Tiền mua
    # diemTichLuy_lb = Label(lb_frame, text="Điểm tích lũy:", bg=bgColor,font=f, padx=2, pady=5)
    # diemTichLuy_lb.grid(row=6, column=0, sticky=W, pady=10)
    
    # diemTichLuy_txt = ttk.Entry(lb_frame, textvariable=self.var_diemTichLuy, width=25, font=f)
    # diemTichLuy_txt.grid(row=6, column=1, pady=10)
    
  
    #Ghi chú
    ngayDK_lb = Label(lb_frame, text="Ngày Đăng Ký:", bg=bgColor,font=f, padx=2, pady=5)
    ngayDK_lb.grid(row=8, column=0, sticky=W, pady=10)
    
    ngayDK_txt = ttk.Entry(lb_frame, textvariable=self.var_ngayDK, state='readonly', width=25, font=f)
    ngayDK_txt.grid(row=8, column=1, pady=10)
    
    #==================== frame btn ==================
    btn_frame = Frame(lb_frame, bg=bgColor)
    btn_frame.place(x=50, y=460, width=250, height=50)
    
    #==================== btn ==================
    add_btn = Button(btn_frame, text="Thêm", command=self.add_data, font=f, bg='#89cff0', width=7)
    add_btn.grid(row=0, column=0, padx=2)
    
    update_btn = Button(btn_frame, text="Cập Nhật", command=self.update, font=f, bg='#89cff0', width=7)
    update_btn.grid(row=0, column=1, padx=2)
    
    reser_btn = Button(btn_frame, text="Làm Mới", command=self.reset_data, font=f, bg='#89cff0', width=7)
    reser_btn.grid(row=0, column=2, padx=2)
    
    # ==================== frame table =======================
    self.table_frame = LabelFrame(kh_frame, bg=bgColor, text="Danh sách khách hàng", font=("times new roman", 18, "bold"), bd=4, relief=RIDGE)
    self.table_frame.place(x=360,y=50, width=625, height=565)
    
    # ================== search ============================
    search_lb = Label(self.table_frame, text="Tìm Kiếm", bg='#89cff0', font=f)
    search_lb.place(x=5, y=20, width=70,height=40)
    
    self.var_searchCombobox = StringVar()
    search_combo = ttk.Combobox(self.table_frame,textvariable=self.var_searchCombobox, state='readonly', font=f, width=23)
    search_combo["value"]=('MAKH', 'SODT', 'HOTEN')
    search_combo.current(0)
    search_combo.place(x=80, y=20, width=75, height=40)
 
    
    search_txt = ttk.Entry(self.table_frame, textvariable=self.var_search, font=f)
    search_txt.place(x=160, y=20, width=210, height=40)
    search_txt.bind("<KeyPress>", self.search)
   
    self.lsMuaHang()
    
    # =================== show data table ===============
    dsKhachHang_tableFrame = Frame(self.table_frame, bg='white', bd=2, relief=RIDGE)
    dsKhachHang_tableFrame.place(x=10, y=75, width=600, height=450)
    
    scroll_x = ttk.Scrollbar(dsKhachHang_tableFrame,orient=HORIZONTAL)
    scroll_y = ttk.Scrollbar(dsKhachHang_tableFrame,orient=VERTICAL)
    
    self.thongTinKH_table = ttk.Treeview(dsKhachHang_tableFrame, column=('maKH', 'hoTen', 'sdt', 'gioiTinh', 'ngaySinh', 'diaChi',
                                                                      'ngayDK'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
    
    scroll_x.pack(side=BOTTOM, fill=X)
    scroll_y.pack(side=RIGHT, fill=Y)
    
    scroll_x.config(command=self.thongTinKH_table.xview)
    scroll_y.config(command=self.thongTinKH_table.yview)
    
    self.thongTinKH_table.heading('maKH', text="Mã Khách Hàng")
    self.thongTinKH_table.heading('hoTen', text="Họ Tên")
    self.thongTinKH_table.heading('sdt', text="SDT")
    self.thongTinKH_table.heading('ngaySinh', text="Ngày Sinh")
    self.thongTinKH_table.heading('gioiTinh', text="Giói Tính")
    self.thongTinKH_table.heading('diaChi', text="Địa Chỉ")
    self.thongTinKH_table.heading('ngayDK', text="Ngày Đăng Ký")
    
    self.thongTinKH_table['show']='headings'
    
    self.thongTinKH_table.column('maKH', width=100)
    self.thongTinKH_table.column('hoTen', width=100)
    self.thongTinKH_table.column('sdt', width=100)
    self.thongTinKH_table.column('ngaySinh', width=100)
    self.thongTinKH_table.column('gioiTinh', width=100)
    self.thongTinKH_table.column('diaChi', width=100)
    self.thongTinKH_table.column('ngayDK', width=100)
    
    
    self.thongTinKH_table.pack(fill=BOTH, expand=1)
    self.thongTinKH_table.bind("<ButtonRelease-1>", self.get_cursor)
    self.load_data()
    
  #============================ Liên Kết Database ==================

  def lsMuaHang(self):
    if self.userID.split('_')[0]=='AD':
      show_btn = Button(self.table_frame, text="Xem LS", command=self.show_ls, bg="#89cff0", font=f)
      show_btn.place(x=500, y=20, width=100, height=40)
  
  def show_ls(self):
    ls = Tk()
    ls.geometry("620x350+500+200")
    ls.title("Lịch sử mua hàng")
    
    makh = 'Mã Khách Hàng:    ' + self.var_maKH.get()
    lb_maKH = Label(ls, text=makh, bg='white', font=f)
    lb_maKH.place(x=10, y=20, height=40)
    
    
    dsHoaDon_tableFrame = Frame(ls, bg='white', bd=2, relief=RIDGE)
    dsHoaDon_tableFrame.place(x=10, y=85, width=600, height=250)
    
    scroll_x = ttk.Scrollbar(dsHoaDon_tableFrame,orient=HORIZONTAL)
    scroll_y = ttk.Scrollbar(dsHoaDon_tableFrame,orient=VERTICAL)
    
    self.thongTinLS_table = ttk.Treeview(dsHoaDon_tableFrame, column=('maHD', 'ngayHD', 'triGia', 'maNV'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
    
    scroll_x.pack(side=BOTTOM, fill=X)
    scroll_y.pack(side=RIGHT, fill=Y)
    
    scroll_x.config(command=self.thongTinLS_table.xview)
    scroll_y.config(command=self.thongTinLS_table.yview)
    
    self.thongTinLS_table.heading('maHD', text='Mã Hóa Đơn', anchor=CENTER)
    self.thongTinLS_table.heading('ngayHD', text='Ngày Hóa Đơn', anchor=CENTER)
    self.thongTinLS_table.heading('triGia', text='Trị Giá', anchor=CENTER)
    self.thongTinLS_table.heading('maNV', text='Mã Nhân Viên', anchor=CENTER)
    
    self.thongTinLS_table.column('maHD', width=100, anchor=CENTER)
    self.thongTinLS_table.column('ngayHD', width=100, anchor=CENTER)
    self.thongTinLS_table.column('triGia', width=100, anchor=CENTER)
    self.thongTinLS_table.column('maNV', width=100, anchor=CENTER)
    
    self.thongTinLS_table.pack(fill=BOTH, expand=1)
    self.thongTinLS_table['show']='headings'
    
    
    conn = pyodbc.connect(database_QLBH[0])
    my_cursor = conn.cursor()
    my_cursor.execute("select SOHD, NGHD, TRIGIA, MANV from HOADON where TRANGTHAI not in ('DELETED') and MAKH=?", self.var_maKH.get())
    rows = my_cursor.fetchall()
    if len(rows)!=0:
      self.thongTinLS_table.delete(*self.thongTinLS_table.get_children())
      for i in rows:
        list=[]
        for j in i:
          list.append(j)
        self.thongTinLS_table.insert("", END, values=list)
      conn.commit()
    conn.close()
    
  def load_data(self):
    conn = pyodbc.connect(database_QLBH[0])
    my_cursor = conn.cursor()
    my_cursor.execute("select* from KHACHHANG where TRANGTHAI='ACTION'")
    rows = my_cursor.fetchall()
    self.thongTinKH_table.delete(*self.thongTinKH_table.get_children())
    if len(rows)!=0:
      for i in rows:
        list = []
        for j in range(0,7): #8 thuộc tính của khách hàng
          list.append(i[j])
        self.thongTinKH_table.insert("", END, values=list)
      conn.commit()
    conn.close()
       
  def add_data(self):
    if self.var_maKH.get() == "" or self.var_sdt.get() == "":
      messagebox.showerror('Error', 'Vui lòng nhập số điện thoại!', parent = self.root)
    else:
      try:
        ngay = self.var_ngaySinh.get().split('-')
        if len(ngay)==3:
          ngSinh=datetime(int(ngay[2]), int(ngay[1]), int(ngay[0]))
        else: ngSinh=''
        
        ngay = self.var_ngayDK.get().split('-')
        ngDK=datetime(int(ngay[2]), int(ngay[1]), int(ngay[0]))
  
        conn = pyodbc.connect(database_QLBH[0])
        my_cursor = conn.cursor()
        my_cursor.execute('insert into KHACHHANG values(?,?,?,?,?,?,?,?)',
        (self.var_maKH.get(),
        self.var_hoTen.get(),
        self.var_sdt.get(),
        self.var_GioiTinh.get(),
        ngSinh,
        self.var_diaChi.get(),
        ngDK,
        'ACTION'
        ))
        conn.commit()
        self.load_data()
        conn.close()
        messagebox.showinfo('Success', 'Thêm Khách Hàng Thành Công', parent = self.root)
      except Exception as e:
        messagebox.showwarning('Warning', f'Xuất hiện một số vấn đề: {str(e)}', parent = self.root)

  def get_cursor(self, event=""):
    cursor_row= self.thongTinKH_table.focus()
    content=self.thongTinKH_table.item(cursor_row)
    row=content['values']
    if row != "":
      self.var_maKH.set(row[0]),
      self.var_hoTen.set(row[1]),
      self.var_sdt.set('0'+str(row[2])),
      self.var_GioiTinh.set(row[3]),
      self.var_ngaySinh.set(row[4]),
      self.var_diaChi.set(row[5]),
      self.var_ngayDK.set(row[6])
    
  def update(self):
    if self.var_sdt.get()=="":
      messagebox.showerror('Error', 'Vui lòng nhập số điện thoại!', parent=self.root)
    else:
      try:
        # diem = int(self.var_diemTichLuy.get())
        conn = pyodbc.connect (database_QLBH[0])
        my_cursor = conn.cursor()
        my_cursor.execute('update KHACHHANG set HOTEN=?, SODT=?, GIOITINH=?, NGSINH=?, DCHI=?, NGDK=?, TRANGTHAI=? where MAKH=?', 
                          (
                          self.var_hoTen.get(),
                          self.var_sdt.get(),
                          self.var_GioiTinh.get(),
                          self.var_ngaySinh.get(),
                          self.var_diaChi.get(),
                          self.var_ngayDK.get(),
                          'ACTION',
                          self.var_maKH.get()
                          ))
        conn.commit()
        self.load_data()
        conn.close()
        messagebox.showinfo('Update', 'Cập nhật thành công!', parent=self.root)
      except Exception as e:
        messagebox.showwarning('Warning', f'Xuất hiện một số vấn đề: {str(e)}', parent=self.root)
    
        
  def reset_data(self):
    self.var_hoTen.set(''),
    self.var_sdt.set(''),
    self.var_ngaySinh.set(''),
    self.var_GioiTinh.set(''),
    self.var_diaChi.set(''),
    self.var_ngayDK.set('')
    self.var_maKH.set(self.set_maKH())
    
    
    current_datetime = datetime.now()
    current_date = str(current_datetime.day)+'-'+str(current_datetime.month)+'-'+str(current_datetime.year)
    self.var_ngayDK.set(current_date)
      
  def search(self, event):
    if self.var_searchCombobox.get()=="MAKH":
      select_column=0
    elif self.var_searchCombobox.get()=="SODT":
      select_column=2
    else:
      select_column=1
    
    select_from= "KHACHHANG"
    if event.keysym == 'BackSpace':
      query=self.var_search.get()[:-1]
    else:
      query=self.var_search.get()+event.char
    ds = get_dataSQL(select_from)
    options=[i[select_column] for i in ds]
    ds_index=search_index(query, options)
    
    if len(ds_index)!=0:
      self.thongTinKH_table.delete(*self.thongTinKH_table.get_children())
      for i in ds_index:
        list = []
        for j in range(0,8): #8 thuộc tính của khách hàng
          list.append(ds[i][j])
        self.thongTinKH_table.insert("", END, values=list)
    elif len(query)<1:
      self.load_data()
     
  #================== tạo mã khách hàng ====================
  def set_maKH(self):
    conn = pyodbc.connect(database_QLBH[0])
    my_cursor = conn.cursor()
    my_cursor.execute('select count(MAKH) from KHACHHANG')
    count = my_cursor.fetchall()
    ref = count[0][0]
    if ref < 10:
      return 'KH0000' + str(ref)
    elif ref < 100:
      return 'KH000' + str(ref)
    elif ref < 1000:
      return 'KH00' + str(ref)
    return 'KH0' + str(ref)
   
  
if __name__ == "__main__":
  root = Tk()
  ojb = khachHang_win(root, 'AD_0001')
  root.mainloop()