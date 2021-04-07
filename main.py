import cv2
imgcapture=cv2.VideoCapture(0)
result=input("do you want to capture the photo:[Y/N]")
while(result=='Y' or result=='y' ):
    ret, frame = imgcapture.read()
    cv2.imwrite(input("enter name photo file:"), frame)
    print("image capture ................")
    result = input("do you want to capture the photo:[Y/N]")
imgcapture.release()