from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import pyodbc
from tkinter import filedialog
import os
import sys

sys.path.append('E:\hk2_namII\TuHoc\QuanLiBanHang')
from sqlConnect import*


f = font=("times new roman", 12)
bgColor = '#f3d8d6'
fgColor = "#fefffa"

class qlSP_win:
  def __init__(self, root, madm):
    self.root = root
    self.root.geometry("1000x590+220+80")
    self.root.overrideredirect(True)
    
    self.madm=madm
     
     
    # ==================== task bar ===================
    taskbar_frame = Frame(self.root)
    taskbar_frame.place(x=0, y=0, width=1200, height=30)
  
    lb_title = Label(taskbar_frame, text="Quản lý sản phẩm",  font=("times new roman", 10, "bold"), borderwidth=0)
    lb_title.place(x=0, y=0, height=30)
    
    btn_exit = Button(taskbar_frame, text="✖", command=root.destroy, font= ("times new roman", 16, "bold"), bd=3, fg='red')
    btn_exit.place(x=950, y=0, width=50, height=30)
    #-------------------------------------------
     
    qlSP_frame = Frame(root, bg=bgColor)
    qlSP_frame.place(x=0, y=30, width=1000, height=620)
    
      #biến qlsp
    self.var_anh = StringVar()
    self.var_masp = StringVar()
    self.var_tensp = StringVar()
    self.var_danhmuc = StringVar()
    self.var_giaNhap = StringVar()
    self.var_giaBan = StringVar()
    self.var_sluong = IntVar()
    self.var_dvt = StringVar()
    self.var_xuatXu = StringVar()
    self.var_ngayNhap = StringVar()
    
    # ==================== frame ttsp =======================
    self.ttsp_frame = LabelFrame(qlSP_frame, bg=bgColor, text="Thông Tin Sản Phẩm", font=("times new roman", 18, "bold"), bd=4, relief=RIDGE)
    self.ttsp_frame.place(x=10,y=0, width=980, height=250)
    
    #================== search ============================
    search_lb = Label(self.ttsp_frame, text="Tìm Kiếm", bg='#89cff0', font=f)
    search_lb.place(x=530, y=0, width=70,height=30)
        
    self.var_searchCombobox = StringVar()
    search_combo = ttk.Combobox(self.ttsp_frame, textvariable=self.var_searchCombobox, state='readonly', font=f, width=23)
    search_combo["value"]=('MASP', 'TENSP')
    search_combo.current(0)
    search_combo.place(x=605, y=0, width=100, height=30)
    
    self.var_search = StringVar()
    search_txt = ttk.Entry(self.ttsp_frame, textvariable=self.var_search, font=f)
    search_txt.place(x=710, y=0, width=250, height=30)
    search_txt.bind("<KeyPress>", self.search)
   
    #===================== content ttsp ================
    img_import = Image.open(r'.//img//new-product.png')
    img_import = img_import.resize((150, 150), Image.ANTIALIAS)
    self.import_photo = ImageTk.PhotoImage(img_import)
    img_lb = Label(self.ttsp_frame, image=self.import_photo)
    img_lb.place(x=20, y=10, width=150, height=150)
    
    img_lb = Label(self.ttsp_frame, text='Image File', font=f, bg=bgColor)
    img_lb.place(x=2, y=180, width=75, height=30)
    
    file_img_txt = ttk.Entry(self.ttsp_frame, textvariable=self.var_anh, font=f)
    file_img_txt.place(x=100, y=180, width=200, height=30)
    
    img_btn = Button(self.ttsp_frame, text='Browse', command=self.open_file, bg='#89cff0',font=f)
    img_btn.place(x=295, y=180, width=75, height=30)
    
      #chức năng
    them_btn = Button(self.ttsp_frame, text='Thêm', command=self.add_data, bg='#89cff0',font=f)
    them_btn.place(x=610, y=180, width=75,height=30)
    
    xoa_btn = Button(self.ttsp_frame, text='Xóa', command=self.delete_data, bg='#89cff0',font=f)
    xoa_btn.place(x=700, y=180, width=75,height=30)
    
    capNhat_btn = Button(self.ttsp_frame, text='Cập Nhật', command=self.update_data, bg='#89cff0',font=f)
    capNhat_btn.place(x=790, y=180, width=75,height=30)
    
    lamMoi_btn = Button(self.ttsp_frame, text='Làm Mới', command=self.reset_data, bg='#89cff0',font=f)
    lamMoi_btn.place(x=880, y=180, width=75,height=30)
    
      #thông tin sản phẩm
    madm_lb = Label(self.ttsp_frame, text=self.madm, bg='#89cff0', font=f)
    madm_lb.place(x=215, y=0, height=30)
    
    thongTin_frame = Frame(self.ttsp_frame, bg=bgColor)
    thongTin_frame.place(x=205, y=40, width=750, height=120)
    
      #row 0
    maSP_lb = Label(thongTin_frame, text='Mã Sản Phẩm:', font=f, bg=bgColor)
    maSP_lb.place(x=10, y=0, height=30)
    maSP_txt = ttk.Entry(thongTin_frame, textvariable=self.var_masp, font=f)
    maSP_txt.place(x=110,y=0, width=150, height=30)
    
    tenSP_lb = Label(thongTin_frame, text='Tên Sản Phẩm:', font=f, bg=bgColor)
    tenSP_lb.place(x=285, y=0, height=30)
    tenSP_txt = ttk.Entry(thongTin_frame, textvariable=self.var_tensp, font=f)
    tenSP_txt.place(x=390, y=0, width=150, height=30)
    
    danhMuc_lb = Label(thongTin_frame, text='Danh Mục SP:', font=f, bg=bgColor)
    danhMuc_lb.place(x=565, y=0, height=30)
    danhMuc_Combo = ttk.Combobox(thongTin_frame, textvariable=self.var_danhmuc, state='readonly', font=f)
    danhMuc_Combo['values'] =tuple(self.dsDM())
    danhMuc_Combo.place(x=670, y=0, width=80, height=30)
    for i in self.dsDM():
      temp=re.findall(self.madm, i)
      if temp!=[]:
        current_dm=self.dsDM().index(temp[0])
    danhMuc_Combo.current(current_dm)
        #row 1
    giaNhap_lb = Label(thongTin_frame, text="Giá Nhập:", font=f, bg=bgColor)
    giaNhap_lb.place(x=10, y=40, height=30)
    giaNhap_txt = ttk.Entry(thongTin_frame, textvariable=self.var_giaNhap, font=f)
    giaNhap_txt.place(x=110, y=40, width=150, height=30)
    
    giaBan_lb = Label(thongTin_frame, text='Giá Bán:', font=f, bg=bgColor)
    giaBan_lb.place(x=285, y=40, height=30)
    giaBan_txt = ttk.Entry(thongTin_frame, textvariable=self.var_giaBan, font=f)
    giaBan_txt.place(x=390, y=40, width=150, height=30)
    
    soLuong_lb = Label(thongTin_frame, text='Số Lượng:', bg=bgColor,font=f)
    soLuong_lb.place(x=565, y=40, height=30)
    soLuongGiam_btn = Button(thongTin_frame, command=self.sl_giam, text='-', font=f)
    soLuongGiam_btn.place(x=644,y=40,width=30,height=30)
    soLuong_txt = ttk.Entry(thongTin_frame, textvariable=self.var_sluong, font=f)
    soLuong_txt.place(x=677, y=40, width=40, height=30)
    soLuongTang_btn = Button(thongTin_frame, command=self.sl_tang, text='+', font=f)
    soLuongTang_btn.place(x=720,y=40,width=30,height=30)
    
        #row 2
    donViTinh_lb = Label(thongTin_frame, text='Đơn Vị Tính:', font=f, bg=bgColor)
    donViTinh_lb.place(x=10, y=80, height=30)
    donViTinh_txt = ttk.Entry(thongTin_frame, textvariable=self.var_dvt, font=f)
    donViTinh_txt.place(x=110,y=80, width=150, height=30)
    
    ngayNhap_lb = Label(thongTin_frame, text='Ngày Nhập:', font=f, bg=bgColor)
    ngayNhap_lb.place(x=285, y=80, height=30)
    ngayNhap_lb = ttk.Entry(thongTin_frame, textvariable=self.var_ngayNhap, font=f)
    ngayNhap_lb.place(x=390, y=80, width=150, height=30)
    
    xuatXu_lb = Label(thongTin_frame, text='Xuất Xứ:', font=f, bg=bgColor)
    xuatXu_lb.place(x=565, y=80, height=30)
    xuatXu_txt = ttk.Entry(thongTin_frame, textvariable=self.var_xuatXu, font=f)
    xuatXu_txt.place(x=645, y=80, width=105, height=30)
    
    # =================== table sanpham ===============
    dsSanPham_tableFrame = Frame(qlSP_frame, bg='white', bd=2, relief=RIDGE)
    dsSanPham_tableFrame.place(x=10, y=260, width=980, height=290)
    
    scroll_x = ttk.Scrollbar(dsSanPham_tableFrame,orient=HORIZONTAL)
    scroll_y = ttk.Scrollbar(dsSanPham_tableFrame,orient=VERTICAL)
    
    self.thongTinSP_table = ttk.Treeview(dsSanPham_tableFrame, column=('maSanPham', 'sanPham', 'gia','giaGoc', 'donViTinh', 'nguonGoc', 'kho',  'ngayNhap', 'maDM', 'hinh'),
                                         xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
    
    scroll_x.pack(side=BOTTOM, fill=X)
    scroll_y.pack(side=RIGHT, fill=Y)
    
    scroll_x.config(command=self.thongTinSP_table.xview)
    scroll_y.config(command=self.thongTinSP_table.yview)
    
    self.thongTinSP_table.heading('maSanPham', text='Mã Sản Phẩm')
    self.thongTinSP_table.heading('sanPham', text='Sản Phẩm')
    self.thongTinSP_table.heading('gia', text='Giá Bán')   
    self.thongTinSP_table.heading('giaGoc', text='Giá Nhập')
    self.thongTinSP_table.heading('donViTinh', text='Đơn Vị Tính')
    self.thongTinSP_table.heading('nguonGoc', text='Nguồn Gốc')
    self.thongTinSP_table.heading('kho', text='Kho')
    self.thongTinSP_table.heading('ngayNhap', text='Ngày Nhập')
    self.thongTinSP_table.heading('maDM', text='Mã Danh Mục')
    self.thongTinSP_table.heading('hinh', text='Hình Ảnh')
    
    
    
    self.thongTinSP_table['show'] = 'headings'
    
    self.thongTinSP_table.column('maSanPham', width=100, anchor=CENTER)
    self.thongTinSP_table.column('sanPham', width=100, anchor=CENTER)
    self.thongTinSP_table.column('gia', width=100, anchor=CENTER)
    self.thongTinSP_table.column('giaGoc', width=75, anchor=CENTER)
    self.thongTinSP_table.column('donViTinh', width=50, anchor=CENTER)
    self.thongTinSP_table.column('nguonGoc', width=75, anchor=CENTER)
    self.thongTinSP_table.column('kho', width=50, anchor=CENTER)
    self.thongTinSP_table.column('ngayNhap', width=75, anchor=CENTER)
    self.thongTinSP_table.column('maDM', width=75, anchor=CENTER)
    self.thongTinSP_table.column('hinh', width=75, anchor=CENTER)
    
    
    self.thongTinSP_table.pack(fill=BOTH, expand=1)
    self.thongTinSP_table.bind("<ButtonRelease-1>", self.get_cursor)
    self.load_table()
    
    #===============================
  
  def load_img(self, path):
    if path == 'None' or path == "":
      path = './/img//null.jpg'
    try: 
      img_import = Image.open(path)
      img_import = img_import.resize((150, 150), Image.ANTIALIAS)
      self.import_photo = ImageTk.PhotoImage(img_import)
      img_lb = Label(self.ttsp_frame, image=self.import_photo)
      img_lb.place(x=20, y=10, width=150, height=150)
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
      
  def dsDM(self):
    conn = pyodbc.connect(database_QLBH[0])
    my_cursor = conn.cursor()
    my_cursor.execute('select MADM from DANHMUC')
    rows = my_cursor.fetchall()
    list=[]
    if len(rows)!=0:
      for i in rows:
        list.append(i[0])
      return list
    list.append("")
    return list
      
  def load_table(self):
    conn = pyodbc.connect(database_QLBH[0])
    my_cursor = conn.cursor()
    my_cursor.execute("select* from SanPham where TRANGTHAI='ACTION' and MADM=?", self.madm)
    rows = my_cursor.fetchall()
    self.thongTinSP_table.delete(*self.thongTinSP_table.get_children())
    if len(rows)!=0:
      for i in rows:
        list=[]
        for j in range(1,10):
          list.append(i[j])
        list.append(i[0])
        self.thongTinSP_table.insert('', END, values=list)
      conn.commit()
    conn.close()
    
  def get_cursor(self, event=''):
    cursor_row = self.thongTinSP_table.focus()
    content = self.thongTinSP_table.item(cursor_row)
    row=content['values']
    if row !="":
      self.var_masp.set(row[0])
      self.var_tensp.set(row[1])
      self.var_giaBan.set(row[2])
      self.var_giaNhap.set(row[3])
      self.var_dvt.set(row[4])
      self.var_xuatXu.set(row[5])
      self.var_sluong.set(row[6])
      self.var_ngayNhap.set(row[7])
      self.var_danhmuc.set(row[8])
      self.var_anh.set(row[9])
      
      self.load_img(row[9])
      
  def add_data(self):
    if self.var_masp.get() =='':
      messagebox.showerror('Error', 'Vui lòng nhập mã sản phẩm!',parent= self.root)
    elif self.var_danhmuc.get() =='':
      messagebox.showerror('Error', 'Vui lòng chọn danh mục!',parent= self.root)
    else:
      try:
        conn = pyodbc.connect(database_QLBH[0])
        my_cursor = conn.cursor()
        my_cursor.execute("select MASP from SANPHAM")
        rows = my_cursor.fetchall()
        for i in rows:
          if self.var_masp.get() == i[0]:
            messagebox.showerror('Error', 'Mã Sản Phẩm Đã Tồn Tại!', parent=self.root)
            return 0
        my_cursor = conn.cursor()
        my_cursor.execute('insert into SANPHAM values(?,?,?,?,?,?,?,?,?,?,?)',
                          self.var_anh.get(),
                          self.var_masp.get(),
                          self.var_tensp.get(),
                          self.var_giaBan.get(),
                          self.var_giaNhap.get(),
                          self.var_dvt.get(),
                          self.var_xuatXu.get(),
                          self.var_sluong.get(),
                          self.var_ngayNhap.get(),
                          self.var_danhmuc.get(),
                          'ACTION'
                          )
        conn.commit()
        messagebox.showinfo('Success', 'Thêm Sản Phẩm Thành Công', parent = self.root)
        self.load_table()
        conn.close()
        self.reset_data()
      except Exception as e:
        messagebox.showinfo('Warning', f'Xuất hiện một số vấn đề: {str(e)}', parent=self.root)
  
  def update_data(self):
    if self.var_masp.get() =='':
      messagebox.showerror('Error', 'Vui lòng nhập mã sản phẩm!',parent= self.root)
    else:
      try:
        conn = pyodbc.connect(database_QLBH[0])
        my_cursor = conn.cursor()
        my_cursor.execute('update SANPHAM set HINHANH=?, TENSP=?, GIA=?, GIAGOC=?, DVT=?, NUOCSX=?, SOLUONG=?, NGAYNHAP=?, MADM=?, TRANGTHAI=? WHERE MASP=?',
                          self.var_anh.get(),
                          self.var_tensp.get(),
                          self.var_giaBan.get(),
                          self.var_giaNhap.get(),
                          self.var_dvt.get(),
                          self.var_xuatXu.get(),
                          self.var_sluong.get(),
                          self.var_ngayNhap.get(),
                          self.var_danhmuc.get(),
                          'ACTION',
                          self.var_masp.get()
                          )
        conn.commit()
        messagebox.showinfo('Success', 'Cập Nhật Sản Phẩm Thành Công', parent = self.root)
        self.load_table()
        conn.close()
        self.reset_data()
      except Exception as e:
        messagebox.showwarning('Warning', f'Xuất hiện một số vấn đề: {str(e)}', parent=self.root)
  
  def delete_data(self):
    if self.var_masp.get() =='':
      messagebox.showerror('Error', 'Vui lòng nhập mã sản phẩm',parent= self.root)
    else:
      try:
        delete_data= messagebox.askyesno('Hệ Thống Quản Lý Bán Hàng', 'Bạn có chắc muốn xóa sản phẩm này?', parent=self.root)
        if delete_data>0:
          conn = pyodbc.connect(database_QLBH[0])
          my_cursor = conn.cursor()
          my_cursor.execute("update SANPHAM set TRANGTHAI='DELETED' WHERE MASP=?", self.var_masp.get())
          messagebox.showinfo('Delete', 'Xóa thành công!',parent=self.root)
          conn.commit()
          self.load_table()
          conn.close()
          self.reset_data()
      except Exception as e:
        messagebox.showwarning('Warning', f'Xuất hiện một số vấn đề: {str(e)}', parent=self.root)
    
  def reset_data(self):
    self.var_anh.set(''),
    self.var_tensp.set(''),
    self.var_giaBan.set(''),
    self.var_giaNhap.set(''),
    self.var_dvt.set(''),
    self.var_xuatXu.set(''),
    self.var_sluong.set(''),
    self.var_ngayNhap.set(''),
    self.var_danhmuc.set(''),
    self.var_masp.set('')
    self.load_img('')
  
  def search(self, event):
    if self.var_searchCombobox.get()=="MASP":
      select_column=1
    elif self.var_searchCombobox.get()=="TENSP":
      select_column=2
    else:
      select_column=9
    
    select_from= "SANPHAM"
    if event.keysym == 'BackSpace':
        query=self.var_search.get()[:-1]
    else:
      query=self.var_search.get()+event.char
    conn = pyodbc.connect(database_QLBH[0])
    my_cursor = conn.cursor()
    my_cursor.execute("select* from SANPHAM where TRANGTHAI='ACTION' and MADM=?", self.madm)
    ds = my_cursor.fetchall()
    options=[i[select_column] for i in ds]
    ds_index=search_index(query, options)
    
    if len(ds_index)!=0:
      self.thongTinSP_table.delete(*self.thongTinSP_table.get_children())
      for i in ds_index:
        list=[]
        for j in range(1,10):
          list.append(ds[i][j])
        list.append(ds[i][0])
        self.thongTinSP_table.insert('', END, values=list)
    elif len(query)<1:
      self.load_table()
    
  def sl_tang(self):
    self.var_sluong.set(self.var_sluong.get()+1)
      
  def sl_giam(self):
    if self.var_sluong.get() - 1 < 0:
      messagebox.showerror('Error', 'Số lượng vượt quá phạm vi cho phép', parent=self.root)
    else:
      self.var_sluong.set(self.var_sluong.get()-1)
  
  def delete_sp(self):
    delete_data= messagebox.askyesno('Hệ Thống Quản Lý Bán Hàng', 'Bạn có chắc muốn xóa khách hàng này?', parent=self.root)
    if delete_data>0:
      try:
        if self.var_search=="":
          messagebox.showerror('Error', 'Không tốn tại mã sản phẩm!', parent=self.root)
        else: 
          giam = int(self.var_thanhTien.get())*int(self.var_giamGia.get())//100
          tien = int(self.var_thanhTien.get()) - giam
          conn = pyodbc.connect (database_QLBH[0])
          my_cursor = conn.cursor()
          my_cursor.execute('update CTHD set TRANGTHAI=? where MACTHD=?', 
                            (
                              self.var_maDH.get(),
                              self.var_search.get(),
                              self.var_soLuong.get(),
                              giam,
                              tien,
                              'DELETE',
                              self.var_maCTHD.get(),
                            ))
          conn.commit()
          self.load_sp(self.var_maDH.get())
          conn.close()
          messagebox.showinfo('Update', 'Cập nhật thành công!', parent=self.root)
          self.reset_sp()
          self.tongTien()
      except Exception as e:
        messagebox.showwarning('Warning', f'Xuất hiện một số vấn đề: {str(e)}', parent = self.root)


if __name__ == "__main__":
  root = Tk()
  ojb = qlSP_win(root)
  root.mainloop()           