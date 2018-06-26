from controllers.detecter import DetectionController
from controllers.DataController import DataController
import os

def main():
    ROOT_DIR = os.path.dirname(os.path.abspath('__init__.py'))
    print (ROOT_DIR)
    print ("downloading images from database")
    data = DataController()
    try:
        data.downloadForagidos()
    except Exception as identifier:
        print identifier
    os.chdir(ROOT_DIR)
    cascPath = "haarcascade_frontalface_default.xml"
    control = DetectionController()
    control.accessWebCam(cascPath)
    return ""

if __name__ == "__main__":
    main()