import re
import pyodbc

database_QLBH = ['Driver={SQL Server Native Client 11.0};'
  'Server=MSI\SQLEXPRESS;'
  'Database=QLBH;'
  'Trusted_Connection=yes;'
]

def search_index(query, options):
  list_row=[]
  for i in range(len(options)):
    result=re.findall(query.lower(), options[i].lower())
    if result!=[]:
      list_row.append(i)
  return(list_row)


def get_dataSQL(select_from):
  conn = pyodbc.connect(database_QLBH[0])
  my_cursor = conn.cursor()
  my_cursor.execute('select* from '+select_from+" where TRANGTHAI='ACTION'")
  rows = my_cursor.fetchall()
  conn.commit()
  conn.close()
  return rows

