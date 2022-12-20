import _instaloader
import _push_to_s3_n_mysql as pts
import _filectl as ctl
from datetime import date, datetime
import time

def main() :
    ctl.session_file_delete()
    _instaloader.get_image_from_instargram()

    default_path="/home/instargram_crawler"
    blackpink=['jennierubyjane', 'lalalalisa_m', 'roses_are_rosie', 'sooyaaa__']
    

    new_div=''
    for mem in blackpink :
        new_filenames=list()
        new_rows=list()

        dir_path=default_path+"/"+mem
        new_filenames=pts.get_filename_ls(dir_path)

        for i in new_filenames :
            c1,c2,c3,c4,c5,c6,c7 = pts.imagefile_upload_to_s3(default_path+"/"+mem+"/"+i, i)
            image_row=[c1,c2,c3,c4,c5,c6,c7]
            new_rows.append(image_row)

            ctl.delete_file(default_path+"/"+mem+"/"+i)

        pts.insert_data_to_mysql(new_rows)
    

main()