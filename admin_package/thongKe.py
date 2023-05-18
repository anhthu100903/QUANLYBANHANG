import matplotlib.pyplot as plt #pip install matplotlib
from tkinter import*
from tkinter import ttk
from tkinter import Tk

from admin_package.xuLyThongKe import xuLy
from tkinter import messagebox

f = font=("times new roman", 12)
bgColor = '#f3d8d6'
fgColor = "#fefffa"

class thongKe_win:
    def __init__(self, root):
        self.root = root
        # if flag=='menu':
        #     self.root.geometry('1000x620+250+40')
        #     self.root.overrideredirect(True)
        
        self.xl = xuLy(self.root)

        thongKe_frame = Frame(self.root, bg=bgColor)
        thongKe_frame.place(x=0, y=0, width=1000, height=620)
        
        #===================== title ===================
        title_lb = Label(thongKe_frame, text="Thống Kê", font=("times newroman", 24, "bold"), fg='red', bg=bgColor)
        title_lb.place(x=0, y=0, width=350, height=50)
        
        #=====================Doanh Số frame =============
        doanhSo_frame = LabelFrame(thongKe_frame, text=' Thống Kê Doanh Số Và Lợi Nhuận ', bd=4, relief="sunken", font=f, bg=bgColor)
        doanhSo_frame.place(x=30, y=60, width=430, height=250)
        
        lb_title =Label(doanhSo_frame, text='', bg=bgColor, font=f)
        lb_title.grid(row=0,column=0, padx=20,pady=5)
        lb_homNay = Label(doanhSo_frame, text='7 Ngày: ', bg=bgColor, font=f)
        lb_homNay.grid(row=1,column=0, padx=20, pady=5)
        lb_tuan = Label(doanhSo_frame, text='4 Tuần: ', bg=bgColor, font=f)
        lb_tuan.grid(row=2,column=0, padx=20, pady=5)
        lb_thang = Label(doanhSo_frame, text='', bg=bgColor, font=f)
        lb_thang.grid(row=3,column=0, padx=20, pady=5)
        m =self.xl.clickNgay()[len(self.xl.clickNgay())-1].split('-')[1]
        lb_thang.config(text=(str(m)+' Tháng'))
            #+++++++++++
        lb_titleDS =Label(doanhSo_frame, text='Doanh Số', bg=bgColor, font=f)
        lb_titleDS.grid(row=0,column=1, padx=20,pady=5)
        lb_homNayDS = Label(doanhSo_frame, text='', bg=bgColor, font=f)
        lb_homNayDS.grid(row=1,column=1, padx=20, pady=5)
        dshn = sum(self.xl.doannhSo_Ngay())
        lb_homNayDS.config(text=str(dshn))
        
        lb_tuanDS = Label(doanhSo_frame, text='', bg=bgColor, font=f)
        lb_tuanDS.grid(row=2,column=1, padx=20, pady=5)
        dst=sum(self.xl.doannhSo_Tuan_Thang(self.xl.clickTuan()))
        lb_tuanDS.config(text=str(dst))
        
        lb_thangDS = Label(doanhSo_frame, text='', bg=bgColor, font=f)
        lb_thangDS.grid(row=3,column=1, padx=20, pady=5)
        dsthang=sum(self.xl.doannhSo_Tuan_Thang(self.xl.clickThang()))
        lb_thangDS.config(text=str(dsthang))
        
            #++++++++++++++++++++
        lb_titleDS =Label(doanhSo_frame, text='Lợi Nhuận', bg=bgColor, font=f)
        lb_titleDS.grid(row=0,column=2, padx=20,pady=5)
        lb_homNayLN = Label(doanhSo_frame, text='', bg=bgColor, font=f)
        lb_homNayLN.grid(row=1,column=2, padx=20, pady=5)
        lnhn=dshn-sum(self.xl.giaVon_ngay())
        lb_homNayLN.config(text=lnhn)
        
        lb_tuanLN = Label(doanhSo_frame, text='', bg=bgColor, font=f)
        lb_tuanLN.grid(row=2,column=2, padx=20, pady=5)
        lnt=dst-sum(self.xl.giaVon_Tuan_thang(self.xl.clickTuan()))
        lb_tuanLN.config(text=lnt)
        
        lb_thangLN = Label(doanhSo_frame, text='', bg=bgColor, font=f)
        lb_thangLN.grid(row=3,column=2, padx=20, pady=5)
        lnthang=dsthang-sum(self.xl.giaVon_Tuan_thang(self.xl.clickThang()))
        lb_thangLN.config(text=lnthang)
        
            #Chức năng
        lb_showDS = Label(doanhSo_frame, text='Xem bảng thống kê theo:', bg=bgColor, font=f, fg='red')
        lb_showDS.place(x=15, y=175, width=170, height=30)
        btn_ngay=Button(doanhSo_frame, text='Ngày',command=self.xl.show_dSo_ngay, bg='#89cff0',font=f)
        btn_ngay.place(x=220,y=175,width=60, height=35)
        btn_tuan=Button(doanhSo_frame, text='Tuần', command=self.xl.show_tuan, bg='#89cff0',font=f)
        btn_tuan.place(x=285,y=175,width=60, height=35)
        btn_thang=Button(doanhSo_frame, text='Tháng', command=self.xl.show_thang,  bg='#89cff0',font=f)
        btn_thang.place(x=350,y=175,width=60, height=35)
    
    
        
        
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++




        #=====================Số Lượng Sản Phẩm frame =============
        slSanPham_frame = LabelFrame(thongKe_frame, text=' Thống Kê Số Lượng Sản Phẩm Đã Bán ', bd=4, relief='raised', font=f, bg='white', fg='red')
        slSanPham_frame.place(x=540, y=60, width=430, height=250)
        
        lbsp_title =Label(slSanPham_frame, text='', bg='white', font=f)
        lbsp_title.grid(row=0,column=0, padx=20,pady=5)
        lbsp_homNay = Label(slSanPham_frame, text='Hôm Nay: ', bg='white', font=f)
        lbsp_homNay.grid(row=0,column=1, padx=20, pady=5)
        lbsp_tuan = Label(slSanPham_frame, text='7 Ngày: ', bg='white', font=f)
        lbsp_tuan.grid(row=0,column=2, padx=20, pady=5)
        lbsp_thang = Label(slSanPham_frame, text='Tháng: ', bg='white', font=f)
        lbsp_thang.grid(row=0,column=3, padx=20, pady=5)
            #+++++++++++
        lbsp_titleDB =Label(slSanPham_frame, text='Đã Bán: ', bg='white', font=f)
        lbsp_titleDB.grid(row=1,column=0, padx=20,pady=5)
        lbsp_homNayDB = Label(slSanPham_frame, text='', bg='white', font=f)
        lbsp_homNayDB.grid(row=1,column=1, padx=20, pady=5)
        spslhomnay = self.xl.sLuongBanNgay()
        tongSLNgay=sum(list(spslhomnay.values()))
        lbsp_homNayDB.config(text=str(tongSLNgay))
        
        lb_tuanDB = Label(slSanPham_frame, text='', bg='white', font=f)
        lb_tuanDB.grid(row=1,column=2, padx=20, pady=5)
        spslTuan = self.xl.sLuongBan_Tuan_Thang(self.xl.clickTuan())
        tongTuan=sum(list(spslTuan.values()))
        lb_tuanDB.config(text=str(tongTuan))
        
        lb_thangDB = Label(slSanPham_frame, text='', bg='white', font=f)
        lb_thangDB.grid(row=1,column=3, padx=20, pady=5)
        spslThang = self.xl.sLuongBan_Tuan_Thang(self.xl.clickThang())
        tongThang=sum(list(spslThang.values()))
        lb_thangDB.config(text=str(tongThang))
        
            #++++++++++++++++++++
        lb_titleKho=Label(slSanPham_frame, text='Số sản phẩm còn trong kho: ', bg='white', font=f)
        lb_titleKho.grid(row=2,columnspan=2, padx=20,pady=5)
        lb_tongKho = Label(slSanPham_frame, text='', bg='white', font=f)
        lb_tongKho.grid(row=2,column=3, padx=20, pady=5)
        lb_tongKho.config(text=self.xl.showTongKho())
    
            #Chức năng
        lb_showSL = Label(slSanPham_frame, text='Xem bảng thống kê theo:', bg='white', font=f, fg='red')
        lb_showSL.place(x=15, y=175, width=170, height=30)
        btn_ngay=Button(slSanPham_frame, text='Ngày',command=self.xl.show_SLNgay, bg='#89cff0',font=f)
        btn_ngay.place(x=220,y=175,width=60, height=35)
        btn_tuan=Button(slSanPham_frame, text='Tuần', command=self.xl.show_SLTuan, bg='#89cff0',font=f)
        btn_tuan.place(x=285,y=175,width=60, height=35)
        btn_thang=Button(slSanPham_frame, text='Tháng', command=self.xl.show_SLThang,  bg='#89cff0',font=f)
        btn_thang.place(x=350,y=175,width=60, height=35)

    
        
        
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++




        #=====================Số Lượng Nhân Viên Bán Được frame =============
        slnvb_frame = LabelFrame(thongKe_frame, text=' Thống Kê Số Đơn Hàng và Doanh Thu Của NVien ', bd=4, relief='raised', font=f, bg='white', fg='red')
        slnvb_frame.place(x=30, y=350, width=430, height=250)
        
        lbsl_title =Label(slnvb_frame, text='', bg='white', font=f)
        lbsl_title.grid(row=0,column=0, padx=10,pady=5)
        lbsl_homNay = Label(slnvb_frame, text='Hôm Nay: ', bg='white', font=f)
        lbsl_homNay.grid(row=0,column=1, padx=10, pady=5)
        lbsl_tuan = Label(slnvb_frame, text='7 Ngày`: ', bg='white', font=f)
        lbsl_tuan.grid(row=0,column=2, padx=10, pady=5)
        lbsl_thang = Label(slnvb_frame, text='Tháng: ', bg='white', font=f)
        lbsl_thang.grid(row=0,column=3, padx=10, pady=5)
            #+++++++++++
        lbsl_titleDB =Label(slnvb_frame, text='Số Đơn Hàng: ', bg='white', font=f)
        lbsl_titleDB.grid(row=1,column=0, padx=10,pady=5)
        lbsl_homNayDB = Label(slnvb_frame, text='', bg='white', font=f)
        lbsl_homNayDB.grid(row=1,column=1, padx=10, pady=5)
        slnvb_homnay = self.xl.SLNVBanNgay()
        tongSLnvbNgay=sum(list(slnvb_homnay.values()))
        lbsl_homNayDB.config(text=str(tongSLnvbNgay))
        
        lb_tuanNVDB = Label(slnvb_frame, text='', bg='white', font=f)
        lb_tuanNVDB.grid(row=1,column=2, padx=10, pady=5)
        slnvb_Tuan = self.xl.SLNVBan_Tuan_Thang(self.xl.clickTuan())
        tongSLNVBTuan=sum(list(slnvb_Tuan.values()))
        lb_tuanNVDB.config(text=str(tongSLNVBTuan))
        
        lb_thangNVDB = Label(slnvb_frame, text='', bg='white', font=f)
        lb_thangNVDB.grid(row=1,column=3, padx=10, pady=5)
        slnvbThang = self.xl.SLNVBan_Tuan_Thang(self.xl.clickThang())
        tongSLNVBThang=sum(list(slnvbThang.values()))
        lb_thangNVDB.config(text=str(tongSLNVBThang))
        
            #+++++++++++c+++++++++


        lbsl_titleThu =Label(slnvb_frame, text='Thu được: ', bg='white', font=f)
        lbsl_titleThu.grid(row=2,column=0, padx=10,pady=5)
        lbsl_homNayThu = Label(slnvb_frame, text='', bg='white', font=f)
        lbsl_homNayThu.grid(row=2,column=1, padx=10, pady=5)
        #lấy daonh thu cuả ngay hiện tại -> phần tử cuối của list
        day=self.xl.doannhSo_Ngay()
        lbsl_homNayThu.config(text=str(day[len(day)-1]))
        
        lb_tuanNVThu = Label(slnvb_frame, text='', bg='white', font=f)
        lb_tuanNVThu.grid(row=2,column=2, padx=10, pady=5)
        #lấy daonh thu cuả tuan hiện tại -> phần tử cuối của list
        week=self.xl.doannhSo_Tuan_Thang(self.xl.clickTuan())
        lb_tuanNVThu.config(text=str(week[len(week)-1]))
        
        lb_thangNVThu = Label(slnvb_frame, text='', bg='white', font=f)
        lb_thangNVThu.grid(row=2,column=3, padx=10, pady=5)
        #lấy daonh thu cuả tháng hiện tại -> phần tử cuối của list
        month=self.xl.doannhSo_Tuan_Thang(self.xl.clickThang())
        lb_thangNVThu.config(text=str(month[len(month)-1]))
            #+++++++++++c+++++++++
            
        self.choose = IntVar()
        lb_radio_SLNVB = Label(slnvb_frame, text="Chọn:", justify = LEFT, padx = 20, font=f, background='white')
        lb_radio_SLNVB.grid(row=3, column=0, padx=10, pady=5)
        ttk.Radiobutton(slnvb_frame,  text="Doanh Thu", variable=self.choose, value=1).grid(row=3, column=1, padx = 10, pady=5)
        ttk.Radiobutton(slnvb_frame,  text="Số Đơn Hàng", variable=self.choose,  value=2).grid(row=3, column=2, padx = 10, pady=30)
        
    
            #Chức năng
        lb_showSL = Label(slnvb_frame, text='Xem bảng thống kê theo:', bg='white', font=f, fg='red')
        lb_showSL.place(x=15, y=175, width=170, height=30)
        btn_ngay=Button(slnvb_frame, text='Ngày',command=self.show_dThu_sLBan_Nv_Ngay, bg='#89cff0',font=f)
        btn_ngay.place(x=220,y=175,width=60, height=35)
        btn_tuan=Button(slnvb_frame, text='Tuần', command=self.show_dThu_sLBan_Nv_Tuan, bg='#89cff0',font=f)
        btn_tuan.place(x=285,y=175,width=60, height=35)
        btn_thang=Button(slnvb_frame, text='Tháng', command=self.show_dThu_sLBan_Nv_Thang,  bg='#89cff0',font=f)
        btn_thang.place(x=350,y=175,width=60, height=35)
        
        
        
        
    
        
        
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++




        
        #===================== Hóa Đơn frame =============
        hoaDon_frame = LabelFrame(thongKe_frame, text=' Thống Kê Số Lượng Đơn Hàng ', bd=4, relief="sunken", font=f, bg=bgColor)
        hoaDon_frame.place(x=540, y=350, width=430, height=250)
        
        lb_titleHD = Label(hoaDon_frame, text='', bg=bgColor, font=f)
        lb_titleHD.grid(row=0,column=0, padx=20,pady=5)
        lb_homNayHD = Label(hoaDon_frame, text='7 Ngày: ', bg=bgColor, font=f)
        lb_homNayHD.grid(row=0,column=1, padx=20, pady=5)
        lb_tuanHD = Label(hoaDon_frame, text='4 Tuần: ', bg=bgColor, font=f)
        lb_tuanHD.grid(row=0,column=2, padx=20, pady=5)
        lb_thangHD = Label(hoaDon_frame, text='', bg=bgColor, font=f)
        lb_thangHD.grid(row=0,column=3, padx=20, pady=5)
        m =self.xl.clickNgay()[len(self.xl.clickNgay())-1].split('-')[1]
        lb_thangHD.config(text=(str(m)+' Tháng'))
        
            #+++++++++++
        lb_titleSLHD =Label(hoaDon_frame, text='Số lượng\n đơn hàng', bg=bgColor, font=f)
        lb_titleSLHD.grid(row=1,column=0, padx=20,pady=5)
        lb_homNaySLHD = Label(hoaDon_frame, text='', bg=bgColor, font=f)
        lb_homNaySLHD.grid(row=1,column=1, padx=20, pady=5)
        slhn = sum(self.xl.SLDon_Ngay())
        lb_homNaySLHD.config(text=str(slhn))
        
        lb_tuanSLHD = Label(hoaDon_frame, text='', bg=bgColor, font=f)
        lb_tuanSLHD.grid(row=1,column=2, padx=20, pady=5)
        sltuan=sum(self.xl.SLDon_Tuan_Thang(self.xl.clickTuan()))
        lb_tuanSLHD.config(text=str(sltuan))
        
        lb_thangSLHD = Label(hoaDon_frame, text='', bg=bgColor, font=f)
        lb_thangSLHD.grid(row=1,column=3, padx=20, pady=5)
        slthang=sum(self.xl.SLDon_Tuan_Thang(self.xl.clickThang()))
        lb_thangSLHD.config(text=str(slthang))
        
        
            #Chức năng
        lb_showDS = Label(hoaDon_frame, text='Xem bảng thống kê theo:', bg=bgColor, font=f, fg='red')
        lb_showDS.place(x=15, y=175, width=170, height=30)
        btn_ngay=Button(hoaDon_frame, text='Ngày',command=self.xl.show_slDon_Ngay, bg='#89cff0',font=f)
        btn_ngay.place(x=220,y=175,width=60, height=35)
        btn_tuan=Button(hoaDon_frame, text='Tuần', command=self.xl.show_slDon_Tuan, bg='#89cff0',font=f)
        btn_tuan.place(x=285,y=175,width=60, height=35)
        btn_thang=Button(hoaDon_frame, text='Tháng', command=self.xl.show_slDon_Thang,  bg='#89cff0',font=f)
        btn_thang.place(x=350,y=175,width=60, height=35)
    
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def show_dThu_sLBan_Nv_Ngay(self):
        if self.choose.get()==0:
            messagebox.showerror('Error','Vui lòng chọn Doanh thu hoặc Số lượng!', parent=self.root)
        elif self.choose.get()==1:
            self.xl.show_TienBanDuocNVNgay()
        else:
            self.xl.show_SLNVNgay()
            
    def show_dThu_sLBan_Nv_Tuan(self):
        if self.choose.get()==0:
            messagebox.showerror('Error','Vui lòng chọn Doanh thu hoặc Số lượng!', parent=self.root)
        elif self.choose.get()==1:
            self.xl.show_TienBanDuocNVTuan()
        else:
            self.xl.show_SLNVTuan() 
            
    def show_dThu_sLBan_Nv_Thang(self):
        if self.choose.get()==0:
            messagebox.showerror('Error','Vui lòng chọn Doanh thu hoặc Số lượng!', parent=self.root)
        elif self.choose.get()==1:
            self.xl.show_TienBanDuocNVThang()
        else:
            self.xl.show_SLNVThang() 




if __name__ == "__main__":
    root = Tk()
    ojb = thongKe_win(root)
    root.mainloop()