import cv2
from datetime import datetime
import time

def picture():
  cap = cv2.VideoCapture(0)
  if cap.isOpened():
      while True:
          ret, frame = cap.read()
          if ret:
              if cv2.waitKey(1) == -1:
                  cv2.imwrite('photo.jpg',frame)
                  break
          else:
              print('no frame')
              break
  else:
      print('no camera!')

  cap.release()
  cv2.destroyAllWindows()

def n_time():
  dt = str(datetime.now())
  current_time = int(dt[17:19])
  if  current_time % 30 == 0:
    print(dt[0:19]) #picture()
    time.sleep(1)

while True:
  n_time()