# Django Setting

세팅은 나중에 다시 세팅할 때 길을 잃지 않도록 기록함.

- django 프로젝트 생성(대문자로)하고 해당 프로젝트 디렉토리로 이동

```
$ mkdir <PROJECT_NAME>
$ cd <PROJECT_NAME>
```

- 프로젝트 폴더 내부에 <폴더명> (이하 \<venv\>)라는 폴더로 파이썬 가상독립환경 만들기

```
$ python -m venv <venv>
```

- venv 활성화(windows, mac) == 사용 중인 파이썬 디렉토리 변경

```
$ source <venv>/Scripts/activate
$ source <venv>/bin/activate
```

- venv 비활성화(windows)

```
$ deactivate
```

- pip 설치 내역 깔끔한지 확인

```
$ pip list
```

- 현재 python이 venv 내부의 파이썬이 맞는지 확인

```
$ which python
```

- 원하는 pip 패키지 설치

```
$ pip install django3.2.18 django_extensions
```

이후 VSCode 사용시 `Ctrl + Shift + p` - `interpreter` - `python interpreter` 선택 - 원하는 가상환경 선택

`django_extensions`는 `shell_plus`를 위함.

- 마스터 앱과 manage.py 생성하기 (소문자로)

```
$ django-admin startproject <project_name>
```

또는

```
$ django-admin startproject <project_name> .
```

- 서버 실행하여 잘 나오는지 확인

```
$ python manage.py runserver
```

- APP 생성

```
python manage.py startapp <appname>
```

이후 `master app`의 `setting.py`에서 `INSTALLED_APPS`에 app을 추가한다. 반드시 쉼표 찍을 것.

- `migration` 파일 생성 및 DB에 변경내역 적용

```
$ python manage.py makemigrations <APP_NAME>
$ python manage.py migrate <APP_NAME>
```

`APP_NAME` 생략 시 모든 `app`에 대해 migrate 한다.

`makemigrations`을 10000번 하면 에러가 나지 않고 `/migrations/10000...` 의 형태로 계속 파일이 생성된다.