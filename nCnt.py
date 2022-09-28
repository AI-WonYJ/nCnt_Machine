# -*- coding: utf-8 -*-
from flask import Flask, render_template
import cv2
import numpy as np
from datetime import datetime
import time
import random

# 클래스 리스트
classes = ["person",  "bench", "umbrella", "handbag","bottle", "chair", "bed", "dining table",
           "laptop", "remote", "keyboard", "cell phone", "microwave", "refrigerator", "book"]

net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

def yolo(frame, size, score_threshold, nms_threshold):
  # 이미지의 높이, 너비, 채널 받아오기
  height, width = frame.shape

  # 네트워크에 넣기 위한 전처리
  blob = cv2.dnn.blobFromImage(frame, 0.00392, (size, size), (0, 0, 0), True, crop=False)

  # 전처리된 blob 네트워크에 입력
  net.setInput(blob)

  # 결과 받아오기
  outs = net.forward(output_layers)

  # 각각의 데이터를 저장할 빈 리스트
  class_ids = []
  confidences = []
  boxes = []

  for out in outs:
      for detection in out:
          scores = detection[5:]
          class_id = np.argmax(scores)
          confidence = scores[class_id]

          if confidence > 0.1:
              # 탐지된 객체의 너비, 높이 및 중앙 좌표값 찾기
              center_x = int(detection[0] * width)
              center_y = int(detection[1] * height)
              w = int(detection[2] * width)
              h = int(detection[3] * height)

              # 객체의 사각형 테두리 중 좌상단 좌표값 찾기
              x = int(center_x - w / 2)
              y = int(center_y - h / 2)

              boxes.append([x, y, w, h])
              confidences.append(float(confidence))
              class_ids.append(class_id)

  # Non Maximum Suppression (겹쳐있는 박스 중 confidence 가 가장 높은 박스를 선택)
  indexes = cv2.dnn.NMSBoxes(boxes, confidences, score_threshold=score_threshold, nms_threshold=nms_threshold)

  global ncnt_people

  for i in range(len(boxes)):
      if i in indexes:
          x, y, w, h = boxes[i]
          try:#에러로부터 보호되는 코드부분
            class_name = classes[class_ids[i]]
            if class_name == "person":
                ncnt_people += 1
          except IndexError: #에러가 발생하면 실행되는 부분
            pass #그냥 지나가고 싶다면, pass문을 사용하면 된다.

  return frame

def Cam():  # 웹캠으로 사진 찍기
    cap = cv2.VideoCapture(0)
    if cap.isOpened():
        while True:
            ret, frame = cap.read()
            if ret:
                # cv2.imshow('camera', frame)
                if cv2.waitKey(1) == -1:
                    # time.sleep(1)
                    cv2.imwrite('photo.jpg',frame)
                    break
            else:
                print('no frame')
                break
    else:
        print('no camera!')

    cap.release()

def machine():

    Cam()

    # 이미지 경로
    img = "photo.jpg"

    # 이미지 읽어오기
    frame = cv2.imread(img)

    # 입력 사이즈 리스트 (Yolo 에서 사용되는 네크워크 입력 이미지 사이즈)
    size_list = [320, 416, 608]

    global ncnt_people
    ncnt_people = 0

    frame = yolo(frame=frame, size=size_list[2], score_threshold=0.4, nms_threshold=0.4)
    # cv2.imshow("Output_Yolo", frame)

    print("\n사람 수: {0}명".format(ncnt_people))

    

ncnt_people = "testing_"+str(random.randint(0,10))

with open('ncnt.txt', "w") as file_write:
  file_write.write(ncnt_people)

# machine()

with open('ncnt.txt', "r") as file_read:
  for line in file_read:
    print(line)
    ncnt_people = line
    
    
    
# 여기부터 플래스크 백엔드, 수정해야 함
app = Flask(__name__)

@app.route('/')
def OUTPUT():
    current_time = datetime.now()
    current_time = str(current_time)[0:19]  
    return render_template('index.html', counting = ncnt_people, time = current_time)

if __name__ == '__main__':
    app.debug = True
    app.run()#host='0.0.0.0')
