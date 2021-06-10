from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.resolution = (2592, 1944)
camera.start_preview()
sleep(2)
camera.capture('/home/pi/Desktop/board.png', format = 'png' )
camera.stop_preview()
