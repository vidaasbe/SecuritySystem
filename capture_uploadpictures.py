import cv2
import dropbox
import time
import random

def take_snapshot():
    number = random.randint(0,100)
    #Starting the camera
    #O means primary camera and 1 means secondary camera
    videocaptureobject = cv2.VideoCapture(0)
    result = True
    while(result):
        #Read the frame/Click the picture by using the read function
        ret,frame = videocaptureobject.read()
        #Generate a file name to save the picture using string concatenation
        img_name = "img"+str(number)+".jpg"
        #Use imwrite function to save the image on your computer
        cv2.imwrite(img_name,frame)
        result = False

    print("Picture Taken")
    #Release/Close the camera
    videocaptureobject.release()
    #Close the windows that might have opened during the process
    cv2.destroyAllWindows()
    return img_name

def upload_file(img_name):
    access_token = 'Z9LNmxoHqjoAAAAAAAAAARuMDK8CHZaqG_9CC6Z4On1gBKQMH33cNtmnFf6aSCj9'
    file_to = "/"+img_name
    dbx = dropbox.Dropbox(access_token)
    with open(img_name, 'rb' ) as F:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
        print("File Uploaded")

def main():
    start_time = time.time()
    while True:
        if((time.time()-start_time)>=5):
            name = take_snapshot()
            upload_file(name)
            start_time = time.time()

main()
