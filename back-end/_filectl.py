import os

def delete_file(filepath) :
    if os.path.exists(filepath) :
        os.remove(filepath)
        print("delete file : "+filepath[31:])

def session_file_delete() :
    if os.path.exists('/home/ubuntu/.config/instaloader/session-blackpinkcrawling') :
        os.remove('/home/ubuntu/.config/instaloader/session-blackpinkcrawling')
        print("delete file : session-blackpinkcrawling")
        