import os
from datetime import date, datetime
import idpass as id

def get_image_from_instargram() :
    myid=id.instargram_id
    mypass=id.instargram_pass

    blackpink={"JENNIE":"jennierubyjane", "LISA":"lalalalisa_m", "JISOO":"sooyaaa__", "ROSIE":"roses_are_rosie"}
    

    for key in blackpink:
        #com = 'instaloader --fast-update --post-filter="datetime(yy,mm,td) <= date_utc < datetime(yy,mm,tm)"  --login=my_id -p=my_pass insta_id --no-profile-pic --no-compress-json --no-metadata-json --no-videos --filename-pattern={date_local}_member'
        com = 'instaloader --fast-update --post-filter="datetime(2022,9,30) <= date_utc < datetime(2022,11,1)"  --login=my_id -p=my_pass insta_id --no-profile-pic --no-compress-json --no-metadata-json --no-videos --filename-pattern={date_local}_member'
        com=com.replace("insta_id", f"{blackpink[key]}")
        com=com.replace("my_id", myid)
        com=com.replace("member", f"{key}")
        com=com.replace("my_pass", mypass)
        #com=com.replace("yy", str(y))
        #com=com.replace("mm", str(m))
        #com=com.replace("td", str(d-1))
        #com=com.replace("tm", str(d))
        os.system(com) #파이썬에서 스크립트 실행

get_image_from_instargram()