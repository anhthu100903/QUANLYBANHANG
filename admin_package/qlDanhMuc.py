from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import pyodbc
import sys
from admin_package.qlSanPham import qlSP_win
# from qlSanPham import qlSP_win

sys.path.append('E:\hk2_namII\TuHoc\QuanLiBanHang')
from sqlConnect import*

f = font=("times new roman", 12)
bgColor = '#f3d8d6'
fgColor = "#fefffa"

class qlDM_win:
  def __init__(self, root):
    self.root = root
    
    qlDM_frame = Frame(root, bg=bgColor)
    qlDM_frame.place(x=0, y=0, width=1000, height=620)
    #===================== title ===================
    title_lb = Label(qlDM_frame, text="Quản Lý Danh Mục", font=("times newroman", 24, "bold"), fg='red', bg=bgColor)
    title_lb.place(x=0, y=0, width=300, height=50)
    #biến dữ liệu
    self.var_madm = StringVar()
    self.var_tendm = StringVar()
    # search
    search_lb = Label(qlDM_frame, text="Tìm Kiếm", bg='#89cff0', font=f)
    search_lb.place(x=550, y=20, width=70,height=30)
        
    self.var_searchCombobox = StringVar()
    search_combo = ttk.Combobox(qlDM_frame, textvariable=self.var_searchCombobox, state='readonly', font=f, width=23)
    search_combo["value"]=('MADM', 'TENDM')
    search_combo.current(0)
    search_combo.place(x=625, y=20, width=100, height=30)
    
    self.var_search = StringVar()
    search_txt = ttk.Entry(qlDM_frame,textvariable=self.var_search, font=f)
    search_txt.place(x=730, y=20, width=250, height=30)
    search_txt.bind("<KeyPress>", self.search)
   
    #=================== Thông tin danh mục =============
    ttdm_frame = LabelFrame(qlDM_frame, text='Thông tin danh mục', bg=bgColor, font=("times new roman", 18, "bold"), bd=4, relief=RIDGE)
    ttdm_frame.place(x=10, y=60, width=590, height=150)

    #thông tin danh mục
    maDM_lb = Label(ttdm_frame, text='Mã Danh Mục:', bg=bgColor, font=f)
    maDM_lb.place(x=10, y=10, width=100, height=30)
    maDM_txt = ttk.Entry(ttdm_frame, textvariable=self.var_madm, font=f)
    maDM_txt.place(x=115, y=10, width=150, height=30)

    tenDM_lb = Label(ttdm_frame, text='Tên Danh Mục:', bg=bgColor, font=f)
    tenDM_lb.place(x=310, y=10, width=100, height=30)
    tenDM_txt = ttk.Entry(ttdm_frame, textvariable=self.var_tendm, font=f)
    tenDM_txt.place(x=410, y=10, width=150, height=30)
    
    #chức năng
    them_btn = Button(ttdm_frame, text='Thêm', command=self.add_danhmuc, bg='#89cff0',font=f)
    them_btn.place(x=220, y=60, width=75,height=30)
    
    xoa_btn = Button(ttdm_frame, text='Xóa', command=self.delete_danhmuc, bg='#89cff0',font=f)
    xoa_btn.place(x=310, y=60, width=75,height=30)
    
    capNhat_btn = Button(ttdm_frame, text='Cập Nhật', command=self.update_danhmuc, bg='#89cff0',font=f)
    capNhat_btn.place(x=400, y=60, width=75,height=30)
    
    lamMoi_btn = Button(ttdm_frame, text='Làm Mới', command=self.reset_danhmuc, bg='#89cff0',font=f)
    lamMoi_btn.place(x=490, y=60, width=75,height=30)
    
    xem_dssp = Button(qlDM_frame, command=self.load_sanpham, text='Xem Sản Phảm', font=f, bg='#89cff0')
    xem_dssp.place(x=300, y=230, width=150, height=30)
    
    xem_dssp = Button(qlDM_frame, command=self.sanPham, text='Chỉnh Sửa Sản Phẩm', font=f, bg='#89cff0')
    xem_dssp.place(x=450, y=230, width=150, height=30)
    #danh sách danh mục
    dsDanhMuc_lb = Label(qlDM_frame, text='Danh Sách Danh Mục', font=f, bg=bgColor)
    dsDanhMuc_lb.place(x=610, y=60, width=140, height=20)
    dsDanhMuc_tableFrame = Frame(qlDM_frame, bg=bgColor)
    dsDanhMuc_tableFrame.place(x=610, y=80, width=380, height=180)
    
    scroll_x = ttk.Scrollbar(dsDanhMuc_tableFrame,orient=HORIZONTAL)
    scroll_y = ttk.Scrollbar(dsDanhMuc_tableFrame,orient=VERTICAL)
    
    self.thongTinDM_table = ttk.Treeview(dsDanhMuc_tableFrame, column=('maDM', 'tenDanhMuc'),
                                         xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
    
    scroll_x.pack(side=BOTTOM, fill=X)
    scroll_y.pack(side=RIGHT, fill=Y)
    
    scroll_x.config(command=self.thongTinDM_table.xview)
    scroll_y.config(command=self.thongTinDM_table.yview)
    
    self.thongTinDM_table.heading('maDM', text='Mã Danh Mục')
    self.thongTinDM_table.heading('tenDanhMuc', text='Tên Danh Mục')
    
    self.thongTinDM_table['show'] = 'headings'
    
    self.thongTinDM_table.column('maDM', width=150, anchor=CENTER)
    self.thongTinDM_table.column('tenDanhMuc', width=200, anchor=CENTER)
    
    self.thongTinDM_table.pack(fill=BOTH, expand=1)
  
    #danh sách sản phẩm
    dsDanhMuc_lb = Label(qlDM_frame, text='Danh Sách Sản Phẩm', font=f, bg=bgColor)
    dsDanhMuc_lb.place(x=10, y=300, width=140, height=20)
    dsSanPham_tableFrame = Frame(qlDM_frame, bg='white', bd=2, relief=RIDGE)
    dsSanPham_tableFrame.place(x=10, y=320, width=980, height=290)
    
    scroll_x = ttk.Scrollbar(dsSanPham_tableFrame,orient=HORIZONTAL)
    scroll_y = ttk.Scrollbar(dsSanPham_tableFrame,orient=VERTICAL)
    
    self.thongTinSP_table = ttk.Treeview(dsSanPham_tableFrame, column=('maSanPham', 'sanPham', 'donViTinh', 'nguonGoc', 'gia', 'kho', 'giaGoc', 'ngayNhap'),
                                         xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
    
    scroll_x.pack(side=BOTTOM, fill=X)
    scroll_y.pack(side=RIGHT, fill=Y)
    
    scroll_x.config(command=self.thongTinSP_table.xview)
    scroll_y.config(command=self.thongTinSP_table.yview)
    
    self.thongTinSP_table.heading('maSanPham', text='Mã Sản Phẩm')
    self.thongTinSP_table.heading('sanPham', text='Sản Phẩm')
    self.thongTinSP_table.heading('donViTinh', text='Đơn Vị Tính')
    self.thongTinSP_table.heading('nguonGoc', text='Nguồn Gốc')
    self.thongTinSP_table.heading('gia', text='Giá Bán')   
    self.thongTinSP_table.heading('kho', text='Kho')
    self.thongTinSP_table.heading('giaGoc', text='Giá Nhập')
    self.thongTinSP_table.heading('ngayNhap', text='Ngày Nhập')
    
    
    self.thongTinSP_table['show'] = 'headings'
    
    self.thongTinSP_table.column('maSanPham', width=100)
    self.thongTinSP_table.column('sanPham', width=100)
    self.thongTinSP_table.column('donViTinh', width=50)
    self.thongTinSP_table.column('nguonGoc', width=75)
    self.thongTinSP_table.column('gia', width=100)
    self.thongTinSP_table.column('kho', width=50)
    self.thongTinSP_table.column('giaGoc', width=75)
    self.thongTinSP_table.column('ngayNhap', width=75)
    
    self.thongTinSP_table.pack(fill=BOTH, expand=1)
    
    self.thongTinDM_table.bind("<ButtonRelease-1>", self.get_cursor)
    self.load_danhmuc()
  
  def load_danhmuc(self):
    conn = pyodbc.connect(database_QLBH[0])
    my_cursor = conn.cursor()
    my_cursor.execute("select* from DANHMUC where TRANGTHAI not in ('DELETED')")
    rows = my_cursor.fetchall()
    self.thongTinDM_table.delete(*self.thongTinDM_table.get_children())
    if len(rows)!=0:
      for i in rows:
        list=[]
        for j in range(0,2):
          list.append(i[j])
        self.thongTinDM_table.insert('', END, values=list)
      conn.commit()
    conn.close()
  
  def load_sanpham(self):
    conn = pyodbc.connect(database_QLBH[0])
    my_cursor = conn.cursor()
    my_cursor.execute("select* from SANPHAM where TRANGTHAI not in ('DELETED') and MADM=?", self.var_madm.get())
    rows = my_cursor.fetchall()
    self.thongTinSP_table.delete(*self.thongTinSP_table.get_children())
    if len(rows)!=0:
      for i in rows:
        list=[]
        for j in range(1, 10):
          list.append(i[j])
        self.thongTinSP_table.insert('', END, values=list)
      conn.commit()
    conn.close()
    
  def get_cursor(self, event=''):
    cursor_row = self.thongTinDM_table.focus()
    content = self.thongTinDM_table.item(cursor_row)
    row=content['values']
    if row !="":
      self.var_madm.set(row[0])
      self.var_tendm.set(row[1])
      
  def add_danhmuc(self):
    if self.var_madm.get()=='':
      messagebox.showerror('Error', 'Vui lòng nhập mã danh mục!',parent= self.root)
    else:
      try:
        conn = pyodbc.connect(database_QLBH[0])
        my_cursor = conn.cursor()
        my_cursor.execute("select MADM from DANHMUC")
        rows = my_cursor.fetchall()
        for i in rows:
           if self.var_madm.get() == i[0]:
            messagebox.showerror('Error', 'Mã Danh Mục Đã Tồn Tại!', parent=self.root)
            return 0
        my_cursor = conn.cursor()
        my_cursor.execute('insert into DANHMUC values(?,?,?)',
                          self.var_madm.get(),
                          self.var_tendm.get(),
                          'ACTION'
                        )
        conn.commit()
        messagebox.showinfo('Success', 'Thêm Danh Mục Thành Công', parent = self.root)
        self.load_danhmuc()
        conn.close()
        self.reset_danhmuc()
      except Exception as e:
        messagebox.showwarning('Warning', f'Xuất hiện một số vấn đề: {str(e)}', parent=self.root)
  
  def update_danhmuc(self):
    if self.var_madm.get() =='':
      messagebox.showerror('Error', 'Vui lòng nhập mã danh mục!',parent= self.root)
    else:
      try:
        conn = pyodbc.connect(database_QLBH[0])
        my_cursor = conn.cursor()
        my_cursor.execute("select MADM from DANHMUC")
        rows = my_cursor.fetchall()
        flag=0
        for i in rows:
           if self.var_madm.get() != i[0]:
             flag +=1
        if flag == len(rows):
          messagebox.showerror('Error', 'Mã Danh Mục Không Tồn Tại!', parent=self.root)
          return 0
          
        my_cursor = conn.cursor()
        my_cursor.execute('update DANHMUC set TENDM=? WHERE MADM=?',
                        self.var_tendm.get(),
                        self.var_madm.get())
        conn.commit()
        messagebox.showinfo('Success', 'Cập Nhật Danh Mục Thành Công', parent = self.root)
        self.load_danhmuc()
        conn.close()
        self.reset_danhmuc()
      except Exception as e:
        messagebox.showwarning('Warning', f'Xuất hiện một số vấn đề: {str(e)}', parent=self.root)
  
  def delete_danhmuc(self):
    if self.var_madm.get() =='':
      messagebox.showerror('Error', 'Vui lòng nhập mã danh mục',parent= self.root)
    else:
      try:
        delete_data= messagebox.askyesno('Hệ Thống Quản Lý Bán Hàng', 'Bạn có chắc muốn xóa danh mục này?', parent=self.root)
        if delete_data>0:
          conn = pyodbc.connect(database_QLBH[0])
          my_cursor = conn.cursor()
          my_cursor.execute("update DANHMUC set TRANGTHAI='DELETED' WHERE MADM=?", self.var_madm.get())
          messagebox.showinfo('Delete', 'Xóa thành công!',parent=self.root)
          conn.commit()
          self.load_danhmuc()
          conn.close()
          self.reset_danhmuc()
      except Exception as e:
        messagebox.showwarning('Warning', f'Xuất hiện một số vấn đề: {str(e)}', parent=self.root)
  
  def reset_danhmuc(self):
    self.var_madm.set('')
    self.var_tendm.set('')
    self.thongTinSP_table.delete(*self.thongTinSP_table.get_children())
  
  def search(self, event):
    if self.var_searchCombobox.get()=="MADM":
      select_column=0
    elif self.var_searchCombobox.get()=="TENDM":
      select_column=1
    
    select_from= "DANHMUC"
    if event.keysym == 'BackSpace':
        query=self.var_search.get()[:-1]
    else:
      query=self.var_search.get()+event.char
    ds = get_dataSQL(select_from)
    options=[i[select_column] for i in ds]
    ds_index=search_index(query, options)
    
    if len(ds_index)!=0:
      self.thongTinDM_table.delete(*self.thongTinDM_table.get_children())
      for i in ds_index:
        list=[]
        for j in range(0,3):
          list.append(ds[i][j])
        self.thongTinDM_table.insert('', END, values=list)
    elif len(query)<1:
      self.load_danhmuc()
  
  def sanPham(self):
    new_window=Toplevel(self.root)
    dk = qlSP_win(new_window, self.var_madm.get())
    
    
if __name__ == "__main__":
  root = Tk()
  ojb = qlDM_win(root)
  root.mainloop()      
  