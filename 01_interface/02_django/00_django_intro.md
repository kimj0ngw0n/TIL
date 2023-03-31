# [Django](https://developer.mozilla.org/ko/docs/Learn/Server-side/Django) Intro


## MTV 패턴

MVC : Model View Controller

MTV : Model Template VIew

서로 거의 같은 의미를 지닌다.

Flask, FastAPI와 비교했을 때, 기능이 많고 무겁다.

![MTV](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Introduction/basic-django.png)

- View : 중간관리자

- Model : 데이터 관리

- Template : 화면

- URLS : 사용자 요청


## 흐름

1. 사용자의 URL 요청

1. master app의 url.py 확인

1. app의 url.py 확인

1. app의 views.py 확인

1. 해당하는 함수 확인

1. 함수 내용 실행(templates의 html 파일 출력)


## 디렉토리

- 프로젝트 디렉토리의 기준은 `master app`의 `setttings.py`에서 `BASE_DIR = Path(__file__).resolve().parent.parent`로 정의되어 있다. 즉, 기본적으로 `settings.py`의 부모의 부모 디렉토리이다.

- `Django` 프로젝트 내에서 패키지를 `import` 할 경우, 같은 디렉토리에서 검색하고, 없으면 프로젝트 디렉토리 기준 최상단 디렉토리에서 찾는다. 


## HTML 파일 연결

- html 파일을 만들때 반드시 templates 폴더 아래에 모아야 한다.

- html 파일을 연결할 때, render의 첫번째 인자는 request로 고정이다. (마치 인스턴스 매서드의 첫번째 인자가 self 인 것과 같다.) 두번째 인자는 템플릿 이름이다. 

## ORM

- `python` -> `SQL`로 번역해주는 소프트웨어로, `Django`가 이에 해당한다.