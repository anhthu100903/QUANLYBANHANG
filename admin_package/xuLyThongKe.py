import matplotlib.pyplot as plt #pip install matplotlib
from tkinter import*
import sys
sys.path.append('E:\hk2_namII\TuHoc\QuanLiBanHang')
from sqlConnect import database_QLBH
import pyodbc
from datetime import datetime
import matplotlib.pyplot as plt
from tkinter import messagebox

class xuLy:
  def __init__(self, root):
    self.root = root


#+++++++++++++++++++++++++++++++++++++++++++++++++ DOANH SỐ ++++++++++++++++++++++++++++++++++++++++++++





   #================== ngày ==================== 
   
  def doannhSo_Ngay(self):
    conn = pyodbc.connect(database_QLBH[0])
    dSo_ngay=[]
    day =self.clickNgay()
    for i in range (0, len(day)):#7 ngày
      my_cursor = conn.cursor()
      my_cursor.execute("select sum(TRIGIA) from HOADON where TRANGTHAI='ACTION' and  NGHD=?", day[i])
      rows = my_cursor.fetchall()
      if rows[0][0] == None or len(rows)==0:
        dSo_ngay.append(0)
      else:
        dSo_ngay.append(int(rows[0][0]))
    return dSo_ngay
  
  def giaVon_ngay(self):
    conn = pyodbc.connect(database_QLBH[0])
    dSo_ngay=[]
    day =self.clickNgay()
    for i in range (0,7):#7 ngày
      my_cursor = conn.cursor()
      my_cursor.execute("select sum(GIAGOC)\
                        from SANPHAM, (select MASP from CTHD where SOHD in (select SOHD from HOADON where TRANGTHAI='ACTION' and NGHD =?))T\
                        where SANPHAM.MASP = T.MASP ", day[i])
      rows = my_cursor.fetchall()
      if rows[0][0] == None or len(rows)==0:
        dSo_ngay.append(0)
      else:
        dSo_ngay.append(int(rows[0][0]))
    return dSo_ngay

  def show_dSo_ngay(self):
    ngay_dSo=[]
    ngay_loi=[]
    for i in self.clickNgay():
      ngay_dSo.append(int(i.split('-')[2])-0.15)
      ngay_loi.append(int(i.split('-')[2])+0.15)

    loi_nhuan=[]
    von=self.giaVon_ngay()
    doanh_thu=self.doannhSo_Ngay()
    for i in range(0,7):
      loi_nhuan.append(doanh_thu[i]-von[i])
    plt.bar(ngay_dSo, doanh_thu, label="Doanh Thu",color='y', width=0.3)
    plt.bar(ngay_loi, loi_nhuan, label="Lợi Nhuận", color='c', width=0.3)
    plt.legend()
    plt.xlabel('VND')
    plt.ylabel('Ngày')
    plt.title('Biểu Đồ Hiển Thị Vốn Và Doanh Thu Trong 7 Ngày')
    plt.show()


#================ tuần ================

  def doannhSo_Tuan_Thang(self, ngayDK):
    conn = pyodbc.connect(database_QLBH[0])
    dSo=[]
    day =ngayDK
    for i in range (0,len(ngayDK)):
      my_cursor = conn.cursor()
      my_cursor.execute("select sum(TRIGIA) from HOADON where TRANGTHAI='ACTION' and NGHD>=? and NGHD<=?", day[i][0], day[i][1])
      rows = my_cursor.fetchall()
      if rows[0][0] == None or len(rows)==0:
        dSo.append(0)
      else:
        dSo.append(int(rows[0][0]))
    return dSo
  
  def giaVon_Tuan_thang(self, ngayDK):
    conn = pyodbc.connect(database_QLBH[0])
    dSo_ngay=[]
    day =ngayDK
    for i in range (0,len(ngayDK)):#7 ngày
      my_cursor = conn.cursor()
      my_cursor.execute("select sum(GIAGOC)\
                        from SANPHAM, (select MASP from CTHD where SOHD in (select SOHD from HOADON where TRANGTHAI='ACTION' and NGHD >=? and NGHD <=? ))T\
                        where SANPHAM.MASP = T.MASP ", day[i][0], day[i][1])
      rows = my_cursor.fetchall()
      if rows[0][0] == None or len(rows)==0:
        dSo_ngay.append(0)
      else:
        dSo_ngay.append(int(rows[0][0]))
    return dSo_ngay
  
  def show_dSo_Tuan_Thang(self, ngayDK):
    ds_dSo=[]
    ds_loiNhuan=[]
    ngayBD = ngayDK[0][0].split('-')[2]
    ngayKT=ngayDK[0][1].split('-')[2]
    if int(ngayKT) - int(ngayBD) > 7:
      for i in range(1, len(ngayDK)+1):
        ds_dSo.append(i-0.15)
        ds_loiNhuan.append(i+0.15)
      thang_bd=int(ngayDK[0][0].split('-')[1])
      thang_kt =int(ngayDK[len(ngayDK)-1][0].split('-')[1])
      nam=ngayDK[len(ngayDK)-1][0].split('-')[0]
      plt.xlabel('Từ tháng ' + str(thang_bd) +' đến tháng ' + str(thang_kt) + ' năm ' + str(nam))
      plt.ylabel('VND')
      plt.title('Biểu Đồ Hiển Thị Vốn Và Doanh Thu Các Tháng Trong Năm ' + str(nam))
    else:
      for i in range(1, len(ngayDK)+1):
        #(ngày bắt đầu tuần + (tháng-1)*số ngày tb tháng trong năm)//7
        ds_dSo.append(i-0.15)
        ds_loiNhuan.append(i+0.15)
      
      tuan_bd=int((int(ngayDK[0][0].split('-')[2])+(int(ngayDK[0][0].split('-')[1])-1)*30.5)//7)
      tuan_kt=int((int(ngayDK[len(ngayDK)-1][0].split('-')[2])+(int(ngayDK[len(ngayDK)-1][0].split('-')[1])-1)*30.5)//7)
      
      plt.xlabel('Từ tuần ' + str(tuan_bd) + ' năm ' + ngayDK[0][0].split('-')[0] +' đến tuần ' + str(tuan_kt) + ' năm ' + ngayDK[len(ngayDK)-1][0].split('-')[0])
      plt.ylabel('VND')
      plt.title('Biểu Đồ Hiển Thị Vốn Và Doanh Thu Trong 4 Tuần')
    loi_nhuan=[]
    von=self.giaVon_Tuan_thang(ngayDK)
    doanh_thu=self.doannhSo_Tuan_Thang(ngayDK)
    for i in range(0,len(ngayDK)):
      loi_nhuan.append(doanh_thu[i]-von[i])
    plt.bar(ds_dSo, doanh_thu, label="Doanh Thu",color='y', width=0.3)
    plt.bar(ds_loiNhuan, loi_nhuan, label="Lợi Nhuận", color='c', width=0.3)
    plt.legend()
    plt.show()
    
  def show_tuan(self):
    self.show_dSo_Tuan_Thang(self.clickTuan())

#================== tháng =========================

  def show_thang(self):
    self.show_dSo_Tuan_Thang(self.clickThang())






#++++++++++++++++++++++++++++++++++++++++++++++++++ Số lượng bán của mỗi sản phẩm  ++++++++++++++++++++++++++++++++++++++++++++








#ngày
  def sLuongBanNgay(self):
    conn = pyodbc.connect(database_QLBH[0])
    
    my_cursor = conn.cursor()
    my_cursor.execute("select MASP, TENSP from SANPHAM where TRANGTHAI='ACTION'") #lấy mã sản phẩm và tên sản phẩm trong sql
    rows= my_cursor.fetchall()
    dssp=[i[0] for i in rows] #masp nằm ở cột đầu tiên
    dsTenSp=[i[1] for i in rows] #tensp nằm ở cột thứ 2
    
    curent_date = datetime.now() #ngày hiện tại
    day=str(curent_date.year) + '-' + str(curent_date.month) + '-' + str(curent_date.day) #dịnh dạng yy-mm-dd
    
    L = []
    for i in dssp:
      my_cursor = conn.cursor()
      #tính số lượng mỗi sản phẩm đã bán
      my_cursor.execute("select SUM(SOLUONG)\
                        FROM (select MASP, SOLUONG\
                              from CTHD, (select SOHD from HOADON where NGHD =? and TRANGTHAI='ACTION')A\
                              where CTHD.SOHD = A.SOHD)T\
                        WHERE MASP=?", day, i)
      rows = my_cursor.fetchall()
      if len(rows)==0:
        L.append(0)
      else:
        L.append(rows[0][0])
    dict_SP=dict()
    for i in range(0, len(dsTenSp)):
      if L[i]==None:
        dict_SP[dsTenSp[i]]=0
      else:
        dict_SP[dsTenSp[i]]=L[i]
    return dict_SP #trả về kiểu từ điển gồm tên sản phẩm và số lượng sản phẩm đã bán
    
  
  def show_SLNgay(self):
    dict_SP = self.sLuongBanNgay()
    tong=0
    for i in dict_SP.values():
      tong+=int(i)
    if tong==0:
      messagebox.showwarning('Warning','Hiện chưa có sản phẩm được bán trong ngày!', parent=self.root)
    else:
      plt.title('Tổng số lượng bán: '+ str(tong), loc='left', pad=20)
      plt.xlabel('Biểu đồ thể hiện cơ cấu số lượng sản phẩm bán trong 1 ngày!')
      plt.pie(dict_SP.values(), labels=dict_SP.keys(), autopct='%1.1f%%', shadow=True, startangle=90)
      plt.axis('equal')# trục x = trục y
      plt.legend()
      plt.show()
#tuần-tháng
  def sLuongBan_Tuan_Thang(self, ngayDK):
    conn = pyodbc.connect(database_QLBH[0])
    
    my_cursor = conn.cursor()
    my_cursor.execute("select MASP, TENSP from SANPHAM where TRANGTHAI='ACTION'")
    rows= my_cursor.fetchall()
    dssp=[i[0] for i in rows]
    dsTenSp=[i[1] for i in rows]
    # print(ngayDK())
    day=ngayDK
    ngayBD= day[len(ngayDK)-1][0]
    ngayKT= day[len(ngayDK)-1][1]
    L = []
    for j in dssp:
      my_cursor = conn.cursor()
      my_cursor.execute("select SUM(SOLUONG)\
                        FROM (select MASP, SOLUONG\
                              from CTHD, (select SOHD from HOADON where NGHD>=? and NGHD<=?)A\
                              where CTHD.SOHD = A.SOHD)T\
                        WHERE MASP=?",ngayBD, ngayKT, j)
      rows = my_cursor.fetchall()
      if len(rows)==0:
        L.append(0)
      else:
        L.append(rows[0][0])
      
    dict_SP=dict()
    for i in range(0, len(dsTenSp)):
      if L[i]==None:
        dict_SP[dsTenSp[i]]=0
      else:
        dict_SP[dsTenSp[i]]=L[i]
    return dict_SP
  
  def show_SLTuan(self):
    dict_SP = self.sLuongBan_Tuan_Thang(self.clickTuan())
    tong=sum(list(dict_SP.values()))
    if tong==0:
      messagebox.showwarning('Warning','Hiện chưa có sản phẩm được bán trong tuần!', parent = self.root)
    else:
      plt.title('Tổng số lượng bán: '+ str(tong), loc='left', pad=20)
      plt.xlabel('Biểu đồ thể hiện cơ cấu số lượng sản phẩm bán trong 7 ngày gần nhất!')
      plt.pie(dict_SP.values(), labels=dict_SP.keys(), autopct='%1.1f%%', shadow=True, startangle=90)
      plt.axis('equal')# trục x = trục y
      plt.legend()
      plt.show()
  
  def show_SLThang(self):
    dict_SP = self.sLuongBan_Tuan_Thang(self.clickThang())
    tong=0
    for i in dict_SP.values():
      tong+=int(i)
    if tong==0:
      messagebox.showwarning('Warning','Hiện chưa có sản phẩm được bán trong tuần!', parent = self.root)
    else:
      plt.title('Tổng số lượng bán: '+ str(tong), loc='left', pad=20)
      plt.xlabel('Biểu đồ thể hiện cơ cấu số lượng sản phẩm bán trong tháng gần nhất!')
      plt.pie(dict_SP.values(), labels=dict_SP.keys(), autopct='%1.1f%%', shadow=True, startangle=90)
      plt.axis('equal')# trục x = trục y
      plt.legend()
      plt.show()
  
  def showTongKho(self):
    conn = pyodbc.connect(database_QLBH[0])
    my_cursor = conn.cursor()
    my_cursor.execute("select sum(SOLUONG) from SANPHAM")
    rows = my_cursor.fetchall()
    return rows[0][0] #trả về số lượng tất cả sản phẩm trong kho






#++++++++++++++++++++++++ Sản phẩm bán số lượng hóa đơn mỗi nhân viên bán được






#số lượng hóa đơn mỗi nhân viên bán được
#ngày
  def SLNVBanNgay(self):
    conn = pyodbc.connect(database_QLBH[0])
    
    my_cursor = conn.cursor()
    my_cursor.execute("select USER_ID, TEN from TAIKHOAN")  #lấy tên và mã nhân viên từ sql
    rows= my_cursor.fetchall()
    dsnv=[i[0] for i in rows] #manv năm ở cột đầu tiên trong sql
    dsTenNV=[i[1] for i in rows] #ten nằm ở cột thứ 2 trong sql
    
    curent_date = datetime.now() #ngày hiện tại
    day=str(curent_date.year) + '-' + str(curent_date.month) + '-' + str(curent_date.day) #định dạng yy-mm-dd
    
    L = []
    for i in dsnv:
      my_cursor = conn.cursor()
      my_cursor.execute("select COUNT(SOHD) from HOADON where NGHD=? and MANV=? and TRANGTHAI='ACTION'", day, i) #đếm số hóa đơn mỗi ngày của mỗi nhân viên
      rows = my_cursor.fetchall()
      if len(rows)==0:
        L.append(0)
      else:
        L.append(rows[0][0])
      
    dict_SP=dict()
    for i in range(0, len(dsnv)):
      if L[i]==None:
        dict_SP[dsTenNV[i]]=0
      else:
        dict_SP[dsTenNV[i]]=L[i]
    return dict_SP #trả về kiểu từ điển gòm tên nv và só hóa đơn
    
  
  def show_SLNVNgay(self):
    
    dict_SP = self.SLNVBanNgay()
    tong=0
    for i in dict_SP.values():
      tong+=int(i)
    if tong==0:
      messagebox.showwarning('Warning','Hiện chưa có hóa đơn nào!', parent=self.root)
    else:
      plt.title('Nhân viên đã bán: '+ str(tong), loc='left', pad=20)
      plt.xlabel('Biểu đồ thể hiện cơ cấu số lượng bán của nhân viên trong 1 ngày!')
      plt.pie(dict_SP.values(), labels=dict_SP.keys(), autopct='%1.1f%%', shadow=True, startangle=90)
      plt.axis('equal')# trục x = trục y
      plt.legend()
      plt.show()

#tuần-tháng
  def SLNVBan_Tuan_Thang(self, ngayDK): #số lượng đơn hàng của 7 ngày gần nhất, số lượng đơn hàng từ ngày 1-31 của tháng hiện tại
    conn = pyodbc.connect(database_QLBH[0])
    my_cursor = conn.cursor()
    my_cursor.execute("select USER_ID, TEN from TAIKHOAN") #lấy tên và mã nhân viên từ sql
    rows= my_cursor.fetchall()
    dsnv=[i[0] for i in rows] #manv năm ở cột đầu tiên trong sql
    dsTenNV=[i[1] for i in rows] #ten nằm ở cột thứ 2 trong sql
    day=ngayDK #danh sách các ngày theo yêu cầu
    ngayBD= day[len(ngayDK)-1][0]  #lấy ngày bắt đầu ở phần tử cuối
    ngayKT= day[len(ngayDK)-1][1] #lấy ngày kết thức ở phân tử cuối
    L = []
    for j in dsnv:
      my_cursor = conn.cursor()
      #dếm số hóa đơn của mỗi nhân viên trong tuần hoặc  tháng
      my_cursor.execute("select COUNT(SOHD) from HOADON where NGHD>=? and NGHD<=? and MANV=? and TRANGTHAI='ACTION'",ngayBD, ngayKT, j)
      rows = my_cursor.fetchall()
      if len(rows)==0:
        L.append(0)
      else:
        L.append(rows[0][0])
      
    dict_SP=dict()
    for i in range(0, len(dsTenNV)):
      if L[i]==None:
        dict_SP[dsTenNV[i]]=0
      else:
        dict_SP[dsTenNV[i]]=L[i]
    return dict_SP #trả về kiểu từ điển gòm tên nv và só hóa đơn
  
  def show_SLNVTuan(self):
    dict_SP = self.SLNVBan_Tuan_Thang(self.clickTuan())
    tong=sum(list(dict_SP.values()))
    if tong==0:
      messagebox.showwarning('Warning','Hiện chưa có hóa đơn nào!', parent=self.root)
    else:
      # plt.title('Biểu đồ thể hiện cơ cấu số lượng sản phẩm bán trong 1 ngày!',pad=20)
      plt.title('Nhân viên đã bán: '+ str(tong), loc='left', pad=20)
      plt.xlabel('Biểu đồ thể hiện cơ cấu số lượng sản phẩm bán trong 7 ngày gần nhất!')
      plt.pie(dict_SP.values(), labels=dict_SP.keys(), autopct='%1.1f%%', shadow=True, startangle=90)
      plt.axis('equal')# trục x = trục y
      plt.legend()
      plt.show()
  
  def show_SLNVThang(self):
    dict_SP = self.SLNVBan_Tuan_Thang(self.clickThang())
    tong=sum(list(dict_SP.values()))
    if tong==0:
      messagebox.showwarning('Warning','Hiện chưa có hóa đơn nào!', parent=self.root)
    else:
      # plt.title('Biểu đồ thể hiện cơ cấu số lượng sản phẩm bán trong 1 ngày!',pad=20)
      plt.title('Nhân viên đã bán: '+ str(tong), loc='left', pad=20)
      plt.xlabel('Biểu đồ thể hiện cơ cấu số lượng sản phẩm bán trong tháng gần nhất!')
      plt.pie(dict_SP.values(), labels=dict_SP.keys(), autopct='%1.1f%%', shadow=True, startangle=90)
      plt.axis('equal')# trục x = trục y
      plt.legend()
      plt.show()
  
#doanh thu mỗi nhân viên bán được
  
  def TienBanDuocNV_Ngay(self):
    conn = pyodbc.connect(database_QLBH[0])
    
    my_cursor = conn.cursor()
    my_cursor.execute("select USER_ID, TEN from TAIKHOAN")# where TRANGTHAI='ACTION'
    rows= my_cursor.fetchall()
    dsnv=[i[0] for i in rows]
    dsTenNV=[i[1] for i in rows]
    
    curent_date = datetime.now()
    day=str(curent_date.year) + '-' + str(curent_date.month) + '-' + str(curent_date.day)
    
    L = []
    for i in dsnv:
      my_cursor = conn.cursor()
      my_cursor.execute("select SUM(TRIGIA) from HOADON where NGHD=? and MANV=? and TRANGTHAI='ACTION'", day, i)
      rows = my_cursor.fetchall()
      if len(rows)==0:
        L.append(0)
      else:
        L.append(rows[0][0])
      
    dict_SP=dict()
    for i in range(0, len(dsnv)):
      if L[i] == None:
        dict_SP[dsTenNV[i]]=0
      else:
        dict_SP[dsTenNV[i]]=L[i]
    return dict_SP
    
  
  def show_TienBanDuocNVNgay(self):
    dict_SP = self.TienBanDuocNV_Ngay()
    chieuRong=[0.2 for i in dict_SP.values()]
    plt.xlabel('Tên Nhân Viên')
    plt.ylabel('Doanh Thu')
    plt.title('Biểu đồ thể hiện doanh thu của mỗi nhân viên trong ngày!')
    plt.bar(range(len(dict_SP)), list(dict_SP.values()),color='r', width=chieuRong)
    plt.xticks(range(len(dict_SP)), dict_SP.keys())
    plt.show()

#tuần-tháng
  def TienBanDuocNV_Tuan_Thang(self, ngayDK):
    conn = pyodbc.connect(database_QLBH[0])
    
    my_cursor = conn.cursor()
    my_cursor.execute("select USER_ID, TEN from TAIKHOAN")
    rows= my_cursor.fetchall()
    dsnv=[i[0] for i in rows]
    dsTenNV=[i[1] for i in rows]
    
    day=ngayDK
    ngayBD= day[len(ngayDK)-1][0]
    ngayKT= day[len(ngayDK)-1][1]
    L = []
    for j in dsnv:
      my_cursor = conn.cursor()
      my_cursor.execute("select SUM(TRIGIA) from HOADON where NGHD>=? and NGHD<=? and MANV=? and TRANGTHAI='ACTION'",ngayBD, ngayKT, j)
      rows = my_cursor.fetchall()
      if len(rows)!=0:
        L.append(rows[0][0])
      else:
        L.append(0)
      
    dict_SP=dict()
    for i in range(0, len(dsTenNV)):
      if L[i] == None:
        dict_SP[dsTenNV[i]]=0
      else:
        dict_SP[dsTenNV[i]]=L[i]
    return dict_SP
  
  def show_TienBanDuocNVTuan(self):
    dict_SP = self.TienBanDuocNV_Tuan_Thang(self.clickTuan())
    tong=sum(list(dict_SP.values()))
    chieuRong=[0.2 for i in dict_SP.values()]
    plt.xlabel('Tên Nhân Viên')
    plt.ylabel('Doanh Thu')
    plt.title('Biểu đồ thể hiện cơ cấu số lượng sản phẩm\n bán trong 7 ngày gần nhất!')
    plt.bar(range(len(dict_SP)), list(dict_SP.values()),color='r', width=chieuRong)
    plt.xticks(range(len(dict_SP)), dict_SP.keys())
    plt.show()
  
  def show_TienBanDuocNVThang(self):
    dict_SP = self.TienBanDuocNV_Tuan_Thang(self.clickThang())
    tong=sum(dict_SP.values())
    
    
    ngayDK=self.clickThang()
    thang = ngayDK[len(ngayDK)-1][0].split('-')[1]
    nam=ngayDK[len(ngayDK)-1][0].split('-')[0]
    chieuRong=[0.2 for i in dict_SP.values()]
    
    plt.xlabel('Tên Nhân Viên')
    plt.ylabel('Doanh Thu')
    plt.title('Biểu Đồ Thể Hiện Số Lượng Hóa Đơn Đã Bán\n Của Mỗi Nhân Viên Trong Tháng ' + str(thang) + '-' + str(nam))
    plt.bar(range(len(dict_SP)), list(dict_SP.values()),color='r', width=chieuRong)
    plt.xticks(range(len(dict_SP)), dict_SP.keys())
    plt.show()
  




#++++++++++++++++++++++++ Sản phẩm bán số lượng hóa đơn mỗi nhân viên bán được




  def SLDon_Ngay(self):
    conn = pyodbc.connect(database_QLBH[0])
    
    my_cursor = conn.cursor()
    
    day=self.clickNgay()
    sl_hoaDon = []
    L = []
    for i in range(0, len(day)):
      my_cursor = conn.cursor()
      my_cursor.execute("select COUNT(SOHD) from HOADON where NGHD=? and TRANGTHAI='ACTION'", day[i])
      rows = my_cursor.fetchall()
      if rows[0][0] == None or len(rows)==0:
        sl_hoaDon.append(0)
      else:
        sl_hoaDon.append(int(rows[0][0]))
    return sl_hoaDon

  def show_slDon_Ngay(self):
    ngay=[]
    for i in self.clickNgay():
      ngay.append(int(i.split('-')[2]))

    slhd = self.SLDon_Ngay()
    chieuRong=[0.5 for i in slhd]
    plt.xlabel('Ngày: ')
    plt.ylabel('Số Lượng')
    plt.title('Biểu đồ thể hiện số lượng hóa đơn bán được trong ngày!')
    plt.bar(range(len(slhd)), list(slhd),color='r', width=chieuRong)
    plt.xticks(range(len(slhd)), ngay)
    plt.show()

  def SLDon_Tuan_Thang(self, ngayDK):
    conn = pyodbc.connect(database_QLBH[0])
    my_cursor = conn.cursor()
    
    day = ngayDK
    sl_hoaDon=[]
    L = []
    for i in range(0, len(ngayDK)):
      my_cursor = conn.cursor()
      
      ngayBD= day[i][0]
      ngayKT= day[i][1]
      
      my_cursor.execute("select COUNT(SOHD) from HOADON where NGHD>=? and NGHD<=? and TRANGTHAI='ACTION'",ngayBD, ngayKT)
      rows = my_cursor.fetchall()
      if rows[0][0] == None or len(rows)==0:
        sl_hoaDon.append(0)
      else:
        sl_hoaDon.append(int(rows[0][0]))
    return sl_hoaDon
  
  def show_slDon_Tuan(self):
    slhd = self.SLDon_Tuan_Thang(self.clickTuan())
    tong=sum(slhd)
    chieuRong=[0.5 for i in slhd]
    plt.xlabel('Tuần')
    plt.ylabel('Số Lượng')
    plt.title('Biểu đồ thể hiện số lượng hóa đơn bán được\n trong tuần 4 tuần gần!')
    plt.bar(range(len(slhd)), list(slhd),color='r', width=chieuRong)
    plt.xticks(range(len(slhd)), range(1,len(slhd)+1))
    plt.show()
    
  def show_slDon_Thang(self):
    slhd = self.SLDon_Tuan_Thang(self.clickThang())
    tong=sum(slhd)
    chieuRong=[0.5 for i in slhd]
    
    ngayDK=self.clickThang()
    thang_bd=int(ngayDK[0][0].split('-')[1])
    thang_kt =int(ngayDK[len(ngayDK)-1][0].split('-')[1])
    nam=ngayDK[len(ngayDK)-1][0].split('-')[0]
    
    plt.ylabel('Số Lượng')
    plt.xlabel('Từ tháng ' + str(thang_bd) +' đến tháng ' + str(thang_kt) + ' năm ' + str(nam))
    plt.title('Biểu Đồ Thể Hiện Số Lượng Hóa Đơn Đã Bán Mỗi Tháng Trong Năm ' + str(nam))
    
    plt.bar(range(len(slhd)), list(slhd),color='r', width=chieuRong)
    plt.xticks(range(len(slhd)), range(1,len(slhd)+1))
    plt.show()
  
  
  
  #=============sự kiện==============  
  def clickNgay(self):
    current_date = datetime.now()
    L=[]
    for i in range(6,-1,-1):
      L.append(self.ngay_dkien(current_date, -i)) 
    return L
  
  def clickTuan(self):
    current_date = datetime.now()
    L=list()
    temp=current_date
    for i in range(0, 4):
      L2=[]
      L2.append(self.ngay_dkien(temp, -6))
      L2.append(self.ngay_dkien(temp, 0))
      L.insert(0,L2)
      a=self.ngay_dkien(temp, -7).split('-')
      temp = datetime(int(a[0]), int(a[1]), int(a[2]))
    return L
  
  def clickThang(self):
    try:
      current_date = datetime.now()
      L=list()
      soNgayThang = self.songaytrongthang(current_date.month, current_date.year)
      temp=datetime(current_date.year, current_date.month, soNgayThang)
      for i in range(0, current_date.month):
        soNgayThang = self.songaytrongthang(temp.month, temp.year)
        L2=[]
        L2.append(self.ngay_dkien(temp, -soNgayThang+1)) #bỏ ngày hiện tại
        L2.append(self.ngay_dkien(temp, 0))
        L.insert(0, L2)
        a=self.ngay_dkien(temp,-soNgayThang).split('-')
        temp = datetime(int(a[0]), int(a[1]), int(a[2]))
      return L
    except Exception as e:
      messagebox.showwarning('Warning', f'Xuất hiện một số vấn đề: {str(e)}', parent = self.root)
  
  #============xử lý ngày============================
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
  