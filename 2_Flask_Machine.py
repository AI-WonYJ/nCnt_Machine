# ============ Set ============

# -*- coding: utf-8 -*-
from flask import Flask, render_template 
import numpy as np
from datetime import datetime

# 변수 지정
previous_time, standard_time, ncnt_people = 0, 0, 0



# ============ Function ============ 
def check():
  global ncnt_people
  with open("nCnt.txt", "r") as file:
      for line in file.readlines():
        info_list = line.split("/")
        ncnt_people = info_list[0]
        standard_time = info_list[1]
        print("\n", line,"\n")


# ============ Machine ============ 

# 웹 출력    
app = Flask(__name__)

@app.route('/')
def OUTPUT():
    check()
    current_time = datetime.now()  # 실시간 시간 측정
    current_time = str(current_time)[0:19]  # 필요한 부분 가공
    return render_template('new.html', counting = ncnt_people, time = current_time, old_time = standard_time)  # Flask로 new.html에 변수 값 전달

if __name__ == '__main__':
    app.debug = True
    app.run()#host='0.0.0.0')
