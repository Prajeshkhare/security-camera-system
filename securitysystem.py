from distutils.command.upload import upload
from tkinter import image_names
import cv2
import dropbox
import time
import random

from numpy import number

# def take_snapshot():
# # intializing cv2
#     videoCaptureObject = cv2.VideoCapture(0)
#     result = True
#     while(result):
#         # read the frames while the camera is on
#         ret,frame = videoCaptureObject.read()
#         # cv2.imwrite() method is use to save an image to  any storage device
#         cv2.imwrite("newPicture1.jpg",frame)
#         result = False

#     # releasing the camera
#     videoCaptureObject.release()
#     # closes all the window that might be open during the process
#     cv2.destroyAllWindows()

# take_snapshot()


start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)
# intializing cv2
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        # read the frames while the camera is on
        ret,frame = videoCaptureObject.read()
        # cv2.imwrite() method is use to save an image to  any storage device
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time = time.time
        result = False
    return img_name
    print("snapShotTaken")
    # releasing the camera
    videoCaptureObject.release()
    # closes all the window that might be open during the process
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token = "sl.BBOJSdg2nVteSHSu1o4fAEcp1Qs7Vz1ealYo1Cwt9n4GlQZk3jk6P-JMBA_0zLVK6VDz24KmZ5NlTpE2oNCE1vRLOq_ETG2_wRfs56tzva59utR33Pck4Z-nqXQyrYKwMBb1AytLp1Nx"
    file = img_name
    file_from = file
    file_to = "/testFolder/"+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from,"rb") as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file Uploaded")

def main():
    while(True):
        if((time.time() - start_time ) >= 300 ):
            name = take_snapshot()
            upload_file(name)

main()