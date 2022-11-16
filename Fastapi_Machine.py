# ============ Set ============

# -*- coding: utf-8 -*-
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder
from datetime import datetime
import random

# 변수 지정
standard_time, ncnt_people = 0, 0



# ============ Function ============ 
def check():
  global ncnt_people, standard_time
  with open("nCnt.txt", "r") as file:
      for line in file.readlines():
        info_list = line.split("/")
        ncnt_people = info_list[0]
        standard_time = info_list[1]
        print("\n", line,"\n")


# ============ Machine ============ 

# 웹 출력    
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def Page(request: Request):#, ncnt_people: str, current_time: str, standard_time: str):
    check()
    current_time = datetime.now()  # 실시간 시간 측정
    current_time = str(current_time)[0:21]  # 필요한 부분 가공
    return templates.TemplateResponse("new.html", {"request": request, "counting": int(ncnt_people), "time": current_time, "old_time": standard_time})  # FastAPI로 new.html에 변수 값 전달

@app.get("/nCnt")
async def nCnt():
  check()
  current_time = datetime.now()  # 실시간 시간 측정
  current_time = str(current_time)[0:21]  # 필요한 부분 가공
  jsondata = jsonable_encoder({"counting": int(ncnt_people), "time": current_time, "old_time": standard_time})
  return jsondata

@app.get("/ssccounter_info")
async def nCnt():
  check()
  current_time = datetime.now()  # 실시간 시간 측정
  current_time = str(current_time)[0:21]  # 필요한 부분 가공
  temperature = random.randint(10, 30)
  humidity = random.randint(50, 90)
  dust = random.randint(10, 200);
  jsondata = jsonable_encoder({"temperature": temperature, "humidity": humidity, "dust": dust, "lamp": True, "people_count": int(ncnt_people), "last_time": standard_time, "get_time": current_time, "air_cleaner": True})
  return jsondata