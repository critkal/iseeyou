
"""This is the main module that will run sequentialy trought downloading, access web cam and the
sending an alert
"""

import os

from controllers.detecter import DetectionController
from controllers.DataController import DataController


def main():
    """Peform a run by calling the downloadForagidos and then runing the face detection"""
    #Saves root directory to further comebacks
    root = os.path.dirname(os.path.abspath('__init__.py'))
    print("downloading images from database")
    data = DataController()
    try:
        #download all images from website
        data.downloadForagidos()
    except Exception as identifier:
        print(identifier)
    #change directory to root
    os.chdir(root)
    #path to the face detection algoritm
    casc_path = "haarcascade_frontalface_default.xml"
    control = DetectionController()
    #acces webcam and start scanning
    control.accessWebCam(casc_path)
    return ""

if __name__ == "__main__":
    main()
    