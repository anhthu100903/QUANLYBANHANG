import matplotlib.pyplot as plt #pip install matplotlib
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import pyodbc
import sys
sys.path.append('E:\hk2_namII\TuHoc\QuanLiBanHang')
from sqlConnect import database_QLBH

from datetime import datetime
from admin_package.xuLyThongKe import xuLy

f = font=("times new roman", 12)
bgColor = '#f3d8d6'
fgColor = "#fefffa"

class thongKe_NV_win:
  def __init__(self, root, userId):
    self.root=root
    self.userID=userId
    
    #biến sd
    self.dict_doanhthu=dict()
    self.dict_sodon=dict()
    
    #gọi hàm
    self.dthu_sdon_Nam("COUNT(SOHD)", self.dict_sodon)
    self.dthu_sdon_Nam("SUM(TRIGIA)", self.dict_doanhthu)
    
    thongKe_frame = Frame(root, bg=bgColor)
    thongKe_frame.place(x=0, y=0, width=1000, height=620)
    
    #===================== title ===================
    title_lb = Label(thongKe_frame, text="Thống Kê", font=("times newroman", 24, "bold"), fg='red', bg=bgColor)
    title_lb.place(x=15, y=0, height=50)
    
    #=====================Số Lượng Nhân Viên Bán Được frame =============
    slnvb_frame = LabelFrame(thongKe_frame, text=' Thống kê số đon hàng và doanh thu ', bd=4, relief='raised', font=f, bg='white', fg='red')
    slnvb_frame.place(x=30, y=60, width=940, height=250)
    
    
    
    lbsl_title =Label(slnvb_frame, text='', bg='white', font=f)
    lbsl_title.place(x=10, y=10, height=30)
    lbsl_homNay = Label(slnvb_frame, text='Hôm Nay: ', bg='white', font=f)
    lbsl_homNay.place(x=200, y=10, height=30)
    lbsl_thang = Label(slnvb_frame, text='Tháng: ', bg='white', font=f)
    lbsl_thang.place(x=400, y=10, height=30)
    lbsl_nam = Label(slnvb_frame, text='Năm: ', bg='white', font=f)
    lbsl_nam.place(x=600, y=10, height=30)
        #+++++++++++
    lbsl_titleDB =Label(slnvb_frame, text='Số Đơn Hàng Đã Bán: ', bg='white', font=f)
    lbsl_titleDB.place(x=10, y=50, height=30)
    lbsl_homNayDB = Label(slnvb_frame, text=str(self.dthu_sdon_Ngay("COUNT(SOHD)")), bg='white', font=f)
    lbsl_homNayDB.place(x=200, y=50, height=30)
    
    lb_thangNVDB = Label(slnvb_frame, text=str(self.dthu_sdon_Thang("COUNT(SOHD)")), bg='white', font=f)
    lb_thangNVDB.place(x=400, y=50, height=30)
    
    lb_namNVDB = Label(slnvb_frame, text=str(sum(self.dict_sodon.values())), bg='white', font=f)
    lb_namNVDB.place(x=600, y=50, height=30)
  
        #+++++++++++Doanh thu+++++++++


    lbsl_titleThu =Label(slnvb_frame, text='Doanh Thu Đã Bán: ', bg='white', font=f)
    lbsl_titleThu.place(x=10, y=90, height=30)
    lbsl_homNayThu = Label(slnvb_frame, text=str(self.dthu_sdon_Ngay("SUM(TRIGIA)")), bg='white', font=f)
    lbsl_homNayThu.place(x=200, y=90, height=30)
    
    lb_tuanNVThu = Label(slnvb_frame, text=str(self.dthu_sdon_Thang("SUM(TRIGIA)")), bg='white', font=f)
    lb_tuanNVThu.place(x=400, y=90, height=30)
    
    lb_thangNVThu = Label(slnvb_frame, text=sum(self.dict_doanhthu.values()), bg='white', font=f)
    lb_thangNVThu.place(x=600, y=90, height=30)
    
      #+++++++++++Radio+++++++++
    radio_frame = Frame(slnvb_frame, bg='white')
    radio_frame.place(x=400, y=140, height=30, width=500)
    self.choose = IntVar()
    lb_radio_SLNVB = Label(radio_frame, text="Chọn:", justify = LEFT, padx = 20, font=f, background='white')
    lb_radio_SLNVB.place(x=0, y=0, height=30)
    ttk.Radiobutton(radio_frame,  text="Doanh Thu", variable=self.choose, value=1,).place(x=100, y=0, height=30)
    ttk.Radiobutton(radio_frame,  text="Số Đơn Hàng", variable=self.choose,  value=2).place(x=200, y=0, height=30)
    

        #Chức năng
    chucnang_frame =Frame(slnvb_frame, bg='white')
    chucnang_frame.place(x=500 , y=175, width=400, height=35)
    lb_showSL = Label(chucnang_frame, text='Xem bảng thống kê theo từng tháng:', bg='white', font=f, fg='red')
    lb_showSL.place(x=30, y=0, width=250, height=30)
    btn_ngay=Button(chucnang_frame, text='Xem',command=self.show_dThu_soDon_Nam, bg='#89cff0',font=f)
    btn_ngay.place(x=300,y=0,width=75, height=30)
    
    
  #=============================== Bảng thống kê hóa đơn trong tháng
  
    dsHoaDon_tableFrame = Frame(thongKe_frame, bg='white', bd=2, relief=RIDGE)
    dsHoaDon_tableFrame.place(x=30, y=325, width=940, height=280)
    
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
    self.load_data()
    
  def nhuan(self, y):
    return ((y % 4 == 0 and y % 100 != 0) or y % 400 == 0)
  
  def songaytrongthang(self, m, y):
    soNgayThang = xuLy.songaytrongthang(self, m, y)
    return soNgayThang
  
  def clickThang(self):
    xuLy.clickThang(self)
 
  def load_data(self):
    try:
      current_date = datetime.now()
      soNgay=self.songaytrongthang(current_date.month, current_date.year)
      temp=datetime(current_date.year, current_date.month, soNgay)
      ngayBD=xuLy.ngay_dkien(self,temp, -soNgay+1)
      ngayKT=str(temp.year)+'-'+str(temp.month)+'-'+str(temp.day)
      
      conn = pyodbc.connect(database_QLBH[0])
      my_curcor = conn.cursor()
      my_curcor.execute("select* from HOADON where TRANGTHAI='ACTION' and NGHD>=? and NGHD<=? and MANV=?", ngayBD, ngayKT, self.userID)
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
 
  def dthu_sdon_Ngay(self, dk_select):
    try:
      curent_date = datetime.now()
      day=str(curent_date.year) + '-' + str(curent_date.month) + '-' + str(curent_date.day)
      
      conn = pyodbc.connect(database_QLBH[0])
      my_cursor = conn.cursor()
      my_cursor.execute("select "+ dk_select+ " from HOADON where NGHD=? and MANV=? and TRANGTHAI='ACTION'", day, self.userID)
      rows = my_cursor.fetchall()
      if rows[0][0]==None or rows[0][0]=="":
        return 0
      else:
        return rows[0][0]
    except Exception as e:
       messagebox.showwarning('Warning', f'Xuất hiện một số vấn đề: {str(e)}', parent = self.root)
   
  def dthu_sdon_Thang(self, dk_select):
    try:
      current_date = datetime.now()
      soNgay=self.songaytrongthang(current_date.month, current_date.year)
      ngayBD=str(current_date.year)+"-"+str(current_date.month)+"-1"
      ngayKT=str(current_date.year)+'-'+str(current_date.month)+'-'+str(current_date.day)
      
      conn = pyodbc.connect(database_QLBH[0])
      my_cursor = conn.cursor()
      my_cursor.execute("select " + dk_select + " from HOADON where NGHD>=? and NGHD<=? and TRANGTHAI='ACTION' and MANV=?",ngayBD, ngayKT, self.userID)
      rows = my_cursor.fetchall()
      if rows[0][0] == None or len(rows)==0:
        return 0
      else:
        return rows[0][0]
    except Exception as e:
       messagebox.showwarning('Warning', f'Xuất hiện một số vấn đề: {str(e)}', parent = self.root)
   
  def dthu_sdon_Nam(self, dk_select, varDict):
    try:
      thangBD=1
      thangKT=datetime.now().month
      nam=datetime.now().year
      for i in range(thangBD, thangKT+1):
        ngayBD=str(nam)+"-"+ str(i)+"-1"
        if i == thangKT:
          ngayKT=str(nam)+"-"+ str(i)+"-"+str(datetime.now().day)
        else:
          ngayKT=str(nam)+"-"+ str(i) +"-"+str(self.songaytrongthang(i, nam))
        
        conn = pyodbc.connect(database_QLBH[0])
        my_cursor = conn.cursor()
        my_cursor.execute("select "+ dk_select +" from HOADON where NGHD>=? and NGHD<=? and MANV=? and TRANGTHAI='ACTION'", ngayBD, ngayKT, self.userID)
        rows = my_cursor.fetchall()
        if rows[0][0]==None or rows[0][0]=="":
          varDict[i]=0
        else:
          varDict[i]=rows[0][0]
    except Exception as e:
      messagebox.showwarning('Warning', f'Xuất hiện một số vấn đề: {str(e)}', parent = self.root)
   
  def show_dthu_sdon(self, dkien):
    if dkien == "doanh thu":
      temp=self.dict_doanhthu
    elif dkien == "số đơn":
      temp=self.dict_sodon
    tong=sum(temp.values())
    chieuRong=[0.2 for i in temp.values()]
    plt.xlabel('Tháng')
    plt.ylabel(dkien)
    plt.title('Biểu đồ thể hiện '+dkien+' của nhân viên trong năm!')
    plt.bar(range(len(temp)), list(temp.values()),color='r', width=chieuRong)
    plt.xticks(range(len(temp)), temp.keys())
    plt.show()
  
  def show_dThu_soDon_Nam(self):
    if self.choose.get()==0:
      messagebox.showerror('Error','Vui lòng chọn Doanh thu hoặc Số lượng!', parent=self.root)
    elif self.choose.get()==1:
      self.show_dthu_sdon("doanh thu")
    else:
      self.show_dthu_sdon("số đơn")
