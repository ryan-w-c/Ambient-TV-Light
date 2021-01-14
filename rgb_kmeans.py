import numpy as np
import cv2, Queue, threading, time
from rpi_ws281x import PixelStrip, Color

# LED strip configuration:
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN = 10        # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

width = 240
height = 130
ledLength = 31.0 / 16
tvWidth = 47.94
tvHeight = 26.96

pixelHeight = int(tvHeight / ledLength)
pixelWidth = int(tvWidth / ledLength)

# print(pixelWidth, pixelHeight)
LED_COUNT = pixelHeight * 2 + pixelWidth        # Number of LED pixels.


ledSample = height / pixelHeight
# Create NeoPixel object with appropriate configuration.
strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
# Intialize the library (must be called once before other functions).
strip.begin()

# bufferless VideoCapture
# https://stackoverflow.com/questions/43665208/how-to-get-the-latest-frame-from-capture-device-camera-in-opencv
class VideoCapture:

  def __init__(self, name):
    self.cap = cv2.VideoCapture(name)
    self.q = Queue.Queue()
    t = threading.Thread(target=self._reader)
    t.daemon = True
    t.start()

  # read frames as soon as they are available, keeping only most recent one
  def _reader(self):
    while True:
      ret, frame = self.cap.read()
      if not ret:
        break
      if not self.q.empty():
        try:
          self.q.get_nowait()   # discard previous (unprocessed) frame
        except Queue.Empty:
          pass
      self.q.put(frame)

  def read(self):
    return self.q.get()

def blackout():
    for i in range(LED_COUNT):
        strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()
    
cap = VideoCapture(0)
while(True):
    # Capture frame-by-frame
    try:
        
        img = cap.read()
        
        img = cv2.resize(img, (width, height))

        # Display the resulting img
        cv2.imshow('img', img)

        # KMEANS
        ledID = 0
        #right side
        for i in range(pixelHeight, 0, -1):
            #print(width - ledSample," ",(i - 1) * ledSample, " ", width, " ", i * ledSample)
            temp = img[(i - 1) * ledSample:i * ledSample, width - ledSample:width]
            # cv2.imshow(str(i), temp)
            Z = temp.reshape((-1,3))

            # convert to np.float32
            Z = np.float32(Z)

            # define criteria, number of clusters(K) and apply kmeans()
            criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
            ret,label,center=cv2.kmeans(Z,1,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
            r = int(center.item(0))
            g = int(center.item(1))
            b = int(center.item(2))
            strip.setPixelColor(ledID, Color(b, r, g))
            strip.show()
            ledID += 1
        
        #top
        for i in range(pixelWidth, 0, -1):
            # print(0,ledSample, (i - 1) * ledSample,i * ledSample)
            temp = img[0:ledSample, (i - 1) * ledSample:i * ledSample]
            # cv2.imshow(str(i), temp)
            Z = temp.reshape((-1,3))

            # convert to np.float32
            Z = np.float32(Z)

            # define criteria, number of clusters(K) and apply kmeans()
            criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
            ret,label,center=cv2.kmeans(Z,1,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
            r = int(center.item(0))
            g = int(center.item(1))
            b = int(center.item(2))
            strip.setPixelColor(ledID, Color(b, r, g))
            strip.show()
            ledID += 1
        
        #left side
        for i in range(pixelHeight):
            temp = img[i * ledSample:(i + 1) * ledSample, 0:ledSample]
            # cv2.imshow(str(i), temp)
            Z = temp.reshape((-1,3))

            # convert to np.float32
            Z = np.float32(Z)

            # define criteria, number of clusters(K) and apply kmeans()
            criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
            ret,label,center=cv2.kmeans(Z,1,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
            r = int(center.item(0))
            g = int(center.item(1))
            b = int(center.item(2))
            strip.setPixelColor(ledID, Color(b, r, g))
            strip.show()
            ledID += 1

        # for keyboard users
        #if cv2.waitKey(1) & 0xFF == ord('q'):
        #    break
        
    except cv2.error:
        blackout()
        print("something went wrong...")
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()