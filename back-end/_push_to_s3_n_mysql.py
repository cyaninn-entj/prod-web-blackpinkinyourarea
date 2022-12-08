import boto3
import os
import idpass as id
from datetime import date, datetime
import pymysql

def get_filename_ls(path):
    file_list=os.listdir(path)
    # 확장자명 입력
    file_list_jpg=[file for file in file_list if file.endswith(".jpg")]
    return file_list_jpg


def s3_connection():
    try:
        # s3 클라이언트 생성
        s3 = boto3.client(
            service_name="s3",
            region_name="ap-northeast-2",
            aws_access_key_id=id.awscli_access_key,
            aws_secret_access_key=id.awscli_secret_access_key,
        )
    except Exception as e:
        print(e)
    else:
        return s3


def imagefile_upload_to_s3(local_file_path, filename):
    s3 = s3_connection()
    try:
        s3.upload_file(local_file_path, "blackpinkinyourarea.cyaninn.com", "images/"+filename, ExtraArgs={"ServerSideEncryption": "AES256"})
        print("upload success : "+filename)
    except Exception as e:
        print(e)
    
    #이미지파일 메타데이터 반환
    if filename.count('_') == 3 :
        f_date, f_time, n, f_filenum = filename.split('_')
        num, h = f_filenum.split('.')
    else :
        f_date, f_time, f_name = filename.split('_')
        n, h = f_name.split('.')
        num=1
    
    y, m, d = f_date.split('-')
    url=id.s3_bucket_url+filename
    dl=0
    y=int(y); m=int(m); d=int(d); num=int(num)
    
    return n, y, m, d, num, url, dl


'''
오라클 연결
def insert_data_to_oracle(row_list) :
    os.putenv('NLS_LANG', 'KOREAN_KOREA.AL32UTF8') 
    db = cx_Oracle.connect(id.db_host,id.db_pass,id.db_ip_port_sid)

    print('{}'.format(db.version))
    cursor = db.cursor()
    
    for i in row_list:
        d_name=     i[0]
        d_year=     i[1]
        d_month=    i[2]
        d_day=      i[3]
        d_filenum=  i[4]
        d_s3url=    i[5]
        d_download= i[6]

        try:
            sql = "insert into blackpinkinyourarea values(:1, :2, :3, :4, :5, :6, :7)"
            
            cursor.execute(sql,(d_name, d_year, d_month, d_day, d_filenum, d_s3url, d_download))
            
            result=db.commit()
            
            print("insert seccess : "+d_name,d_year,d_month,d_day,d_filenum)
        except Exception as e:
            print(e)

    cursor.close()
    db.close()
'''

def insert_data_to_mysql(row_list) :

    # mysql connection 연결
    conn = pymysql.connect(
                        host=       id.db_host,
                        port=       3306,
                        user=       id.db_user,
                        password=   id.db_pass,
                        db=         id.db_name,
                        charset=    'utf8')

    cur=conn.cursor()

    try :  
        for i in row_list:
            d_name=     i[0]
            d_year=     i[1]
            d_month=    i[2]
            d_day=      i[3]
            d_filenum=  i[4]
            d_s3url=    i[5]
            d_download= i[6]

            sql = "INSERT INTO blackpink_img_data (DB_MEM_NAME, DB_YEAR, DB_MONTH, DB_DAY, DB_FILENUM, DB_S3URL, DB_DOWNLOAD) \
                        VALUES (%s, %s, %s, %s, %s, %s, %s)"

            cur.execute(sql, (d_name, d_year, d_month, d_day, d_filenum, d_s3url, d_download))

            print('cur excute success :', d_name, d_year, d_month, d_day, d_filenum)
    except :
        print('excute fail : ', d_name, d_year, d_month, d_day, d_filenum)
    
    conn.commit()
    conn.close()
