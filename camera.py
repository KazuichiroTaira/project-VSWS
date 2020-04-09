# camera.py

import cv2
import os

output_dirpath = 'output'

class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video = cv2.VideoCapture(0)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self, snap_on):
        success, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream
        if snap_on:
            print('---- SNAP')
            frame_no = int(self.get(cv2.CAP_PROP_POS_FRAMES))
            filepath = os.path.join(output_dirpath, 'frame_{:04d}.png'.format(frame_no))
            print(filepath)
            cv2.imwrite(filepath, image)
        
        ret, jpg = cv2.imencode('.jpg', image)
        # print(ret, jpg)
        return jpg.tobytes()
        # return jpg