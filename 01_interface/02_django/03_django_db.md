# DB

## 1. foreignKey

모델에서 `models.foreignKey`로 외래키를 지정하면, 자동으로 변수명(column 이름) 뒤에 `_id`가 붙는다.

## 2. 성능과 객체화

아래 두 코드는 같은 결과를 출력하지만, 밑의 코드가 더 사람 말에 가깝다. 

```python
<Class>.objects.filter(article=<article>)
<article>.<Class>_set.all()
```

아래 두 코드는 같은 결과를 출력하지만, 위는 파이썬에서 데이터를 모두 불러온 뒤, 찾기 때문에 아래가 더 빠르다.

> `like_users`는 `user`가 `posting`에 좋아요를 누른 것을 기록하는 table이다.

```python
user in posting.like_users.all()
posting.like_users.filter(pk=user.pk).exists()
```


## 3. User Class

django에서는 auth_user라는 회원 관리 DB를 기본적으로 제공한다.

django 측에서 제공하는 기본 model로 충분하더라도, 해당 model은 추후 수정이 불가능하므로, custom model을 생성하라고 권장한다.

회원 app 이름은 accounts가 권장된다.

- 세팅

`settings.py`에서 아래와 같이 작성.

```python
AUTH_USER_MODEL = 'accounts.User'
```

- models 가져오기

`models.py`에서 아래와 같이 상속.

```python
from django.conf import settings

class Article(models.Model):
    '''
    column name
    '''
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
```

- form 가져오기

아래와 같이 작성한다.

```python
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

# user model을 직접 가져오지 않는다.
# 사용자가 설정한 User Class를 리턴한다.
User = get_user_model()


class CustomUserCreationForm(UserCreationForm): 

    class Meta:
        model = User
        fields = ('username', )
```

## 4. 쿠키/세션, 해쉬/솔트

[쿠키와 세션](https://interconnection.tistory.com/74)

[쿠키, 세션, 캐시](https://youtu.be/OpoVuwxGRDI)

[해시와 솔트](https://st-lab.tistory.com/100)

## 5. `login_required` 데코레이터

로그인이 되어 있으면 통과하고, 안 되어 있으면 기존에 제출한 URL의 `next` 파라미터에 담아서, `settings.py` 파일의 `LOGIN_URL`로 지정되어 있는 URL로 이동한다.

예를 들면 `settings.py`에 아래와 같이 작성한다.

```python
LOGIN_URL = '/accounts/signin/'
```

## 6. 참조

정참조: 클래스에 있는 내용을 직접 참조

역참조: 클래스에 없는 내용을 `_set` 등을 활용하여 참조

model에서 외래키 또는 n&m 관계의 column 선언부에서 `related_name='<related_name>'`을 설정하여 `_set`을 활용하지 않고 역참조를 할 수 있다.

외래키 또는 n&m 관계가 2개 이상이면 `related_name`를 설정해야 한다.

## 7. model 기본값

models의 기본값을 빈 값으로 하려면 null=True, 기본값을 지정하려면 default=<value>로 설정하면 된다.

## 8. 자기 참조

자기 참조 형식의 테이블의 경우

`symmetrical=True`(기본값)일 경우, 둘 중 한 방향의 데이터만 입력해도, 양 방향으로 저장된다. 즉, 레코드 2개가 저장된다.

`symmetrical=False`일 경우, add한 데이터만 저장된다.

ex) 전자는 친구추가, 후자는 팔로우 의 개념으로 보면 된다.

## 9. string variable routing

variable routing에서 string 형의 변수를 받을 때, 해당 path 함수를 가장 밑에 배치해야 한다.

string 변수를 받을 때, 다른 url 마저 모두 string으로 인식하기 때문이다.

## 10. render와 redirect

render는 함수의 목적이 보여주기 위함일때 사용한다.

클라이언트가 서버에 URL을 요청하는 함수이기 때문에, 필연적으로 render가 사용된다.