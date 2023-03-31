# Django detail

제목 뭐로 해야할지 모르겠다.

## INSTALLED_APPS

- APP에 대한 접근은 `INSTALLED_APPS`에 등록된 순서대로 한다.

## render, redirect

- `render`가 `INSTALLED_APPS`에 있는 모든 APP에 대해 `templates` 안의 모든 파일/폴더를 조회하기 때문에, `templates` 아래에 APP 이름과 같은 이름의 폴더를 생성한 뒤, 그 폴더에 모든 파일을 넣는다.

    함수 실행이 제대로 되기 위해 APP 폴더의 `views.py` 함수의 `return`인 `render(request, '<html 파일명>')`을 수정한다.

## python 파일과 html 파일의 연결

- `render` 함수의 3번째 인자로 dictionary 형태의 자료를 html 파일에 녹여줄 수 있다.

    html 파일에서 해당 변수 사용을 원하면, `key` 값을 중괄호 2개로 감싸면 `value`를 얻을 수 있다.
    
    중괄호 안에 `key` 값 앞뒤로 공백 2개를 넣는 게 convention이다.

## DTL(django template language)

- html 파일내에서 논리 구조를 실행할 수 있도록 해준다. 중괄호 1개는 논리 구조, 중괄호 2개는 출력할 경우 사용한다.

    html 모듈화: html 파일에서 반복되는 부분을 다른 파일을 `import` 하는 것처럼 가져오게 할 수 있다. 


## base.html

- `master app`의 `settings.py`에서 `TEMPLATES` 리스트의 `DIRS` 리스트는 `INSTALLED_APPS`에 없는 `templates` 폴더도 자동으로 조회하게 해준다.

    이를 이용하여 웹 페이지 기본 틀을 모듈화하여 사용할 수 있다.

## GET과 POST

- GET 방식으로 URL을 넘기면 사용자의 입력이 모두 URL에 들어있기에 보안에 취약하다. 이를 해결하기 위해 POST 방식을 사용한다.

    POST 방식에서 인증 도장과 같은 역할을 하는 csrf_token이 존재한다. POST 방식으로 받으려면

    1. `form` 태그의 `method`를 POST로 바꾼다.
    2. `form` 태그 안에 `{% csrf_token %}`를 입력한다. (인증 도장)
    3. `view.py`에서 POST 방식으로 받는다.

        ```
        request.POST['<attribution>']
        ```

    DB 등 서버에 영향을 끼치는 사용자 입력은 반드시 POST로 받는다. ex) DB 추가, 수정, 삭제 등

## Variable Routing

```
# /myapp/hello/name/
path('hello/<str:name>/', views.hello, name='str_hello')
```

- `<str:name>`: URL에서 `name` 부분을 변수로 받을 수 있다.

- `str_hello`: `{% url 'str_hello' %}`과 같이 다른 html 파일에서 변수로 사용할 수 있다.

- 즉, 아래 두 코드는 결과가 같다. 개발자 도구에서 URL을 확인하면 같음을 알 수 있다.

    ```
    <form action="/blog/create/" method="POST">
    <form action="{% url 'create' %}" method="POST">
    ```

## forms

- 사용자 입력과 관련된 도구이다.

- `forms.py`의 필요성

    1. 사용자 입력의 유효성 검증(Validation) - 중요
    2. Views에서 입력 <=> 필드 직접 매칭 귀찮음
    3. HTML에서 input 태그 생성 귀찮음

- 모델과 form의 연결

    ```python
    form = <FormClass>(instance=<instance_name>)
    # 또는
    form = <FormClass>(request.POST, instance=<instance_name>)
    ```

## 구분자

1. `.` => 파이썬 모듈을 지칭할 때 .py 와 관련
2. `/` => 폴더 안에 파일 .html 명시할 때
3. `:` => url name 을 구분할 때 `app_name:patter_name`

## 다른 app과 이름이 겹치는 함수가 있을 경우,

- `app`내의 `urls.py`에서 `app_name = '<app이름>`을 선언하면, Variable Routing 에서 URL name을 구분할 때, `<app이름>:<나머지URL>`과 같이 사용할 수 있다.

## [HTTP status code](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

- 서버가 보내오는 응답

    2xx: 성공. 모두 200에 포함될 수 있다
    3xx: redirect가 성공했다는 의미
    4xx: 클라이언트 에러 응답
    5xx: 서버 에러 응답

- 좋은 웹은 책임소재가 명확해야한다.

- 단일 인스턴스를 찾을 때, 아래와 같이 작성한다.

```python
# views.py
from django.shortcuts import get_object_or_404

# question = Question.objects.get(pk=question_pk)( <= 기존 코드
<instance> = get_object_or_404(Question, pk=<instance_pk>)
```

## 클라이언트 오류로 인한 HTTP status code 출력

- 아래와 같이 함수의 데코레이터로 활용한다.

```python
# views.py
from django.views.decorators.http import require_POST, require_safe, require_http_methods

@require_safe
@require_POST
@require_http_methods(['GET', 'POST'])
def <def_name>:
    pass
```

1. require_safe: GET과 HEAD 방식만 받음
2. require_POST: POST 방식만 받음
3. require_http_methods(['GET', 'POST']): 지정한 방식만 받음 
