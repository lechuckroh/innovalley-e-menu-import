# 이노밸리 E동 구내식당 메뉴 임포트

판교 이노밸리 E동 구내식당 메뉴 엑셀파일을 임포트해서 Firebase로 저장하기 위한 CLI.

## 설정파일
`config.json`파일을 생성한 다음, Firebase 접속 정보를 설정한다.

```json
{
  "apiKey": "{API키}",
  "authDomain": "innovalley-e-menu.firebaseapp.com",
  "databaseURL": "https://innovalley-e-menu.firebaseio.com",
  "projectId": "innovalley-e-menu",
  "storageBucket": "innovalley-e-menu.appspot.com",
  "messagingSenderId": "158488195128",
  "appId": "1:158488195128:web:ef2203c01880cd010c36cd",
  "measurementId": "G-CTQ6FR8GJK",
  "email": "lechuckroh@gmail.com",
  "password": "{패스워드}"
}
```
