# 이노밸리 E동 구내식당 메뉴 임포트

판교 이노밸리 E동 구내식당 메뉴 엑셀파일을 임포트해서 Firebase로 저장하기 위한 CLI.

## 설정파일
`config.ini`파일을 생성한 다음, Firebase 접속 정보를 설정한다.

```ini
[Firebase]
apiKey = {API키}
authDomain = innovalley-e-menu.firebaseapp.com
databaseURL = https://innovalley-e-menu.firebaseio.com
projectId = innovalley-e-menu
storageBucket = innovalley-e-menu.appspot.com
messagingSenderId = 158488195128
appId = 1:158488195128:web:ef2203c01880cd010c36cd
measurementId = G-CTQ6FR8GJK
email = {로그인 이메일}
password = {로그인 패스워드}
```

설정파일 값은 환경변수를 사용해서 오버라이드할 수도 있다.
* `INNO_API_KEY`: `apiKey` 설정
* `INNO_EMAIL`: `email` 설정
* `INNO_PASSWORD`: `password` 설정

## 실행
```bash
# 가상환경 활성화
$ source venv/bin/activate

# 필요한 패키지 설치
$ pip install -r requirements.txt

# 메뉴 엑셀 파일 임포트
$ python3 main.py import <메뉴엑셀파일>

# 디렉토리에 있는 모든 메뉴 엑셀 파일 임포트
$ python3 main.py import <디렉토리>
```
