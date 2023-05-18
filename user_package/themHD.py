from tkinter import*
from tkinter import ttk
import sys
sys.path.append('E:\hk2_namII\TuHoc\QuanLiBanHang')
from sqlConnect import*
from tkinter import messagebox
import pyodbc
from datetime import datetime


f = font=("times new roman", 12)
bgColor = '#f3d8d6'
fgColor = "#fefffa"


class themHD_win:
  def __init__(self, root, userID):
    self.root = root
    self.userID = userID  
    self.root.geometry("990x595+220+75")
    self.root.overrideredirect(True)
    
    themHD_frame = Frame(root, bg=bgColor)
    themHD_frame.place(x=0, y=0, width=990, height=595)
      
    # ==================== task bar ===================
    taskbar_frame = Frame(themHD_frame)
    taskbar_frame.place(x=0, y=0, width=990, height=30)
  
    lb_title = Label(taskbar_frame, text="Thêm hóa đơn",  font=("times new roman", 10, "bold"), borderwidth=0)
    lb_title.place(x=5, y=0, height=30)
    
    btn_exit = Button(taskbar_frame, text="✖", command=root.destroy, font= ("times new roman", 16, "bold"), bd=3, fg='red')
    btn_exit.place(x=950, y=0, width=50, height=30)
    
    #===================== Sản phẩm frame =============
    sanPham_frame = Frame(themHD_frame, bg='white')
    sanPham_frame.place(x=10, y=40, width=600, height=545)
    
    #==================== Thông tin sản phẩm frame ================
    ttsp_frame = Frame(sanPham_frame, bg=bgColor)
    ttsp_frame.place(x=10, y=10, width=580, height=280)
    
    #=================== Thông tin sản phẩm =====================
    
    
    
    #===================== variable sản phẩm ==============
    self.var_tenSP = StringVar()
    self.var_soLuong = StringVar()
    self.var_soLuong.set(0)
    self.var_donGia = StringVar()
    self.var_donGia.set(0)
    self.var_giamGia = StringVar()
    self.var_giamGia.set(0)
    self.var_thanhTien = StringVar()
    self.var_masp = StringVar()
    
    self.saved_sluong = IntVar()
    
    
    #================ +_+ ===============
    self.var_maCTHD = StringVar()
    self.var_maCTHD.set(self.set_maCT())
    maCTHD = ttk.Entry(ttsp_frame, textvariable=self.var_maCTHD,state='readonly', font=f)
    maCTHD.place(x=10, y=5, width=75, height=30)
    
    #search
    search_lb = Label(ttsp_frame, text="Tìm Kiếm", bg='#89cff0', font=f)
    search_lb.place(x=165, y=5, width=70,height=30)
      
    self.var_searchCombobox = StringVar()
    search_combo = ttk.Combobox(ttsp_frame,textvariable=self.var_searchCombobox, state='readonly', font=f, width=23)
    search_combo["value"]=('MASP', 'TENSP', 'MADM')
    search_combo.current(0)
    search_combo.place(x=235, y=5, width=75, height=30)
    
    self.var_search = StringVar()
    search_txt = ttk.Entry(ttsp_frame, textvariable=self.var_search, font=f)
    search_txt.place(x=310, y=5, width=250, height=30)
    search_txt.bind("<KeyPress>", self.search)
    #================== Kho ================
    dsKho_tableFrame = Frame(ttsp_frame, bg='white')
    dsKho_tableFrame.place(x=10, y=45, width=555, height=110)
    
    #================== Bảng Sản Phẩm ======================
    
    scroll_x = ttk.Scrollbar(dsKho_tableFrame, orient=HORIZONTAL)
    scroll_y = ttk.Scrollbar(dsKho_tableFrame, orient=VERTICAL)
    
    self.thongTinKho_table = ttk.Treeview(dsKho_tableFrame,column=('maSP', 'tenSP', 'soLuong', 'donGia', 'donViTinh'),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
    
    scroll_x.pack(fill=X, side=BOTTOM)
    scroll_y.pack(fill=Y, side=RIGHT)
    
    scroll_x.config(command=self.thongTinKho_table.xview)
    scroll_y.config(command=self.thongTinKho_table.yview)
    self.thongTinKho_table.heading('maSP', text='Mã SP', anchor=CENTER)
    self.thongTinKho_table.heading('tenSP', text='Tên SP', anchor=CENTER)
    self.thongTinKho_table.heading('soLuong', text='SLuong', anchor=CENTER)
    self.thongTinKho_table.heading('donGia', text='Đơn Giá', anchor=CENTER)
    self.thongTinKho_table.heading('donViTinh', text='ĐVT', anchor=CENTER)
    
    self.thongTinKho_table.column('maSP', width=50)
    self.thongTinKho_table.column('tenSP', width=60, anchor=CENTER)
    self.thongTinKho_table.column('soLuong', width=40, anchor=CENTER)
    self.thongTinKho_table.column('donGia', width=50, anchor=CENTER)
    self.thongTinKho_table.column('donViTinh', width=50, anchor=CENTER)
    
    self.thongTinKho_table['show'] = 'headings'
    self.thongTinKho_table.bind('<ButtonRelease-1>', self.get_cursorKho)
    self.thongTinKho_table.pack(fill=BOTH, expand=1)
    
    #row 0
    masp_lb = Label(ttsp_frame, text='Mã SP', bg=bgColor, font=f)
    masp_lb.place(x=10, y=165, height=30)
    masp_txt = ttk.Entry(ttsp_frame, textvariable=self.var_masp, font=f)
    masp_txt.place(x=65, y=165, width=125, height=30)
    
    tensp_lb = Label(ttsp_frame, text="Tên SP", bg=bgColor, font=f)
    tensp_lb.place(x=200, y=165, height=30)
    tensp_txt = ttk.Entry(ttsp_frame, textvariable=self.var_tenSP, state='readonly', font=f)
    tensp_txt.place(x=255, y=165, width=125, height=30)
    
    donGia_lb = Label(ttsp_frame, text='Đơn Giá', bg=bgColor, font=f)
    donGia_lb.place(x=390, y=165, height=30)
    donGia_txt = ttk.Entry(ttsp_frame, textvariable=self.var_donGia, state='readonly', font=f)
    donGia_txt.place(x=450, y=165, width=120, height=30)
    
    #row 1
    giamGia_lb = Label(ttsp_frame, text='-%', font=f, bg=bgColor)
    giamGia_lb.place(x=10, y=205, width=25,height=30)
    giamGia_txt = ttk.Entry(ttsp_frame, textvariable=self.var_giamGia, font=f)
    giamGia_txt.place(x=50, y=205, width=95, height=30)
    giamGia_txt.bind("<KeyPress>", self.giam_event)
    
    soLuong_lb = Label(ttsp_frame, text='Số Lượng', bg=bgColor,font=f)
    soLuong_lb.place(x=170, y=205, height=30)
    soLuongGiam_btn = Button(ttsp_frame, command=self.sl_giam, text='-', font=f)
    soLuongGiam_btn.place(x=245,y=205, width=30,height=30)
    soLuong_txt = ttk.Entry(ttsp_frame, textvariable=self.var_soLuong, font=f)
    soLuong_txt.place(x=280, y=205, width=40, height=30)
    soLuong_txt.bind("<KeyPress>", self.sl_event)
    soLuongTang_btn = Button(ttsp_frame, command=self.sl_tang, text='+', font=f)
    soLuongTang_btn.place(x=325, y=205, width=30,height=30)
    
    thanhTien_lb = Label(ttsp_frame, text='Thành Tiền', bg=bgColor, font=f)
    thanhTien_lb.place(x=375, y=205, height=30)
    thanhTien_txt = ttk.Entry(ttsp_frame, textvariable=self.var_thanhTien, state='readonly', font=f)
    thanhTien_txt.place(x=450, y=205, width=120, height=30)
    
    #=================== chức năng ==================
    them_btn = Button(ttsp_frame,command=self.add_sp, text='Thêm', bg='#89cff0',font=f)
    them_btn.place(x=245, y=245, width=75,height=30)
    
    xoa_btn = Button(ttsp_frame, text='Xóa', command=self.delete_sp, bg='#89cff0',font=f)
    xoa_btn.place(x=330, y=245, width=75,height=30)
    
    capNhat_btn = Button(ttsp_frame, text='Cập Nhật', command=self.update_sp, bg='#89cff0',font=f)
    capNhat_btn.place(x=415, y=245, width=75,height=30)
    
    self.lamMoi_btn = Button(ttsp_frame, text='Làm Mới',command=self.reset_sp, bg='#89cff0',font=f)
    self.lamMoi_btn.place(x=500, y=245, width=75,height=30)
    self.lamMoi_btn.bind("<Button-1>", self.clear_focus)
    
    
    #================== Danh Sách Sản Phẩm Hóa Đơn ================
    dsSanPham_tableFrame = LabelFrame(sanPham_frame, text='Sản Phẩm Hóa Đơn', bd=4, relief=RIDGE, font=f, bg='white')
    dsSanPham_tableFrame.place(x=10, y=295, width=580, height=240)
    
    #================== Bảng Sản Phẩm ======================
    
    scroll_x = ttk.Scrollbar(dsSanPham_tableFrame, orient=HORIZONTAL)
    scroll_y = ttk.Scrollbar(dsSanPham_tableFrame, orient=VERTICAL)
    
    self.thongTinSP_table = ttk.Treeview(dsSanPham_tableFrame,column=('maCTHD', 'maSP', 'tenSP', 'soLuong', 'donGia', 'donViTinh', 'giamGia','thanhTien'),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
    
    scroll_x.pack(fill=X, side=BOTTOM)
    scroll_y.pack(fill=Y, side=RIGHT)
    
    scroll_x.config(command=self.thongTinSP_table.xview)
    scroll_y.config(command=self.thongTinSP_table.yview)
    self.thongTinSP_table.heading('maCTHD', text='Mã CTHD', anchor=CENTER)
    self.thongTinSP_table.heading('maSP', text='Mã SP', anchor=CENTER)
    self.thongTinSP_table.heading('tenSP', text='Tên SP', anchor=CENTER)
    self.thongTinSP_table.heading('soLuong', text='SLuong', anchor=CENTER)
    self.thongTinSP_table.heading('donGia', text='Đơn Giá', anchor=CENTER)
    self.thongTinSP_table.heading('donViTinh', text='ĐVT', anchor=CENTER)
    self.thongTinSP_table.heading('giamGia', text='Tiền Giảm', anchor=CENTER)
    self.thongTinSP_table.heading('thanhTien', text='Thành Tiền', anchor=CENTER)
    
    self.thongTinSP_table.column('maCTHD', width=60, anchor=CENTER)
    self.thongTinSP_table.column('maSP', width=50)
    self.thongTinSP_table.column('tenSP', width=60, anchor=CENTER)
    self.thongTinSP_table.column('soLuong', width=40, anchor=CENTER)
    self.thongTinSP_table.column('donGia', width=50, anchor=CENTER)
    self.thongTinSP_table.column('donViTinh', width=50, anchor=CENTER)
    self.thongTinSP_table.column('giamGia', width=65, anchor=CENTER)
    self.thongTinSP_table.column('thanhTien', width=75, anchor=CENTER)
    
    self.thongTinSP_table['show'] = 'headings'
    self.thongTinSP_table.bind('<ButtonRelease-1>', self.get_cursor)
    self.thongTinSP_table.pack(fill=BOTH, expand=1)
    
      
      
    #===================== Thông tin đơn hàng ==================
    
    #=================== variables =================
    self.var_maDH = StringVar()
    self.var_maDH.set(self.set_maDH())
    
    self.var_thoiGian = StringVar()
    current_datetime = datetime.now()
    current_date = str(current_datetime.day)+'-'+str(current_datetime.month)+'-'+str(current_datetime.year)
    self.var_thoiGian.set(current_date)
    
    self.var_maKH = StringVar()
    self.var_ghiChu = StringVar()
    
    #===================== +_+ ===============
    ttdh_frame = Frame(themHD_frame, bg=bgColor)
    ttdh_frame.place(x=610, y=40, width=380, height=565)
    
    #===================== đơn hàng frame ============
    donHang_frame = LabelFrame(ttdh_frame, text='Thông tin đơn hàng', bg='white', bd=4, relief='sunken', font=f)
    donHang_frame.place(x=10,y=0, width=360, height=290)
    
    maDon_lb = Label(donHang_frame, text='Mã Đơn Hàng', bg='white', font=f)
    maDon_lb.place(x=10, y=20, width=100, height=40)
    maDon_frame = Frame(donHang_frame, relief=RAISED, bd=2)
    maDon_frame.place(x=130, y=20, width=220,height=40)
    maDon_txt = ttk.Entry(maDon_frame, textvariable=self.var_maDH, state='readonly', font=f)
    maDon_txt.place(x=2, y=1, width=210,height=32)
    
    maKH_lb = Label(donHang_frame, text='Mã Khách Hàng', bg='white', font=f)
    maKH_lb.place(x=10, y=80, width=110, height=40)
    maKH_frame = Frame(donHang_frame, relief=RAISED, bd=2)
    maKH_frame.place(x=130, y=80, width=220,height=40)
    maKH_txt = ttk.Entry(maKH_frame, textvariable=self.var_maKH, font=f)
    maKH_txt.place(x=2,y=1, width=210, height=32)
    
    thoiGian_lb = Label(donHang_frame, text='Thời Gian:', bg='white', font=f)
    thoiGian_lb.place(x=10, y=140, width=70, height=30)
    thoiGian_frame = Frame(donHang_frame, relief=RAISED, bd=2)
    thoiGian_frame.place(x=125, y=140, width=220,height=40)
    thoiGian_txt = ttk.Entry(thoiGian_frame, textvariable=self.var_thoiGian, state='readonly', font=f)
    thoiGian_txt.place(x=2,y=1, width=210, height=32)
    
    ghiChu_lb = Label(donHang_frame, text='Ghi Chú:', bg='white', font=f)
    ghiChu_lb.place(x=10, y=200, width=65, height=30)
    ghiChu_frame = Frame(donHang_frame, relief=RAISED, bd=2)
    ghiChu_frame.place(x=125, y=200, width=220,height=40)
    ghiChu_txt = ttk.Entry(ghiChu_frame, textvariable=self.var_ghiChu, font=f)
    ghiChu_txt.place(x=2,y=1, width=210, height=32)
    
    
    #=================== thanh toán frame ================
    self.var_tongTien = IntVar()
    self.var_giamHD = StringVar()
    self.var_giamHD.set(0)
    self.var_conLai = IntVar()
    self.var_khachDua = StringVar()
    self.var_khachDua.set(0)
    self.var_traLai = IntVar()
    
    thanhToan_frame = LabelFrame(ttdh_frame, text='Thanh Toán', bg=bgColor, font=f, bd=4, relief=RAISED)
    thanhToan_frame.place(x=10, y=295, width=360, height=250)
    
    tongCong_lb = Label(thanhToan_frame, text='Tổng cộng:', bg=bgColor, font=f)
    tongCong_lb.place(x=10, y=5, width=70, height=30)
    tongCong_txt = ttk.Entry(thanhToan_frame, textvariable=self.var_tongTien, font=f)
    tongCong_txt.place(x=100, y=5, width=230, height=30)
    
    giam_lb = Label(thanhToan_frame, text='Giảm %:', bg=bgColor, font=f)
    giam_lb.place(x=10, y=40, height=30)
    giam_txt = ttk.Entry(thanhToan_frame, textvariable=self.var_giamHD, font=f)
    giam_txt.place(x=100, y=40, width=230, height=30)
    giam_txt.bind("<KeyPress>", self.giamHD_event)
    
    con_lb = Label(thanhToan_frame, text='Còn:', bg=bgColor, font=f)
    con_lb.place(x=10, y=80, width=30, height=30)
    con_txt = ttk.Entry(thanhToan_frame, textvariable=self.var_conLai, font=f)
    con_txt.place(x=100, y=80, width=230, height=30)
    
    khachDua_lb = Label(thanhToan_frame, text='Khách Đưa:', bg=bgColor, font=f)
    khachDua_lb.place(x=10, y=115, width=75, height=30)
    self.khachDua_txt = ttk.Entry(thanhToan_frame, textvariable=self.var_khachDua, font=f)
    self.khachDua_txt.place(x=100, y=115, width=230, height=30)
    self.khachDua_txt.bind("<KeyPress>", self.khachDua_event)
    
    thoiLai_lb = Label(thanhToan_frame, text='Trả Lại:', bg=bgColor, font=f)
    thoiLai_lb.place(x=10, y=150, width=50, height=30)
    thoiLai_txt = ttk.Entry(thanhToan_frame, textvariable=self.var_traLai, font=f)
    thoiLai_txt.place(x=100, y=150, width=230, height=30)
    
    huyHD_btn = Button(thanhToan_frame, text='Hủy Hóa Đơn', command=self.huyHDon , bg='#89cff0', font=f)
    huyHD_btn.place(x=110, y=185, width=115, height=30)
    
    thanhToan_btn = Button(thanhToan_frame, text='Thanh Toán', command=self.thanhToan, bg='#89cff0', font=f)
    thanhToan_btn.place(x=230, y=185, width=100, height=30)
    
    self.load_sp(self.var_maDH.get())
    self.load_kho()
    self.tongTien()
    
    
# ======================== Liên Kết Database ===================
   
   #================== xử lý hiển thị =============   
  def sl_event(self,event):
    if event.keysym == 'BackSpace':
      query=self.var_soLuong.get()[:-1]
    else:
      query=self.var_soLuong.get()+event.char
    if query=='':
      query=0
    try:
      conn = pyodbc.connect(database_QLBH[0])
      my_cursor = conn.cursor()
      my_cursor.execute("select SOLUONG from SANPHAM where MASP=?", self.var_masp.get())
      rows = my_cursor.fetchall()
      if len(rows)!=0:
        soluong=rows[0][0]
        if int(query) > soluong:
          messagebox.showerror('Error', 'Số lượng vượt quá phạm vi cho phép', parent=self.root)
          self.var_soLuong.set(0)
          return "break"
        else:
          self.tinhTien(query)
      conn.commit()
      conn.close()
    except Exception as e:
      messagebox.showwarning('Warning', f'Xuất hiện một số vấn đề: {str(e)}', parent = self.root)
    
  def giam_event(self, event):
    if event.keysym == 'BackSpace':
      query=self.var_giamGia.get()[:-1]
    else:
      query=self.var_giamGia.get()+event.char
    if query=='':
      query=0
    tien = int(self.var_donGia.get())*int(self.var_soLuong.get())
    thanhTien = int(tien) -int(query)*int(tien)//100
    self.var_thanhTien.set(thanhTien)
    
  
  def sl_tang(self):
    try:
      conn = pyodbc.connect(database_QLBH[0])
      my_cursor = conn.cursor()
      my_cursor.execute("select SOLUONG from SANPHAM where MASP=?", self.var_masp.get())
      rows = my_cursor.fetchall()
      if len(rows)!=0:
        soluong=rows[0][0]
        if int(self.var_soLuong.get()) + 1> soluong:
          messagebox.showerror('Error', 'Số lượng vượt quá phạm vi cho phép', parent=self.root)
        else:
          self.var_soLuong.set(str(int(self.var_soLuong.get())+1))
          self.tinhTien(self.var_soLuong.get())
      else:
        messagebox.showwarning('Warning', 'Vui lòng chọn sản phẩm', parent= self.root)
      conn.commit()
      conn.close()
    except Exception as e:
      messagebox.showwarning('Warning', f'Xuất hiện một số vấn đề: {str(e)}', parent = self.root)
      
  def sl_giam(self):
    if int(self.var_soLuong.get()) - 1 < 0:
      messagebox.showerror('Error', 'Số lượng vượt quá phạm vi cho phép', parent=self.root)
    else:
      self.var_soLuong.set(str(int(self.var_soLuong.get())-1))
      self.tinhTien(self.var_soLuong.get())
      
  def tinhTien(self, sl):
    tien = int(self.var_donGia.get())*int(sl)
    thanhTien = int(tien) -int(self.var_giamGia.get())*int(tien)//100
    
    self.var_thanhTien.set(thanhTien)
   
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
    ds = get_dataSQL(select_from)
    options=[i[select_column] for i in ds]
    ds_index=search_index(query, options)
    
    if len(ds_index)!=0:
      self.thongTinKho_table.delete(*self.thongTinKho_table.get_children())
      for i in ds_index:
        list=[]
        for j in range(1,6):
          if j == 4:
            continue
          if j == 3:
            list.append(ds[i][7])
            list.append(int(ds[i][3]))
            continue
          list.append(ds[i][j])
        self.thongTinKho_table.insert('', END, values=list)
    elif len(query)<1:
      self.load_kho()
  
  def load_kho(self):
    try:
      conn = pyodbc.connect(database_QLBH[0])
      my_cursor = conn.cursor()
      my_cursor.execute("select* from SANPHAM where TRANGTHAI='ACTION' and SOLUONG>0")
      rows = my_cursor.fetchall()
      self.thongTinKho_table.delete(*self.thongTinKho_table.get_children())
      if len(rows)!=0:
        for i in rows:
          list=[]
          for j in range(1,6):
            if j == 3:
              list.append(i[7])
              list.append(int(i[3]))
              continue
            if j == 4:
              continue
            list.append(i[j])
          self.thongTinKho_table.insert('', END, values=list)
        conn.commit()
      conn.close()
    except Exception as e:
      messagebox.showwarning('Warning', f'Xuất hiện một số vấn đề: {str(e)}', parent = self.root)
  
  def get_cursorKho(self, event=""):
    cursor_now = self.thongTinKho_table.focus()
    content = self.thongTinKho_table.item(cursor_now)
    rows=content['values']
    if rows != "":
      self.var_masp.set(rows[0])
      self.var_tenSP.set(rows[1])
      self.var_donGia.set(rows[3])
      self.var_soLuong.set(0)
    #xóa trạng thái focus của bảng Sản phẩm hóa đơn
    item2=self.thongTinSP_table.focus()
    self.thongTinSP_table.selection_remove(item2)
  
  def update_soluong(self, dk):
    #chỉnh số lượng sản phẩm
    conn = pyodbc.connect(database_QLBH[0])
    my_cursor = conn.cursor()
    my_cursor.execute("select SOLUONG from SANPHAM where MASP=?", self.var_masp.get())
    sluong = my_cursor.fetchall()[0][0]
    conn.commit()
    if dk == "add":
      slUpdate=sluong-int(self.var_soLuong.get())
    elif dk=="del":
      slUpdate=sluong+int(self.var_soLuong.get())
    else:
      slUpdate=sluong + self.saved_sluong.get() - int(self.var_soLuong.get())
        
    my_cursor = conn.cursor()
    my_cursor.execute("update SANPHAM set SOLUONG=? where MASP=?",slUpdate, self.var_masp.get())
    conn.commit()
    conn.close()
    self.load_kho()
  
  def clear_focus(self, event):
    item1=self.thongTinKho_table.focus()
    self.thongTinKho_table.selection_remove(item1)
    
    item2=self.thongTinSP_table.focus()
    self.thongTinSP_table.selection_remove(item2)
  
  #=============== xử lý chức năng ==============
  def reset_sp(self):
    self.var_maCTHD.set(self.set_maCT())
    self.var_masp.set('')
    self.var_tenSP.set('')
    self.var_soLuong.set(0)
    self.var_donGia.set(0)
    self.var_giamGia.set(0)
    self.var_thanhTien.set('')
    
  def load_sp(self,mahd):
    try:
      conn = pyodbc.connect(database_QLBH[0])
      my_cursor = conn.cursor()
      my_cursor.execute("select* from CTHD where TRANGTHAI not in ('DELETED') and SOHD=? and SOLUONG!=0", mahd)
      rows = my_cursor.fetchall()
      self.thongTinSP_table.delete(*self.thongTinSP_table.get_children())
      if len(rows)!=0:
        for i in rows:
          list = []
          for j in range (0, 6):
            if j == 1:
              continue
            elif j == 3:
              sp_cursor = conn.cursor()
              sp_cursor.execute('select TENSP from SANPHAM where MASP=?', list[1])
              tenSP = sp_cursor.fetchall()
              list.append(tenSP[0][0])
              list.append(i[j])
            elif j == 4:
              sp_cursor = conn.cursor()
              sp_cursor.execute('select GIA, DVT from SANPHAM where MASP=?', list[1])
              sp = sp_cursor.fetchall()
              gia = int(sp[0][0])
              dvt = sp[0][1]
              list.append(gia)
              list.append(dvt)
              list.append(int(i[j]))
            elif j == 5:
              list.append(int(i[j]) - list[6])
            else:
              list.append(i[j])
          self.thongTinSP_table.insert("", END, values=list)
        conn.commit()
      self.tongTien()
        
      conn.close()
    except Exception as e:
      messagebox.showwarning('Warning', f'Xuất hiện một số vấn đề: {str(e)}', parent = self.root)
      
  def add_sp(self):
    if self.var_masp.get() == "" or int(self.var_soLuong.get())==0:
      messagebox.showerror('Error', 'Vui lòng nhập đủ thông tin!', parent = self.root)
    else:
      try:
        self.taoHD()
        mact = self.set_maCT()
        giam = int(self.var_thanhTien.get())*int(self.var_giamGia.get())//100
        tien = int(self.var_thanhTien.get()) - giam
        
        conn = pyodbc.connect(database_QLBH[0])
        my_cursor = conn.cursor()
        my_cursor.execute('insert into CTHD values(?,?,?,?,?,?,?)',
        (
          mact,
          self.var_maDH.get(),
          self.var_masp.get(),
          int(self.var_soLuong.get()),
          giam,
          tien,
          'LOADING'
        ))
        conn.commit()
        conn.close()
        messagebox.showinfo('Success', 'Thêm Sản Phẩm thành công', parent = self.root)
        self.load_sp(self.var_maDH.get())
        self.tongTien()
        self.update_soluong("add")
        self.reset_sp()
      except Exception as e:
        messagebox.showwarning('Warning', f'Xuất hiện một số vấn đề: {str(e)}', parent = self.root)
  
  def update_sp(self):
    if self.var_maCTHD.get()=="":
      messagebox.showerror('Error', 'Không tốn tại mã chi tiết hóa đơn!', parent=self.root)
    else:
      try:
        giam = int(self.var_thanhTien.get())*int(self.var_giamGia.get())//100
        tien = int(self.var_thanhTien.get()) - giam
        conn = pyodbc.connect (database_QLBH[0])
        my_cursor = conn.cursor()
        my_cursor.execute('update CTHD set SOHD=?, MASP=?, SOLUONG=?, GIAM=?, THANHTIEN=? where MACTHD=?', 
                          (
                            self.var_maDH.get(),
                            self.var_masp.get(),
                            int(self.var_soLuong.get()),
                            giam,
                            tien,
                            self.var_maCTHD.get(),
                          ))
        conn.commit()
        self.load_sp(self.var_maDH.get())
        conn.close()
        messagebox.showinfo('Update', 'Cập nhật thành công!', parent=self.root)
        self.update_soluong("update")
        self.tongTien()
        self.reset_sp()
      except Exception as e:
        messagebox.showwarning('Warning', f'Xuất hiện một số vấn đề: {str(e)}', parent = self.root)
      
  def delete_sp(self):
    if self.var_maCTHD.get()=="":
      messagebox.showerror('Error', 'Không tốn tại CTHD không tồn tại!', parent=self.root)
    else: 
      delete_data= messagebox.askyesno('Hệ Thống Quản Lý Bán Hàng', 'Bạn có chắc muốn xóa CTHD này?', parent=self.root)
      if delete_data>0:
        try:
          conn = pyodbc.connect (database_QLBH[0])
          my_cursor = conn.cursor()
          my_cursor.execute("delete from CTHD where MACTHD=?", self.var_maCTHD.get())
          conn.commit()
          conn.close()
          messagebox.showinfo('Update', 'Xóa thành công!', parent=self.root)
          self.load_sp(self.var_maDH.get())
          self.update_soluong("del")
          self.tongTien()
          self.reset_sp()
        except Exception as e:
          messagebox.showwarning('Warning', f'Xuất hiện một số vấn đề: {str(e)}', parent = self.root)
        
  def get_cursor(self, event=""):
    cursor_now = self.thongTinSP_table.focus()
    content = self.thongTinSP_table.item(cursor_now)
    rows=content['values']
    if rows != "":
      self.var_maCTHD.set(rows[0])
      self.var_masp.set(rows[1])
      self.var_tenSP.set(rows[2])
      self.var_soLuong.set(rows[3])
      self.var_donGia.set(rows[4])
      self.var_giamGia.set(100//rows[7])
      self.var_thanhTien.set(rows[7])

      #dùng để lưu số lượng trước khi cập nhật
      self.saved_sluong.set(int(rows[3]))
    #xóa trạng thái focus của bảng Sản phẩm kho
    item1=self.thongTinKho_table.focus()
    self.thongTinKho_table.selection_remove(item1)
      
  #================== tạo mã hóa đơn ====================
  def taoHD(self):
    try:
      conn = pyodbc.connect(database_QLBH[0])
      my_cursor = conn.cursor()
      my_cursor.execute('select count(SOHD) from HOADON')
      temp1=my_cursor.fetchall()[0][0]
      temp2=self.var_maDH.get().split('HD')
      if int(temp2[1])>temp1:
        my_cursor.execute('insert into HOADON values(?,?,?,?,?,?)',
                          (
                            self.var_maDH.get(),
                            'KH00000',
                            datetime.now(),
                            '',
                            self.userID,
                            "LOADING"
                          ))
      conn.commit()
      conn.close()      
    except Exception as e:
      messagebox.showwarning('Warning', f'Xuất hiện một số vấn đề: {str(e)}', parent = self.root)

  def set_maDH(self):
    conn = pyodbc.connect(database_QLBH[0])
    my_cursor = conn.cursor()
    my_cursor.execute("select SOHD from HOADON where TRANGTHAI='LOADING'")
    rows= my_cursor.fetchall()
    if len(rows)!=0:
      return rows[0][0]
    my_cursor = conn.cursor()
    my_cursor.execute('select count(SOHD) from HOADON')
    count = my_cursor.fetchall()
    ref = count[0][0]+1
    if ref < 10:
      return 'HD0000' + str(ref)
    elif ref < 100:
      return 'HD000' + str(ref)
    elif ref < 1000:
      return 'HD00' + str(ref)
    return 'HD0' + str(ref)
  
  #=============== TẠO MÃ CHI TIẾT HÓA ĐƠN =============
  def set_maCT(self):
    conn = pyodbc.connect(database_QLBH[0])
    my_cursor = conn.cursor()
    my_cursor.execute('SELECT TOP 1 * FROM CTHD ORDER BY MACTHD DESC')
    count = my_cursor.fetchall()
    row = count[0][0]
    conn.close()
    if row != '':
      ref = row.split('CT')
    else:
      ref=['', 0]
    ref_cthd = int(ref[1]) + 1
    if ref_cthd < 10:
      return 'CT0000' + str(ref_cthd)
    elif ref_cthd < 100:
      return 'CT000' + str(ref_cthd)
    return 'CT00' + str(ref_cthd)
  
  #================ THANH TOÁN ===============
  def tongTien(self):
    sum=0
    for item in self.thongTinSP_table.get_children():
      tien = self.thongTinSP_table.item(item, "values")[7]
      sum+=int(tien)
    self.var_tongTien.set(sum)
    self.var_conLai.set(sum-int(self.var_giamHD.get()))
    self.var_traLai.set(int(self.var_khachDua.get())-int(self.var_conLai.get()))
    
  def giamHD_event(self, event):
    if event.keysym == 'BackSpace':
      query=self.var_giamHD.get()[:-1]
    else:
      query=self.var_giamHD.get()+event.char
    if query=='':
      query=0
    self.var_conLai.set(int(self.var_tongTien.get())-int(self.var_tongTien.get())*int(query)//100)
    self.var_traLai.set(int(self.var_khachDua.get()) -int(self.var_conLai.get()))
    if event.keysym == 'Return' or event.keysym == 'KP_Enter':
      self.khachDua_txt.focus_set()
    
  def khachDua_event(self, event):
    if event.keysym == 'BackSpace':
      query=self.var_khachDua.get()[:-1]
    else:
      query=self.var_khachDua.get()+event.char
    if query=='':
      query=0
    self.var_conLai.set(int(self.var_tongTien.get())-int(self.var_tongTien.get())*int(self.var_giamHD.get())//100)
    self.var_traLai.set(int(query) -int(self.var_conLai.get()))
  
  def reset_HD(self):
    self.reset_sp()
    self.var_maDH.set(self.set_maDH())
    self.var_maKH.set('')
    
    current_datetime = datetime.now()
    current_date = str(current_datetime.day)+'-'+str(current_datetime.month)+'-'+str(current_datetime.year)
    self.var_thoiGian.set(current_date)
    
    self.var_ghiChu.set('')
    self.var_tongTien.set(0)
    self.var_giamHD.set(0)
    self.var_conLai.set(0)
    self.var_khachDua.set(0)
    self.var_traLai.set(0)
  
  def thanhToan(self):
    if self.var_maKH.get() == "":
      makh ='KH00000'
    else:
      makh = self.var_maKH.get()
    nghd=datetime.now()
    try:
      conn = pyodbc.connect(database_QLBH[0])
      my_cursor = conn.cursor()
      my_cursor.execute('UPDATE HOADON set MAKH=?, NGHD=?, TRIGIA=?, MANV=?, TRANGTHAI=? where SOHD=?',
                        (
                          makh,
                          nghd,
                          # self.var_thoiGian.get(),
                          self.var_conLai.get(),
                          self.userID,
                          "ACTION",
                          self.var_maDH.get()
                        ))
      my_cursor = conn.cursor()
      my_cursor.execute("UPDATE CTHD set TRANGTHAI='ACTION' where SOHD=?",self.var_maDH.get())
      conn.commit()
      conn.close()
      messagebox.showinfo('Success', 'Thanh Toán Thành Công', parent = self.root)
      self.reset_HD()
      self.thongTinSP_table.delete(*self.thongTinSP_table.get_children())
      
    except Exception as e:
      messagebox.showwarning('Warning', f'Xuất hiện một số vấn đề: {str(e)}', parent = self.root)

  def huyHDon(self):
    if self.var_maDH.get()=="":
      messagebox.showerror('Error', 'Không tốn tại mã đơn hàng!', parent=self.root)
    else: 
      delete_data= messagebox.askyesno('Hệ Thống Quản Lý Bán Hàng', 'Bạn có chắc muốn hủy hóa đon này?', parent=self.root)
      if delete_data>0:
        try:
          conn = pyodbc.connect (database_QLBH[0])
          my_cursor = conn.cursor()
          my_cursor.execute("delete from CTHD where SOHD=?", self.var_maDH.get())
          my_cursor = conn.cursor()
          my_cursor.execute("delete from HOADON where SOHD=?", self.var_maDH.get())
          conn.commit()
          conn.close()
          messagebox.showinfo('Update', 'Xóa thành công!', parent=self.root)
          self.thongTinSP_table.delete(*self.thongTinSP_table.get_children())
          self.reset_sp()
          self.tongTien()
        except Exception as e:
          messagebox.showwarning('Warning', f'Xuất hiện một số vấn đề: {str(e)}', parent = self.root)
        
    
  
 
if __name__ == "__main__":
  root = Tk()
  ojb = themHD_win(root, "NV_00001")
  root.mainloop()