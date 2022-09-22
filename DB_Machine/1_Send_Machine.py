import cv2
from datetime import datetime
import time


old_time = 0


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
  global old_time
  dt = str(datetime.now())
  current_time = int(dt[17:19])
  if old_time != current_time:
    old_time = current_time
    if  current_time % 3 == 0:
      print(dt[0:19]) #picture()


# 변수에 이전 시간 저장하고, 같으면 pass

while True:
  n_time()
