"""This module detect faces using the webcam."""

import cv2
import sys
import logging as log
import datetime as dt
from time import sleep

class DetectionController():

    def accessWebCam(self, cascPath):
        """Access the webCam and start detecting faces using the an algoritm
        
        Keyword arguments:
        cascPath -- String path to the face detection algrotim (default '')
        """
        
        faceCascade = cv2.CascadeClassifier(cascPath)
        log.basicConfig(filename='webcam.log',level=log.INFO)

        video_capture = cv2.VideoCapture(0)
        anterior = 0

        while True:
            if not video_capture.isOpened():
                print('Unable to load camera.')
                sleep(5)
                pass

            # Capture frame-by-frame
            ret, frame = video_capture.read()

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30)
            )

            # Draw a rectangle around the faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            if anterior != len(faces):
                anterior = len(faces)
                log.info("faces: "+str(len(faces))+" at "+str(dt.datetime.now()))
                sub_face = frame[y:y+h, x:x+w]
                FaceFileName = "unknowfaces/face_" + str(y) + ".jpg"
                cv2.imwrite(FaceFileName, sub_face)

            # Display the resulting frame
            cv2.imshow('Video', frame)


            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # When everything is done, release the capture
        video_capture.release()
        cv2.destroyAllWindows()