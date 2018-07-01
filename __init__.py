from controllers.detecter import DetectionController
from controllers.DataController import DataController
import os

def main():
    """Peform a run by calling the downloadForagidos and then runing the face detection"""
    #Saves root directory to further comebacks
    ROOT_DIR = os.path.dirname(os.path.abspath('__init__.py'))
    print ("downloading images from database")
    data = DataController()
    try:
        #download all images from website
        data.downloadForagidos()
    except Exception as identifier:
        print identifier
    #change directory to root
    os.chdir(ROOT_DIR)
    #path to the face detection algoritm
    cascPath = "haarcascade_frontalface_default.xml"
    control = DetectionController()
    #acces webcam and start scanning
    control.accessWebCam(cascPath)
    return ""

if __name__ == "__main__":
    main()