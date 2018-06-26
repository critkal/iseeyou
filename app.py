import cv2
import sys
import logging as log
import datetime as dt
from time import sleep
from iseeyou.controllers import DetectionControler

cascPath = "haarcascade_frontalface_default.xml"
DetectionControler.accessWebCam(cascPath)