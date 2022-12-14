# nCnt_Machine
배포 소스코드 repository
http://114.71.48.94:8080/

![analysis](https://user-images.githubusercontent.com/101448204/199458387-33d5d9fe-1441-4099-9a29-7ccd35715058.jpg)
![4analysis](https://user-images.githubusercontent.com/101448204/202064192-ce60c47d-4bf2-4c19-9632-b7db4621beb7.jpg)



<성능>



개발 기간: 8/31 ~ 10/31

11/2
  - 머신 위치 변경에 따른 블러딩 범위 변경
  - 블러딩 크기 변경
  - 개발자용 분석 결과 이미지 인식률 표현 박스 추가

10/31
  - 정식 버전 배포
  - 페이지 구성 요소 추가 및 변경
  - 거울로 인한 측정 오류 개선: 특정 부분 블러딩 처리
  - Machine 안정화 및 속도 개선: Multi Processing
  - Count 새로고침 방식 변경: 특정 주기 자동 새로고침 방식 > Button을 누를 경우 새로고침 방식으로 변경

시험기간과 과제로 10/12 ~ 10/30 개발 중단

10/11
  - Font 변경
  - Footer 아이콘 링크 제거 (css 적용 오류 발생으로 임시 제거)
  - 두 번째 베타버전 배포

10/7 ~ 10/8
  - 인원수에 따른 이미지 변경: 기존 카카오 라이언 이미지 > 인원수에 따라 이미지 변경

10/4
  - Footer 아이콘 추가
  - HTML Main 크기 수정

10/1
  - 에러 분석: 인원수 분석 값 저장 방식에 문제 확인
  - 전역변수에 인원 수 값에 저장하는 방식으로 임시 해결

9/30
  - 첫 번째 베타버전 배포
  - 에러 확인

9/29
  - HTML 재편
  - 이스터에그 추가
  - Footer 생성
  - 1초 주기 웹페이지 새로고침 방식 구축
  - Contributor 웹페이지 생성

9/20 ~ 9/28
  - nCnt Ver. 1 개발
  - 동방에 머신 설치 및 테스트, 수정

9/19
  - 라즈베리파이4 초기 설정 및 소스 코드 테스트

8/31 ~ 9/18
  - 첫 번째 소스코드 개발
  - 웹페이지 제작

8/7 ~ 8/31
  - 여러 오픈소스 비교 후, YOLO를 사용한 이미지 분석 및 인원 수 추출 방식으로 결정

7/31
  - 머신 제작 시작
  - opencv Tutorial 학습
  - 라즈베리파이 os 설치 및 초기 세팅

5/24 ~ 7/30
  - 프로젝트 기획 및 재료 준비

구동방법  
``` putty: vncserver -geometry 1920x1080```  
```Raspberry Pi: python Yolo_Machine.py   /   uvicorn Fastapi_Machine:app --reload --port=5000 -- host=0.0.0.0```
