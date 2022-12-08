import pymysql

def insert_data_to_mysql(row_list) :

    # mysql connection 연결
    conn = pymysql.connect(host='3.39.87.50',
                        port=3306,
                        user='root',
                        password='wpsl97',
                        db='blackpink',
                        charset='utf8')

    cur=conn.cursor()
    
    '''
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
    '''

    try :  
        for i in row_list:
            d_name=     i[0]
            d_filenum=  i[1]

            sql = "INSERT INTO test_1 (usr_name, usr_no) \
                        VALUES (%s, %s)"

            cur.execute(sql, (d_name, d_filenum))
            print('cur excute success :',d_name,d_filenum)
    except :
        print('excute fail')
    
    conn.commit()
    conn.close()

sample_list=[['karina', 22], ['ningning', 20], ['winter', 21], ['giselle', 22]]
insert_data_to_mysql(sample_list)