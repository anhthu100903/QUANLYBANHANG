
from tkinter import*
from tkinter import ttk
import pyodbc
import sys
sys.path.append('E:\hk2_namII\TuHoc\QuanLiBanHang')
from sqlConnect import database_QLBH

f = font=("times new roman", 12)
bgColor = '#f3d8d6'
fgColor = "#fefffa"

class chiTiet_win:
  def __init__(self, mahd):
    self.mahd=mahd
  def xemChiTiet(self):
    chiTiet = Tk()
    chiTiet.geometry('700x500+370+115')
    chiTiet.title('Chi Tiết Hóa Đơn')
    
    chiTietHD_frame = Frame(chiTiet, bg=bgColor)
    chiTietHD_frame.place(x=0, y=0, width=700, height=500)
      
    #===================== Thông tin đơn hàng ==================
    
    #=================== variables =================
    
    #===================== +_+ ===============
    ttdh_frame = Frame(chiTietHD_frame, bg=bgColor)
    ttdh_frame.place(x=0, y=0, width=700, height=210)
    
    #===================== đơn hàng frame ============
    donHang_frame = LabelFrame(ttdh_frame, text='Thông tin đơn hàng', bg='white', bd=4, relief='sunken', font=f)
    donHang_frame.place(x=10,y=10, width=360, height=190)
    
    maDon_lb = Label(donHang_frame, text='Mã Đơn Hàng', bg='white', font=f)
    maDon_lb.place(x=10, y=20, width=100, height=40)
    self.maDon1_lb = Label(donHang_frame, bg='white', font=f)
    self.maDon1_lb.place(x=150, y=20, height=40)
    
    maKH_lb = Label(donHang_frame, text='Mã Khách Hàng', bg='white', font=f)
    maKH_lb.place(x=10, y=65, width=110, height=40)
    self.maKH1_lb = Label(donHang_frame, bg='white', font=f)
    self.maKH1_lb.place(x=150,y=65, height=40)
    
    thoiGian_lb = Label(donHang_frame, text='Thời Gian:', bg='white', font=f)
    thoiGian_lb.place(x=10, y=110, width=70, height=40)
    self.thoiGian1_lb = Label(donHang_frame, bg='white', font=f)
    self.thoiGian1_lb.place(x=150,y=110, height=40)
    
    #=================== thanh toán frame ================
    
    thanhToan_frame = LabelFrame(ttdh_frame, text='Thanh Toán', bg=bgColor, font=f, bd=4, relief=RAISED)
    thanhToan_frame.place(x=380, y=10, width=310, height=190)
    
    tongCong_lb = Label(thanhToan_frame, text='Tổng cộng:', bg=bgColor, font=f)
    tongCong_lb.place(x=10, y=10, width=70, height=35)
    self.tongCong1_lb =Label(thanhToan_frame, bg=bgColor, font=f)
    self.tongCong1_lb.place(x=120, y=10, height=35)
    
    giam_lb = Label(thanhToan_frame, text='Giảm:', bg=bgColor, font=f)
    giam_lb.place(x=10, y=60, width=40, height=35)    
    self.giam1_lb =Label(thanhToan_frame, bg=bgColor, font=f)
    self.giam1_lb.place(x=120, y=60, height=35)
   
    con_lb = Label(thanhToan_frame, text='Còn:', bg=bgColor, font=f)
    con_lb.place(x=10, y=110, width=30, height=35)
    self.con1_lb =Label(thanhToan_frame, bg=bgColor, font=f)
    self.con1_lb.place(x=120, y=110, height=35)
    
    
    #================== Danh Sách Sản Phẩm ================
    dsSanPham_tableFrame = LabelFrame(chiTietHD_frame, text='Danh Sách Sản Phẩm', bd=4, relief=RIDGE, font=f, bg='white')
    dsSanPham_tableFrame.place(x=10, y=220, width=680, height=270)
    
    #================== Bảng Sản Phẩm ======================
    self.stt = 0
    
    
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
    self.thongTinSP_table.pack(fill=BOTH, expand=1)
    self.load_CT()
  
  def load_CT(self):
    conn = pyodbc.connect(database_QLBH[0])
    my_cursor = conn.cursor()
    my_cursor.execute("select* from CTHD where TRANGTHAI='ACTION' and SOHD=?", self.mahd)
    rows = my_cursor.fetchall()
    self.thongTinSP_table.delete(*self.thongTinSP_table.get_children())
    if len(rows)!=0:
      for i in rows:
        list = []
        for j in range (0, 6):
          if j == 1:
            maDon=i[j]
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
          else:
            list.append(i[j])
        self.thongTinSP_table.insert("", END, values=list)
        
        
        self.tongCong1_lb.config(text=str(gia))
        self.giam1_lb.config(text=str(i[4]))
        self.con1_lb.config(text=i[5])
      conn.commit()
      
      self.maDon1_lb.config(text=self.mahd)
      
      my_cursor = conn.cursor()
      my_cursor.execute("select MAKH, NGHD from HOADON where TRANGTHAI='ACTION' and SOHD=?", self.mahd)
      rows = my_cursor.fetchall()
      self.maKH1_lb.config(text=rows[0][0])
      self.thoiGian1_lb.config(text=rows[0][1])
      
    conn.close()

if __name__ == "__main__":
  root = Tk()
  ojb = chiTiet_win("HD00001")
  ojb.xemChiTiet()
  root.mainloop()    