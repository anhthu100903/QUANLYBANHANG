from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import pyodbc
import sys
sys.path.append('E:\hk2_namII\TuHoc\QuanLiBanHang')
from sqlConnect import*

f = font=("times new roman", 12)
bgColor = '#f3d8d6'
fgColor = "#fefffa"


class sanPham_win:
  def __init__(self, root):
    self.root = root
    
    sanPham_frame = Frame(root, bg=bgColor)
    sanPham_frame.place(x=0, y=0, width=1000, height=620)
    
    #===================== title ===================
    title_lb = Label(sanPham_frame, text="Sản Phẩm", font=("times newroman", 24, "bold"), fg='red', bg=bgColor)
    title_lb.place(x=0, y=0, width=200, height=50)
    
    # ==================== frame content =======================
    content_frame = LabelFrame(sanPham_frame, bg=bgColor, text="Danh Sách Sản Phẩm", font=("times new roman", 18, "bold"), bd=4, relief=RIDGE)
    content_frame.place(x=10,y=50, width=980, height=560)
    
    # ================== search ============================
    search_lb = Label(content_frame, text="Tìm Kiếm", bg='#89cff0', font=f)
    search_lb.place(x=20, y=20, width=70,height=40)
        
    self.var_searchCombobox = StringVar()
    search_combo = ttk.Combobox(content_frame,textvariable=self.var_searchCombobox, state='readonly', font=f, width=23)
    search_combo["value"]=('MASP', 'TENSP', 'MADM')
    search_combo.current(0)
    search_combo.place(x=95, y=20, width=75, height=40)
    
    self.var_search = StringVar()
    search_txt = ttk.Entry(content_frame, textvariable=self.var_search, font=f)
    search_txt.bind("<KeyPress>", self.search)
    search_txt.place(x=175, y=20, width=250, height=40)
   
    # =================== show data table ===============
    dsSanPham_tableFrame = Frame(content_frame, bg='white', bd=2, relief=RIDGE)
    dsSanPham_tableFrame.place(x=25, y=100, width=920, height=400)
    
    scroll_x = ttk.Scrollbar(dsSanPham_tableFrame,orient=HORIZONTAL)
    scroll_y = ttk.Scrollbar(dsSanPham_tableFrame,orient=VERTICAL)
    
    self.thongTinSP_table = ttk.Treeview(dsSanPham_tableFrame, column=('maSanPham', 'sanPham', 'gia', 'donViTinh', 'nguonGoc', 'kho', 'madm'),
                                         xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
    
    scroll_x.pack(side=BOTTOM, fill=X)
    scroll_y.pack(side=RIGHT, fill=Y)
    
    scroll_x.config(command=self.thongTinSP_table.xview)
    scroll_y.config(command=self.thongTinSP_table.yview)
    
    self.thongTinSP_table.heading('maSanPham', text='Mã Sản Phẩm')
    self.thongTinSP_table.heading('sanPham', text='Sản Phẩm')
    self.thongTinSP_table.heading('gia', text='Giá')   
    self.thongTinSP_table.heading('donViTinh', text='Đơn Vị Tính')
    self.thongTinSP_table.heading('nguonGoc', text='Nguồn Gốc')
    self.thongTinSP_table.heading('kho', text='Kho')
    self.thongTinSP_table.heading('madm', text='MADM')
    
    self.thongTinSP_table['show'] = 'headings'
    
    self.thongTinSP_table.column('maSanPham', width=100, anchor=CENTER)
    self.thongTinSP_table.column('sanPham', width=100, anchor=CENTER)
    self.thongTinSP_table.column('donViTinh', width=50, anchor=CENTER)
    self.thongTinSP_table.column('nguonGoc', width=75, anchor=CENTER)
    self.thongTinSP_table.column('gia', width=100, anchor=CENTER)
    self.thongTinSP_table.column('kho', width=50, anchor=CENTER)
    self.thongTinSP_table.column('madm', width=50, anchor=CENTER)
    
    self.thongTinSP_table.pack(fill=BOTH, expand=1)
    self.load_data()
    
  #============================ Liên Kết Database ==================
  
  def load_data(self):
    try:
      conn = pyodbc.connect(database_QLBH[0])
      my_cursor = conn.cursor()
      my_cursor.execute("select* from SANPHAM where TRANGTHAI='ACTION'")
      rows = my_cursor.fetchall()
      self.thongTinSP_table.delete(*self.thongTinSP_table.get_children())
      if len(rows)!=0:
        for i in rows:
          list = []
          for j in range(1, 10):
            if j == 4 or j==8:
              continue
            list.append(i[j])
          self.thongTinSP_table.insert("", END, values=list)
        conn.commit()
      conn.close()
    except Exception as e:
      messagebox.showwarning('Warning', f'Xuất hiện một số vấn đề: {str(e)}', parent = self.root)
  
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
      self.thongTinSP_table.delete(*self.thongTinSP_table.get_children())
      for i in ds_index:
        list = []
        for j in range(1, 10):
          if j == 4 or j==8:
            continue
          list.append(ds[i][j])
        self.thongTinSP_table.insert("", END, values=list)
    elif len(query)<1:
      self.load_data()
    
if __name__ == "__main__":
  root = Tk()
  ojb = sanPham_win(root)
  root.mainloop()   