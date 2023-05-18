from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import pyodbc
import sys
sys.path.append('E:\hk2_namII\TuHoc\QuanLiBanHang')
from sqlConnect import*


f = font=("times new roman", 12)
bgColor = '#f3d8d6'
fgColor = "#fefffa"

class duyet_win:
  def __init__(self, root):
    self.root = root
    # self.root.geometry("1000x620+250+40")
    # self.root.overrideredirect(True)
     
    duyetTK_frame = Frame(self.root, bg=bgColor)
    duyetTK_frame.place(x=0, y=0, width=1000, height=620)
    
      #biến qlsp
    self.var_userid = StringVar()
    self.var_username = StringVar()
    self.var_pass = StringVar()
    self.var_ten = StringVar()
    self.var_sdt = StringVar()
    self.var_cmnd = StringVar()
    self.var_email = StringVar()
    self.var_diachi = StringVar()
    self.var_phanquyen = StringVar()
    self.var_ngayDK = StringVar()
    self.duongdan = StringVar()
    
    #================== search ============================
    search_lb = Label(duyetTK_frame, text="Tìm Kiếm", bg='#89cff0', font=f)
    search_lb.place(x=550, y=20, width=70,height=30)
        
    self.var_searchCombobox = StringVar()
    search_combo = ttk.Combobox(duyetTK_frame, textvariable=self.var_searchCombobox, state='readonly', font=f, width=23)
    search_combo["value"]=('USER_NAME', 'SDT')
    search_combo.current(0)
    search_combo.place(x=625, y=20, width=100, height=30)
    
    self.var_search = StringVar()
    search_txt = ttk.Entry(duyetTK_frame, textvariable=self.var_search, font=f)
    search_txt.bind("<KeyPress>", self.search)
    search_txt.place(x=730, y=20, width=250, height=30)
   
    # ==================== frame ttsp =======================
    thongTinTK_frame= LabelFrame(duyetTK_frame, bg=bgColor, text="Tài Khoản Chờ Duyệt", font=("times new roman", 18, "bold"), bd=4, relief=RIDGE)
    thongTinTK_frame.place(x=10,y=50, width=980, height=260)
    
      #chức năng
    duyet_btn = Button(thongTinTK_frame, text='Duyệt', command=self.add_data, bg='#89cff0',font=f)
    duyet_btn.place(x=610, y=190, width=75,height=30)
    
    xoa_btn = Button(thongTinTK_frame, text='Xóa', command=self.delete_data, bg='#89cff0',font=f)
    xoa_btn.place(x=700, y=190, width=75,height=30)
    
    capNhat_btn = Button(thongTinTK_frame, text='Cập Nhật', command=self.update_data, bg='#89cff0',font=f)
    capNhat_btn.place(x=790, y=190, width=75,height=30)
    
    lamMoi_btn = Button(thongTinTK_frame, text='Làm Mới', command=self.reset_data, bg='#89cff0',font=f)
    lamMoi_btn.place(x=880, y=190, width=75,height=30)
    
      #thông tin sản phẩm
      #column 0
    user_id_lb = Label(thongTinTK_frame, text='USER_ID:', font=f, bg=bgColor)
    user_id_lb.place(x=10, y=30, height=30)
    user_id_txt = ttk.Entry(thongTinTK_frame, textvariable=self.var_userid, font=f)
    user_id_txt.place(x=110, y=30, width=200, height=30)
    
    username_lb = Label(thongTinTK_frame, text='Tên Đăng Nhập:', font=f, bg=bgColor)
    username_lb.place(x=10, y=80, height=30)
    username_txt = ttk.Entry(thongTinTK_frame, textvariable=self.var_username, font=f)
    username_txt.place(x=110, y=80, width=200, height=30)
    
    pass_lb = Label(thongTinTK_frame, text='Mật Khẩu:', font=f, bg=bgColor)
    pass_lb.place(x=10, y=130, height=30)
    pass_txt = ttk.Entry(thongTinTK_frame, textvariable=self.var_pass, font=f)
    pass_txt.place(x=110, y=130, width=200, height=30)
    
    permission_lb = Label(thongTinTK_frame, text='Phân Quyền:', font=f, bg=bgColor)
    permission_lb.place(x=10, y=180, height=30)
    permission_txt = Entry(thongTinTK_frame, textvariable=self.var_phanquyen, font=f, state='readonly')
    permission_txt.place(x=110, y=180, width=200, height=30)
    
    
        #column 1
    fullname_lb = Label(thongTinTK_frame, text="Tên:", font=f, bg=bgColor)
    fullname_lb.place(x=360, y=30, height=30)
    fullname_txt = ttk.Entry(thongTinTK_frame, textvariable=self.var_ten, font=f)
    fullname_txt.place(x=420, y=30, width=200, height=30)
    
    
    sdt_lb = Label(thongTinTK_frame, text='SDT:', font=f, bg=bgColor)
    sdt_lb.place(x=360, y=80, height=30)
    sdt_txt = ttk.Entry(thongTinTK_frame, textvariable=self.var_sdt, font=f)
    sdt_txt.place(x=420, y=80, width=200, height=30)
    
    cmnd_lb = Label(thongTinTK_frame, text='CMND:', font=f, bg=bgColor)
    cmnd_lb.place(x=360, y=130, height=30)
    cmnd_txt = ttk.Entry(thongTinTK_frame, textvariable=self.var_cmnd, font=f)
    cmnd_txt.place(x=420, y=130, width=200, height=30)
    
    path_lb = Label(thongTinTK_frame, text='Ảnh:', font=f, bg=bgColor)
    path_lb.place(x=360, y=180, height=30)
    path_txt = ttk.Entry(thongTinTK_frame, textvariable=self.duongdan, font=f)
    path_txt.place(x=420, y=180, width=170, height=30)
    #column 2
    email_lb = Label(thongTinTK_frame, text='Email:', font=f, bg=bgColor)
    email_lb.place(x=670, y=30, height=30)
    email_txt = ttk.Entry(thongTinTK_frame, textvariable=self.var_email, font=f)
    email_txt.place(x=750,y=30, width=200, height=30)
    
    diachi_lb = Label(thongTinTK_frame, text='Địa Chỉ:', font=f, bg=bgColor)
    diachi_lb.place(x=670, y=80, height=30)
    diachi_txt = ttk.Entry(thongTinTK_frame, textvariable=self.var_diachi, font=f)
    diachi_txt.place(x=750,y=80, width=200, height=30)
    
    ngay_lb = Label(thongTinTK_frame, text='Ngày ĐK:', font=f, bg=bgColor)
    ngay_lb.place(x=670, y=130, height=30)
    ngay_txt = ttk.Entry(thongTinTK_frame, textvariable=self.var_ngayDK, font=f)
    ngay_txt.place(x=750,y=130, width=200, height=30)
    
   
    # =================== table sanpham ===============
    dsTaiKhoan_tableFrame = Frame(duyetTK_frame, bg='white', bd=2, relief=RIDGE)
    dsTaiKhoan_tableFrame.place(x=10, y=320, width=980, height=290)
    
    scroll_x = ttk.Scrollbar(dsTaiKhoan_tableFrame,orient=HORIZONTAL)
    scroll_y = ttk.Scrollbar(dsTaiKhoan_tableFrame,orient=VERTICAL)
    
    self.thongTinTK_table = ttk.Treeview(dsTaiKhoan_tableFrame, column=('username', 'pass', 'ten', 'sdt', 'cmnd', 'email',\
                                                                        'diachi', 'phanquyen', 'ngaydk', 'hinhanh'),
                                         xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
    
    scroll_x.pack(side=BOTTOM, fill=X)
    scroll_y.pack(side=RIGHT, fill=Y)
    
    scroll_x.config(command=self.thongTinTK_table.xview)
    scroll_y.config(command=self.thongTinTK_table.yview)
    
    self.thongTinTK_table.heading('username', text='Tên Đăng Nhập')
    self.thongTinTK_table.heading('pass', text='Mật Khẩu')   
    self.thongTinTK_table.heading('ten', text='Họ Tên')
    self.thongTinTK_table.heading('email', text='Email')
    self.thongTinTK_table.heading('sdt', text='SDT')
    self.thongTinTK_table.heading('cmnd', text='CMND')
    self.thongTinTK_table.heading('diachi', text='Địa Chỉ')
    self.thongTinTK_table.heading('phanquyen', text='Phân Quyền')
    self.thongTinTK_table.heading('ngaydk', text='Ngày Đăng Ký')
    self.thongTinTK_table.heading('hinhanh', text='Đường dẫn')
    
    
    
    self.thongTinTK_table['show'] = 'headings'
    
    self.thongTinTK_table.column('username', width=100, anchor=CENTER)
    self.thongTinTK_table.column('pass', width=75, anchor=CENTER)
    self.thongTinTK_table.column('ten', width=100, anchor=CENTER)
    self.thongTinTK_table.column('email', width=75, anchor=CENTER)
    self.thongTinTK_table.column('sdt', width=75, anchor=CENTER)
    self.thongTinTK_table.column('cmnd', width=100, anchor=CENTER)
    self.thongTinTK_table.column('diachi', width=100, anchor=CENTER)
    self.thongTinTK_table.column('ngaydk', width=100, anchor=CENTER)
    self.thongTinTK_table.column('phanquyen', width=100, anchor=CENTER)
    self.thongTinTK_table.column('hinhanh', width=100, anchor=CENTER)
    
    self.thongTinTK_table.pack(fill=BOTH, expand=1)
    self.thongTinTK_table.bind("<ButtonRelease-1>", self.get_cursor)
    self.load_table()
    
 
      
  def load_table(self):
    conn = pyodbc.connect(database_QLBH[0])
    my_cursor = conn.cursor()
    my_cursor.execute("select* from REGISTER")
    rows = my_cursor.fetchall()
    
    self.thongTinTK_table.delete(*self.thongTinTK_table.get_children())
    if len(rows)!=0:
      for i in rows:
        list=[]
        for j in range(0,10):
          list.append(i[j])
        self.thongTinTK_table.insert('', END, values=list)
      conn.commit()
    conn.close()
    
  def get_cursor(self, event=''):
    cursor_row = self.thongTinTK_table.focus()
    content = self.thongTinTK_table.item(cursor_row)
    row=content['values']
    if row !="":
      self.var_username.set(row[0])
      self.var_pass.set(row[1])
      self.var_ten.set(row[2])
      self.var_sdt.set('0'+str(row[3]))
      self.var_cmnd.set('0'+str(row[4]))
      self.var_email.set(row[5])
      self.var_diachi.set(row[6])
      self.var_phanquyen.set(row[7])
      self.var_ngayDK.set(row[8])
      self.duongdan.set(row[9])
      
      conn = pyodbc.connect(database_QLBH[0])
      my_cursor = conn.cursor()
      if row[7]=='Nhân Viên':
        my_cursor.execute("select COUNT(USER_ID) FROM TAIKHOAN WHERE PHANQUYEN not in ('Nhân viên')")
      else:
        my_cursor.execute("select COUNT(USER_ID) FROM TAIKHOAN WHERE PHANQUYEN='Nhân viên'")
      my_cursor.execute("select COUNT(USER_ID) FROM TAIKHOAN WHERE PHANQUYEN='Nhân viên'")
      
      ref = int(my_cursor.fetchall()[0][0])
      print(ref)
      
      if self.var_phanquyen.get() == 'Nhân Viên':
        if ref < 10:
          id = 'NV_0000'
        elif ref < 100:
          id = 'NV_000'
        elif ref < 1000:
          id = 'NV_00'
        else: id = 'NV_0'
      else:
        if ref < 10:
          id = 'AD_0000'
        elif ref < 100:
          id = 'AD_000'
        elif ref < 1000:
          id = 'AD_00'
        else: id = 'AD_0'
      self.var_userid.set(id+str(ref+1))  
      
  def add_data(self):
    if self.var_username.get() =='' or self.var_userid.get()=='':
      messagebox.showerror('Error', 'Vui lòng nhập đủ thông tin!',parent= self.root)
    else:
      try:
        conn = pyodbc.connect(database_QLBH[0])
        my_cursor = conn.cursor()
        my_cursor.execute('insert into TAIKHOAN values(?,?,?,?,?,?,?,?,?,?)',
                          self.var_userid.get(),
                          self.var_ten.get(),
                          self.var_sdt.get(),
                          self.var_cmnd.get(),
                          self.var_email.get(),
                          self.var_diachi.get(),
                          self.var_phanquyen.get(),
                          self.var_ngayDK.get(),
                          'ACTION',
                          self.duongdan.get()
                          )
        my_cursor = conn.cursor()
        my_cursor.execute('insert into ACCOUNT values(?,?,?)',
                          self.var_username.get(),
                          self.var_pass.get(),
                          self.var_userid.get()
                          )
        conn.commit()
        messagebox.showinfo('Success', 'Thêm Tài Khoản Thành Công', parent = self.root)
        self.delete_dk(0)
        conn.close()
      except Exception as e:
        messagebox.showwarning('Warning', f'Xuất hiện một số vấn đề: {str(e)}', parent=self.root)
  
  def update_data(self):
    if self.var_username.get() =='' or self.var_userid.get()=='':
      messagebox.showerror('Error', 'Vui lòng nhập đủ thông tin!',parent= self.root)
    else:
      try:
        conn = pyodbc.connect(database_QLBH[0])
        my_cursor = conn.cursor()
        my_cursor.execute('update REGISTER set PASS=?, FULLNAME=?, SDT=?, CMND=?, EMAIL=?, DIACHI=?, PHANQUYEN=?, NGAYDK=?, HINHANH=? WHERE USER_NAME=?',
                          self.var_pass.get(),
                          self.var_ten.get(),
                          self.var_sdt.get(),
                          self.var_cmnd.get(),
                          self.var_email.get(),
                          self.var_diachi.get(),
                          self.var_phanquyen.get(),
                          self.var_ngayDK.get(),
                          self.duongdan.get(),
                          self.var_username.get()
                          )
        conn.commit()
        messagebox.showinfo('Success', 'Cập Nhật Thông Tin Thành Công', parent = self.root)
        conn.close()
        self.load_table()
        self.reset_data()
      except Exception as e:
        messagebox.showwarning('Warning', f'Xuất hiện một số vấn đề: {str(e)}', parent=self.root)
  
  def delete_data(self):
    self.delete_dk(1)
    
  def delete_dk(self, flag):
    if self.var_username.get() !='' and self.var_userid.get()!='':
      try:
        conn = pyodbc.connect(database_QLBH[0])
        if flag==1:
          temp = messagebox.askyesno('Hệ Thống Quản Lý Bán Hàng', 'Bạn có chắc muốn xóa người đăng ký này?', parent=self.root)
          if temp>0:
            messagebox.showinfo('Delete', 'Xóa thành công!',parent=self.root)
            my_cursor = conn.cursor()
            my_cursor.execute("delete from REGISTER WHERE USER_NAME=?", self.var_username.get())
        else:
          my_cursor = conn.cursor()
          my_cursor.execute("delete from REGISTER WHERE USER_NAME=?", self.var_username.get())
        conn.commit()
        conn.close()
        self.load_table()
        self.reset_data()
      except Exception as e:
        messagebox.showwarning('Warning', f'Xuất hiện một số vấn đề: {str(e)}', parent=self.root)
    else:
      messagebox.showerror('Error', 'Vui lòng nhập đủ thông tin!',parent= self.root)
      
  def reset_data(self):
    self.var_userid.set(''),
    self.var_username.set(''),
    self.var_cmnd.set(''),
    self.var_sdt.set(''),
    self.var_email.set(''),
    self.var_diachi.set(''),
    self.var_pass.set(''),
    self.var_phanquyen.set('Nhân Viên'),
    self.var_ngayDK.set(''),
    self.var_ten.set('')
    self.duongdan.set('')
  
  def search(self, event):
    if self.var_searchCombobox.get()=="USER_NAME":
      select_column=0
    elif self.var_searchCombobox.get()=="SDT":
      select_column=3
    
    select_from= "REGISTER"
    if event.keysym == 'BackSpace':
        query=self.var_search.get()[:-1]
    else:
      query=self.var_search.get()+event.char
    
    conn = pyodbc.connect(database_QLBH[0])
    my_cursor = conn.cursor()
    my_cursor.execute('select* from '+select_from)
    ds = my_cursor.fetchall()
    conn.commit()
    conn.close()
    
    # ds = get_dataSQL(select_from)
    options=[i[select_column] for i in ds]
    ds_index=search_index(query, options)
    
    if len(ds_index)!=0:
      self.thongTinTK_table.delete(*self.thongTinTK_table.get_children())
      for i in ds_index:
        list=[]
        for j in range(0,10):
          list.append(ds[i][j])
        self.thongTinTK_table.insert('', END, values=list)
    elif len(query)<1:
      self.load_table()

if __name__ == "__main__":
  root = Tk()
  ojb = duyet_win(root)
  root.mainloop()      
  

        