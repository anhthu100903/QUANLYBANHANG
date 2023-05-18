from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import sys
import openpyxl

from user_package.themHD import themHD_win
sys.path.append('E:\hk2_namII\TuHoc\QuanLiBanHang')
from sqlConnect import*
from datetime import datetime
from tkcalendar import Calendar

from admin_package.chiTietHD import chiTiet_win
from admin_package.lich import lich_win
from admin_package.xuLyThongKe import xuLy

f = font=("times new roman", 12)
bgColor = '#f3d8d6'
fgColor = "#fefffa"

class qlDonHang_win:
  def __init__(self, root, userid):
    self.root = root
    self.userID=userid
    
    dh_frame = Frame(root, bg=bgColor)
    dh_frame.place(x=0, y=0, width=1000, height=620)
    #===================== title ===================
    title_lb = Label(dh_frame, text="Quản Lý Đơn Hàng", font=("times newroman", 24, "bold"), fg='red', bg=bgColor)
    title_lb.place(x=0, y=0, width=350, height=50)
    
    
    search_lb = Label(dh_frame, text="Tìm Kiếm", bg='#89cff0', font=f)
    search_lb.place(x=575, y=10, width=70,height=40)
    
    
    self.var_searchCombobox = StringVar()
    search_combo = ttk.Combobox(dh_frame,textvariable=self.var_searchCombobox, state='readonly', font=f)
    search_combo["value"]=('SOHD','MAKH')
    search_combo.current(0)
    search_combo.place(x=650, y=10, width=75, height=40)
 
 
    self.var_search = StringVar()
    search_txt = ttk.Entry(dh_frame, textvariable=self.var_search, font=f)
    search_txt.place(x=735, y=10, width=250, height=40)
    search_txt.bind("<KeyPress>", self.search)
    
    # ==================== frame content =======================
    ttdh_frame = LabelFrame(dh_frame, bg=bgColor, text="Danh sách đơn hàng", font=("times new roman", 18, "bold"), bd=4, relief=RIDGE)
    ttdh_frame.place(x=10,y=50, width=980, height=560)
    
    # ================== search ============================
    search_lb = Label(ttdh_frame, text="Lọc Theo", font=f)
    search_lb.place(x=20, y=20, width=75,height=40)
    
    
    self.var_search = StringVar()
    self.var_ngay = StringVar()
    self.var_thang = StringVar()
    self.var_nam = StringVar()
    
    ngay_lb = Label(ttdh_frame, text='Ngày', font=f, bg='white')
    ngay_lb.place(x=100, y=20, width=40, height=40)
    ngay =[]
    for i in range(1,32):
      ngay.append(i)
    ngay_combo = ttk.Combobox(ttdh_frame, textvariable=self.var_ngay, font=f, justify='center')
    ngay_combo["values"]=ngay
    ngay_combo.place(x=141, y=20, width=40, height=40)
    
    
    thang_lb = Label(ttdh_frame, text='Tháng', font=f, bg='#FFFFFF')
    thang_lb.place(x=189, y=20, width=50, height=40)
    thang =[]
    for i in range(1,13):
      thang.append(i)
    thang_combo = ttk.Combobox(ttdh_frame, textvariable=self.var_thang, font=f, justify='center')
    thang_combo["values"]=thang
    thang_combo.place(x=240, y=20, width=40, height=40)
    
    
    nam_lb = Label(ttdh_frame, text='Năm', font=f, bg='#FFFFFF')
    nam_lb.place(x=289, y=20, width=50, height=40)
    nam =[]
    for i in range(2010,2024):
      nam.append(i)
    nam_combo = ttk.Combobox(ttdh_frame, textvariable=self.var_nam, font=f, justify='center')
    nam_combo["values"]=nam
    nam_combo.place(x=340, y=20, width=60, height=40)
    
    lich_img =Image.open(r'./img/calendar.png')
    lich_img=lich_img.resize((40,30), Image.ANTIALIAS)
    self.anh_lich = ImageTk.PhotoImage(lich_img)
    lich_btn = Button(ttdh_frame, command=self.lich, image=self.anh_lich, bg=bgColor)
    lich_btn.place(x=410, y=20, width=75, height=40)
    
    show_btn = Button(ttdh_frame, text="Lọc", command=self.load_data, bg="#89cff0", font=f)
    show_btn.place(x=500, y=20, width=75, height=40)
    
    reset_btn =Button(ttdh_frame, text="Làm mới", command=self.reset_data, bg="#89cff0", font=f)
    reset_btn.place(x=590, y=20, width=75, height=40)
    
    
    themHoaDon_btn = Button(ttdh_frame, text="Thêm Mới", command=self.themHD, bg="#89cff0", font=f)
    themHoaDon_btn.place(x=820, y=20, width=100, height=40)
    
    lb_maDon = Label(ttdh_frame, text="Mã Đơn:", bg=bgColor, font=f)
    lb_maDon.place(x=20, y=125, width=75, height=40)
    
    self.var_maDon = StringVar()
    txt_maDon = ttk.Entry(ttdh_frame, textvariable=self.var_maDon, font=f)
    txt_maDon.place(x=100, y=125, height=35, width=200)
    
    
    btn_xem = Button(ttdh_frame, text='xuất Excel', command=self.excel, font=f, bg="#89cff0")
    btn_xem.place(x=460, y=125, height=35, width=100)
    
    btn_xem = Button(ttdh_frame, text='Xem Chi Tiết', command=self.xemCT, font=f, bg="#89cff0")
    btn_xem.place(x=310, y=125, height=35, width=100)
    
  #=================== show data table ===============
    dsHoaDon_tableFrame = Frame(ttdh_frame, bg='white', bd=2, relief=RIDGE)
    dsHoaDon_tableFrame.place(x=25, y=175, width=920, height=340)
    
    scroll_x = ttk.Scrollbar(dsHoaDon_tableFrame,orient=HORIZONTAL)
    scroll_y = ttk.Scrollbar(dsHoaDon_tableFrame,orient=VERTICAL)
    
    self.thongTinHD_table = ttk.Treeview(dsHoaDon_tableFrame, column=("maHD", "maKH", "hoTen", 'ngayTao', "tongTien", "maNV"),
                                         xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
    
    scroll_x.pack(side=BOTTOM, fill=X)
    scroll_y.pack(side=RIGHT, fill=Y)
    
    scroll_x.config(command=self.thongTinHD_table.xview)
    scroll_y.config(command=self.thongTinHD_table.yview)
    
    self.thongTinHD_table.heading('maHD', text='Mã Hóa Đơn')
    self.thongTinHD_table.heading('maKH', text='Mã Khách Hàng')
    self.thongTinHD_table.heading('hoTen', text='Họ Tên')
    self.thongTinHD_table.heading('ngayTao', text='Ngày Tạo')
    self.thongTinHD_table.heading('tongTien', text='Tổng Tiền')
    self.thongTinHD_table.heading('maNV', text='Mã Nhân Viên')
    
    self.thongTinHD_table['show'] = 'headings'
    
    self.thongTinHD_table.column('maHD', width=100)
    self.thongTinHD_table.column('maKH', width=100)
    self.thongTinHD_table.column('hoTen', width=75)
    self.thongTinHD_table.column('ngayTao', width=100)
    self.thongTinHD_table.column('tongTien', width=100)
    self.thongTinHD_table.column('maNV', width=100)
    
    self.thongTinHD_table.bind('<ButtonRelease-1>', self.get_cursor)
    self.thongTinHD_table.pack(fill=BOTH, expand=1)
    
    self.load_data()
  
   
  def excel(self):
    try:
      conn = pyodbc.connect(database_QLBH[0])
      my_curcor = conn.cursor()
      my_curcor.execute("select* from HOADON where TRANGTHAI='ACTION'")
      rows = my_curcor.fetchall()
      if len(rows)!=0:
        data=[["maHD", "maKH", "hoTen", "ngayTao", "tongTien", "maNV"]]
        for i in rows:
          list=[]
          for j in range(0, 6): #có 6 thuộc tính hóa đơn (1 thuộc tính khách hàng, 1 thuộc tính account)
            if j == 2:
              kh_cursor = conn.cursor()
              kh_cursor.execute("select HOTEN from KHACHHANG where MAKH=?", list[1])
              ten_kh = kh_cursor.fetchall()
              list.append(ten_kh[0][0])
            elif j == 4:
              list.append(self.userID)
            list.append(i[j])
          data.append(list)
        conn.commit()
      conn.close()
    except Exception as e:
      messagebox.showwarning('Warning', f'Xuất hiện một số vấn đề: {str(e)}', parent = self.root)
      
    wb = openpyxl.Workbook()

    # Lấy sheet active
    ws = wb.active

    # Đặt tên cho sheet
    ws.title = "My Sheet"
    # Dữ liệu cần ghi vào
    # data = [
    #     ["maHD", "maKH", "hoTen", "ngayTao", "tongTien", "maNV"],
    #     ["Alice", 25, "USA"],
    #     ["Bob", 30, "Canada"],
    #     ["Charlie", 35, "Australia"]
    # ]

    #Ghi dữ liệu vào sheet
    for row in data:
        ws.append(row)

    # Tạo file excel
    wb.save("example.xlsx")
    messagebox.showinfo("Success", "Thành công!", parent=self.root)
  
  
  def themHD(self):
    self.new_windown = Toplevel(self.root)
    self.app = themHD_win(self.new_windown, self.userID)
  #==================== xem chi tiết ====================
  
  def xemCT(self):
    t =chiTiet_win(self.var_maDon.get())
    t.xemChiTiet()
    
  def lich(self):
    calen =  Tk()
    self.calen = calen
    self.calen.geometry("300x280+500+200")
    self.calen.title("Calendar picker")
    current_date=datetime.now()
    calendar_choose = Calendar(self.calen,selectmode = "day",year=current_date.year,month=current_date.month,date=current_date.day)
    #display on main window
    calendar_choose.pack(pady=30)
    # getting date from the calendar 

    def fetch_date():
      date.config(text = "Ngày: " + calendar_choose.get_date())
      date_choose = str(calendar_choose.get_date()).split('/')
      self.var_thang.set(date_choose[0])
      self.var_ngay.set(date_choose[1])
      self.var_nam.set('20'+date_choose[2])
    #add button to load the date clicked on calendar
    btn_date = Button(self.calen,text="Xác nhận: ",command=fetch_date, bg="gray")
    btn_date.place(x=25, y=230, width=75, height=40)
    date = Label(self.calen, text="")
    date.place(x=130, y=230, width=100, height=40)

  def reset_data(self):
    self.var_ngay.set('')
    self.var_thang.set('')
    self.var_nam.set('')
    self.var_maDon.set('')
    self.load_data()
    
  def load_data(self):
    if self.var_nam.get() !='' and self.var_thang.get() != '' and self.var_ngay !='':
      current_date = datetime(int(self.var_nam.get()), int(self.var_thang.get()), int(self.var_ngay.get()))
      ngayDkien = self.ngay_dkien(current_date, 10)
      conn = pyodbc.connect(database_QLBH[0])
      my_cursor = conn.cursor()
      my_cursor.execute("select* from HOADON where TRANGTHAI='ACTION' and NGHD >=? and NGHD <=?", current_date, ngayDkien)
      rows = my_cursor.fetchall()
    else:
      conn = pyodbc.connect(database_QLBH[0])
      my_cursor = conn.cursor()
      my_cursor.execute("SELECT TOP 10 * FROM HOADON WHERE TRANGTHAI='ACTION' ORDER BY NGHD DESC")
      rows = my_cursor.fetchall()
    
    self.thongTinHD_table.delete(*self.thongTinHD_table.get_children())
    if len(rows)!=0:
      for i in rows:
        list = []
        for j in range(0,6): #8 thuộc tính của  hóa đơn
          if j ==2:
            my_cursor = conn.cursor()
            my_cursor.execute('select HOTEN from KHACHHANG where MAKH=?', list[1])
            ten = my_cursor.fetchall()[0][0]
            list.append(ten)
          list.append(i[j])
        self.thongTinHD_table.insert("", END, values=list)
      conn.commit()
    conn.close()
    
  def get_cursor(self, event=''):
    cursor_row = self.thongTinHD_table.focus()
    content = self.thongTinHD_table.item(cursor_row)
    row=content['values']
    if row !=0:
      self.var_maDon.set(row[0])
    
  def nhuan(self, y):
    return ((y % 4 == 0 and y % 100 != 0) or y % 400 == 0)
  
  def songaytrongthang(self, m, y):
    if m in [1,3,5,7,8,10,12]:
      return 31
    elif m in [4,6,9,11]:
      return 30
    y=int(y)
    if self.nhuan(y):
      return 29
    return 28
   
  def ngay_dkien(self, ngay, dieuKien):
    dtime = [ngay.year, ngay.month,ngay.day]
    ngayCuaThang =self.songaytrongthang(dtime[1], dtime[0])
    if int(dtime[2]) + dieuKien <= ngayCuaThang and  int(dtime[2]) + dieuKien>0:
      d = int(dtime[2])+dieuKien
      m=dtime[1]
      y=dtime[0]
    else:
      if dieuKien > 0:
        if int(dtime[1])+1 <= 12:
          m=int(dtime[1])+1
          y=dtime[0]
        else:
          m=1
          y=int(dtime[0])+1
        ngayCuaThang =self.songaytrongthang(m, y)
        day = -ngayCuaThang + int(dtime[2]) + dieuKien 
        if ngayCuaThang >= day and day>0:
          d = day
        else:
          d =self.songaytrongthang(m-1,y)
          month=dtime[1] + dieuKien//self.songaytrongthang(m-1,y)
          if month > 12:
            m = month -12
          elif month < 1:
            m = 12 + month
          y=dtime[0]-1
      else:
        if int(dtime[1])-1 >= 1:
          m=int(dtime[1])-1
          y=dtime[0]
        else:
          m=12
          y=int(dtime[0])-1
        ngayCuaThang =self.songaytrongthang(m, y)
        #ngày mới tìm
        day = self.songaytrongthang(m,y) + int(dtime[2]) + dieuKien #(số ngày tháng ban đầu) + (điều kiện) + (ngày ban đầu)
        
        if ngayCuaThang >= day and day>0: #(nếu (số ngày tháng trước)>=(ngày mới) và (ngày ban đầu) - (số ngày tháng trước)+(điều kiện)>0)
          d = day
        else:
          d =self.songaytrongthang(m-1,y)
          month=dtime[1] + dieuKien//self.songaytrongthang(m-1,y)
          if month > 12:
            m = month - 12
          elif month < 1:
            m = 12 + month
          y=dtime[0]
          d = ngayCuaThang + dieuKien + dtime[2]
    return str(y) +'-'+ str(m) +'-'+ str(d)
  
  def search(self, event):
    if self.var_searchCombobox.get()=="SOHD":
      select_column=0
    elif self.var_searchCombobox.get()=="MAKH":
      select_column=1
    
    select_from= "HOADON"
    if event.keysym == 'BackSpace':
        query=self.var_search.get()[:-1]
    else:
      query=self.var_search.get()+event.char
    ds = get_dataSQL(select_from)
    options=[i[select_column] for i in ds]
    ds_index=search_index(query, options)
    self.thongTinHD_table.delete(*self.thongTinHD_table.get_children())
    if len(ds_index)!=0:
      for i in ds_index:
        list=[]
        for j in range(0, 6): #có 6 thuộc tính hóa đơn (1 thuộc tính khách hàng, 1 thuộc tính account)
          if j == 2:
            conn = pyodbc.connect(database_QLBH[0])
            kh_cursor = conn.cursor()
            kh_cursor.execute("select HOTEN from KHACHHANG where MAKH=?", list[1])
            ten_kh = kh_cursor.fetchall()
            list.append(ten_kh[0][0])
          elif j == 4:
            list.append(self.userID)
          list.append(ds[i][j])
        self.thongTinHD_table.insert("", END, values=list)
    elif len(query)<1:
      self.load_data()
  
if __name__ == "__main__":
  root = Tk()
  ojb = qlDonHang_win(root)
  root.mainloop()   