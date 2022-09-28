# -*- coding: utf-8 -*-
from flask import Flask, render_template
import cv2
import numpy as np
from datetime import datetime
import time
import random

classes = ["person",  "bench", "umbrella", "handbag","bottle", "chair", "bed", "dining table",
           "laptop", "remote", "keyboard", "cell phone", "microwave", "refrigerator", "book"]
old_time = 0

net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

def yolo(frame, size, score_threshold, nms_threshold):
  height, width = frame.shape
  blob = cv2.dnn.blobFromImage(frame, 0.00392, (size, size), (0, 0, 0), True, crop=False)
  net.setInput(blob)
  outs = net.forward(output_layers)
  class_ids = []
  confidences = []
  boxes = []
  for out in outs:
      for detection in out:
          scores = detection[5:]
          class_id = np.argmax(scores)
          confidence = scores[class_id]
          if confidence > 0.1:
              center_x = int(detection[0] * width)
              center_y = int(detection[1] * height)
              w = int(detection[2] * width)
              h = int(detection[3] * height)
              x = int(center_x - w / 2)
              y = int(center_y - h / 2)
              boxes.append([x, y, w, h])
              confidences.append(float(confidence))
              class_ids.append(class_id)
  indexes = cv2.dnn.NMSBoxes(boxes, confidences, score_threshold=score_threshold, nms_threshold=nms_threshold)
  global ncnt_people
  for i in range(len(boxes)):
      if i in indexes:
          x, y, w, h = boxes[i]
          try:
            class_name = classes[class_ids[i]]
            if class_name == "person":
                ncnt_people += 1
          except IndexError:
            pass
  return frame

def Cam():
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

def machine():
    global old_time
    dt = str(datetime.now())
    current_time = int(dt[17:19])
    if old_time != current_time:
        old_time = current_time
        if  current_time % 3 == 0:
        print(dt[0:19]) #picture()
    Cam()
    img = "photo.jpg"
    frame = cv2.imread(img)
    size_list = [320, 416, 608]
    global ncnt_people
    ncnt_people = 0
    frame = yolo(frame=frame, size=size_list[2], score_threshold=0.4, nms_threshold=0.4)
    print("\n사람 수: {0}명".format(ncnt_people))



with open('ncnt.txt', "w") as file_write:
  file_write.write(ncnt_people)

# machine()

with open('ncnt.txt', "r") as file_read:
  for line in file_read:
    print(line)
    ncnt_people = line
    
    

app = Flask(__name__)

@app.route('/')
def OUTPUT():
    current_time = datetime.now()
    current_time = str(current_time)[0:19]  
    return render_template('index.html', counting = ncnt_people, time = current_time)

if __name__ == '__main__':
    app.debug = True
    app.run()#host='0.0.0.0')
