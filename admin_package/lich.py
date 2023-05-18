from tkinter import *
from tkcalendar import Calendar
from datetime import datetime

#pip install tkcalendar
# creating an object of tkinter
class  lich_win:
   def __init__(self, root):
      self.root = root
      self.root.geometry("300x280+500+200")
      self.root.title("Calendar picker")
      current_date=datetime.now()
      calendar_choose = Calendar(self.root,selectmode = "day",year=current_date.year,month=current_date.month,date=current_date.day)
      #display on main window
      calendar_choose.pack(pady=30)
      # getting date from the calendar 

      def fetch_date():
         date.config(text = "Ngày: " + calendar_choose.get_date())
      #add button to load the date clicked on calendar
      btn_date = Button(self.root,text="Xác nhận: ",command=fetch_date, bg="gray")
      btn_date.place(x=25, y=230, width=75, height=40)
      date = Label(self.root, text="")
      date.place(x=130, y=230, width=100, height=40)
