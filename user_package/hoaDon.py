from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import sys
sys.path.append('E:\hk2_namII\TuHoc\QuanLiBanHang')
from sqlConnect import*
import pyodbc
from user_package.themHD import themHD_win
import openpyxl

f = font=("times new roman", 12)
bgColor = '#f3d8d6'
fgColor = "#fefffa"

class hoaDon_win:
  
  def __init__(self, root, userID):
    self.root = root
    
    self.userID = userID
    
    dh_frame = Frame(root, bg=bgColor)
    dh_frame.place(x=0, y=0, width=1000, height=620)
    
    #===================== title ===================
    title_lb = Label(dh_frame, text="Đơn Hàng", font=("times newroman", 24, "bold"), fg='red', bg=bgColor)
    title_lb.place(x=0, y=0, width=200, height=50)
    
    # ==================== frame content =======================
    ttdh_frame = LabelFrame(dh_frame, bg=bgColor, text="Danh sách hóa đơn", font=("times new roman", 18, "bold"), bd=4, relief=RIDGE)
    ttdh_frame.place(x=10,y=50, width=980, height=560)
    
     # ================== search ============================
    search_lb = Label(ttdh_frame, text="Tìm Kiếm", bg='#89cff0', font=f)
    search_lb.place(x=20, y=20, width=70,height=40)
    
    
    self.var_searchCombobox = StringVar()
    search_combo = ttk.Combobox(ttdh_frame,textvariable=self.var_searchCombobox, state='readonly', font=f)
    search_combo["value"]=('SOHD','MAKH')
    search_combo.current(0)
    search_combo.place(x=95, y=20, width=75, height=40)
 
 
    self.var_search = StringVar()
    search_txt = ttk.Entry(ttdh_frame, textvariable=self.var_search, font=f)
    search_txt.place(x=175, y=20, width=250, height=40)
    search_txt.bind("<KeyPress>", self.search)
   
  #  ===================== btn content ====================
    xuat_btn = Button(ttdh_frame, text="Xuất Excel", command=self.excel, bg="#89cff0", font=f)
    xuat_btn.place(x=710, y=20, width=100, height=40)
    
    themHoaDon_btn = Button(ttdh_frame, text="Thêm Mới", command=self.themHD, bg="#89cff0", font=f)
    themHoaDon_btn.place(x=820, y=20, width=100, height=40)
   
    # =================== show data table ===============
    dsHoaDon_tableFrame = Frame(ttdh_frame, bg='white', bd=2, relief=RIDGE)
    dsHoaDon_tableFrame.place(x=25, y=100, width=920, height=400)
    
    scroll_x = ttk.Scrollbar(dsHoaDon_tableFrame,orient=HORIZONTAL)
    scroll_y = ttk.Scrollbar(dsHoaDon_tableFrame,orient=VERTICAL)
    
    self.thongTinHD_table = ttk.Treeview(dsHoaDon_tableFrame, column=("maHD", "maKH", "hoTen", "ngayTao", "tongTien", "maNV"),
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
    
    self.thongTinHD_table.column('maHD', width=100, anchor=CENTER)
    self.thongTinHD_table.column('maKH', width=100, anchor=CENTER)
    self.thongTinHD_table.column('hoTen', width=75, anchor=CENTER)
    self.thongTinHD_table.column('ngayTao', width=100, anchor=CENTER)
    self.thongTinHD_table.column('tongTien', width=100, anchor=CENTER)
    self.thongTinHD_table.column('maNV', width=100, anchor=CENTER)
    
    
    self.thongTinHD_table.pack(fill=BOTH, expand=1)
    self.load_dataHD()
    self.excel()
  
  def themHD(self):
    self.new_windown = Toplevel(self.root)
    self.app = themHD_win(self.new_windown, self.userID)
   
   #============================= Liên Kết Database Hóa Đơn==================
  
  def excel(self):
    try:
      conn = pyodbc.connect(database_QLBH[0])
      my_curcor = conn.cursor()
      my_curcor.execute("select* from HOADON where TRANGTHAI='ACTION'")
      rows = my_curcor.fetchall()
      if len(rows)!=0:
        data=[["maHD", "maKH", "hoTen", "ngayTao", "tongTien", "maNV"]]
        self.thongTinHD_table.delete(*self.thongTinHD_table.get_children())
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
  
  def load_dataHD(self):
    try:
      conn = pyodbc.connect(database_QLBH[0])
      my_curcor = conn.cursor()
      my_curcor.execute("select* from HOADON where TRANGTHAI='ACTION'")
      rows = my_curcor.fetchall()
      if len(rows)!=0:
        self.thongTinHD_table.delete(*self.thongTinHD_table.get_children())
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
          self.thongTinHD_table.insert("", END, values=list)
        conn.commit()
      conn.close()
    except Exception as e:
      messagebox.showwarning('Warning', f'Xuất hiện một số vấn đề: {str(e)}', parent = self.root)
      
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
      self.load_dataHD()

          
    
if __name__ == "__main__":
  root = Tk()
  ojb = hoaDon_win(root, 'AD_0001')
  root.mainloop()