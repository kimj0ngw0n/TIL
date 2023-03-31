# Function

## Function 1

1. 함수를 쓰는 이유

- 가독성

- 재사용성

- 유지보수

2. Argument

- Parameter: 함수에 입력으로 전달된 값을 받는 변수

- Argument: 함수를 호출할때 전달되는 실제 값

- Positional Arguments: 매개변수와 인자의 위치를 일치시키는 인자

```python
def func(a, b):
    pass
```

- Default Arguments Values: 기본값이 지정된 인자

```python
def func(a, b=0):
    pass
```

- Keyword Arguments: 변수 이름을 특정해 값을 전달하는 인자, keyword arguments 다음에 positional arguments 을 활용할 수 없다.

```python
def func(a, b):
    pass

func(1, b='test')
```

- Arbitrary Argument Lists: 임의의 개수의 positional arguments를 받는다. parameter 이름은 `*args`가 국룰이다.

```python
def func(a, b, *args):
    pass
```

- Arbitrary Keyword Arguments: 임의의 개수의 keyword arguments를 받는다. parameter 이름은 `**kwargs`가 국룰이다.

```python
def func(a, b=0, *args, **kwargs):
    pass
```


## Function 2

1. Python에서 def로 묶이는 함수 박스가 Global/Local scope의 기준이다.

2. Resolution 규칙

- python에서 식별자들은 namespace에 저장되어 있다. LEGB Rule에 따라 이름을 찾아나간다.

    1. Local scope: 함수
    2. Enclosed scope: 특정 함수의 상위 함수, 상대적 공간
    3. Global scope: 함수 밖의 변수 혹은 import된 모듈
    4. Built-in scope: 파이썬 안에 내장되어 있는 함수 또는 속성

3. 하위 scope에서 상위 scope의 변수에 접근은 가능하지만, 해당 변수를 재할당할 수는 없다. 하지만, reference type에서 namespace 값이 가리키는 값은 수정할 수 있다. (04_data_methods 참고)

```python
l = [1, 2, 3]

def func():
    l[0] = 100
    print(l)

func()
```

4. map(function, iterable)

- iterable 의 모든 요소에 function을 적용하고 map object 형태로 결과를 돌려준다.

5. filter(function, iterable)

- iterable 의 모든 요소에 function을 적용하고 반환된 결과가 True인 것들만 filter object 형태로 돌려준다.

6. lambda 함수

- 익명함수로 간단한 조건문을 임시로 만든다. 아래와 같이 쓰일 수 있다.

```python
list(filter((lambda member: member['age'] > 19), members))
```