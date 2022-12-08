import pandas as pd
import pymysql

con = pymysql.connect(host='172.31.78.182', user='root', password='wpsl97',
                       db='blackpink', charset='utf8') # 한글처리 (charset = 'utf8')

cur = con.cursor()

excel_sheet = pd.read_excel('/home/ubuntu/db-backup.xlsx', 
                    sheet_name = 'backup-data', engine='openpyxl')

sql_insert_1 = 'insert into blackpink_img_data values(%s, %s, %s, %s, %s, %s, %s)'
for idx in range(len(excel_sheet)):
    	cur.execute(sql_insert_1, tuple(excel_sheet.values[idx]))
con.commit()

con.close()