# 중고책 매물 현황 프로젝트
알라딘 api를 이용하여 중고책 매물 현황을 시각화하는 프로젝트

## 데이터 파이프라인
![image](https://user-images.githubusercontent.com/78521993/165237530-504a1c9a-66a6-4abb-b8d8-f918517f7719.png)  
  
전체적인 흐름은 다음과 같다. 알라딘 API를 이용하여 추출한 데이터를 필요한 부분만 파싱하여 RDS에 적재한다. 그리고 적재된 데이터들은 슈퍼셋을 통해 시각화한다. 추출 코드나 슈퍼셋은 EC2에 설치하여 24시간 운용하였고, 워크플로는 크론탭을 이용하였다.

## 프로젝트 결과

https://user-images.githubusercontent.com/78521993/165235852-b12ccc33-131f-4b85-89ad-4cd23f402186.mp4
