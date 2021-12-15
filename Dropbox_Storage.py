import dropbox
import cv2

class Cloud_Storage:
    def __init__(self,access_token):
        self.access_token = access_token
    def takeSnapshot():
        cam = cv2.VideoCapture(0)
        result = True
        while(result == True):
            result,image = cam.read()
            cv2.imwrite("Snapshot.jpg" , image)
            result = False
        cam.release()
        cv2.destroyAllWindows()
    def uploadFiles(self,source,destination):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(source,'rb')
        dbx.files_upload(f.read(),destination)
def main():
    access_token = 'sl.A96ZxuAGWcQPCD_OyOHEguPIhKpVE3akbyw8z_5CFCjU_p11mlPIoOIR0QvXLjkcISu1d5qsVFXXxkZ443jLy-OfHX4vRA_K9J4Vu-QBDoQlmQT4OcP3cI9gSl2SITYd9Hg9ibgwQZF8'
    newUser = Cloud_Storage(access_token)
    source = "Snapshot.jpg"
    destination = input("Enter the destination of your file :- ")
    newUser.uploadFiles(source,destination)
    print("File has been successfully uploaded !!")
main()