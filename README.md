# 📕중고책 매물 현황 프로젝트

## 📄프로젝트 개요
- 중고책 매물 현황 시각화 프로젝트  
- [블로그 포스팅](https://kgw7401.tistory.com/category/%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8/%EC%95%8C%EB%9D%BC%EB%94%98%20%EC%A4%91%EA%B3%A0%EC%B1%85%20%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8)

## ✏프로젝트 설명
- 알라딘 API를 이용하여 중고책 매물 데이터를 받은 뒤 해당 데이터를 이용하여 중고책 매물 현황을 시각화한다.
- 간단한 데이터 파이프라인을 만들어보면서 ETL 과정을 체험해본다.

## 🛠데이터 파이프라인
<p align="center">
  <img src="https://user-images.githubusercontent.com/78521993/165237530-504a1c9a-66a6-4abb-b8d8-f918517f7719.png" />
</p>
  
- 알라딘 API를 이용하여 추출한 데이터를 필요한 부분만 파싱하여 RDS에 적재한다.
- 적재된 데이터들은 슈퍼셋을 통해 시각화한다. 
- 추출 코드나 슈퍼셋은 EC2에 설치하여 24시간 운용하였고, 워크플로는 크론탭을 이용하였다.

## 🚀프로젝트 결과

https://user-images.githubusercontent.com/78521993/165235852-b12ccc33-131f-4b85-89ad-4cd23f402186.mp4
