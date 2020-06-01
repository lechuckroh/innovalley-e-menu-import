# 이노밸리 E동 구내식당 메뉴 임포트

[![Build Status](https://drone.lechuckcgx.com/api/badges/lechuckroh/innovalley-e-menu-import/status.svg)](https://drone.lechuckcgx.com/lechuckroh/innovalley-e-menu-import)

판교 이노밸리 E동 구내식당 메뉴 엑셀파일을 임포트해서 Firebase로 저장하기 위한 CLI.

## 설정파일
`config.ini`파일을 열어서, Firebase 접속 정보를 설정한다.

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

> Firebase 접속정보는 프로젝트 콘솔의 왼쪽 위에 있는 톱니바퀴 아이콘 -> 프로젝트 설정 -> 일반 -> 내 앱 -> Firebase SDK snippet에서 확인할 수 있다.
> Firebase 사용자 패스워드는 Authentication -> Users 에서 초기화할 수 있다.

설정파일 값은 환경변수를 사용하거나, `.env` 파일을 사용해서 오버라이드할 수도 있다.
* `INNO_API_KEY`: `apiKey` 설정
* `INNO_EMAIL`: `email` 설정
* `INNO_PASSWORD`: `password` 설정

## 실행
```bash
# 가상환경 설치
$ python3 -m venv venv

# 가상환경 활성화
$ source venv/bin/activate

# 필요한 패키지 설치
$ pip install -r requirements.txt

# 메뉴 엑셀 파일 임포트
$ python3 main.py import <메뉴엑셀파일>

# 디렉토리에 있는 모든 메뉴 엑셀 파일 임포트
$ python3 main.py import <디렉토리>
```

### docker를 사용한 실행
`.env` 파일을 생성한 다음, 인증정보를 입력한다:

```dotenv
INNO_API_KEY=<apiKey>
INNO_EMAIL=<email>
INNO_PASSWORD=<password>
```

임포트할 `*.xlsx` 파일을 `./data` 디렉토리에 저장한 후, 다음과 같이 실행한다: 
```bash
$ docker-compose run --rm importer
```

## 빌드
drone.io 를 사용해 빌드하기 위해서는 secret을 등록해야 한다.
* `docker_username`: docker 저장소 사용자
* `docker_password`: docker 저장소 패스워스

drone-cli 를 사용해 로컬에서 빌드하려면 `.env`파일에 secret을 등록한 후 사용한다.
```ini
docker_username=lechuckroh
docker_password=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

drone-cli 를 사용해 빌드:
```bash
$ drone exec --secret-file .env
```
