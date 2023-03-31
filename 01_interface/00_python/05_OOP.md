# OOP

## 1. 객체 지향과 프로토타입의 이해

[링크](https://black7375.tistory.com/86)

대충 느낌은 알겠지만, 설명할 수 있을 정도로 이해하려면 프로토타입을 선택한 자바스크립트를 공부해봐야 할 것 같다.


## 2. 객체 지향 프로그래밍(Object Oriented Programming)

1. 장점

    코드의 직관성

    활용의 용이성

    변경의 유연성

2. 클래스(Class)와 인스턴스(Instance)

    모든 객체는 특정 클래스의 인스턴스이다.

    type() 함수를 통해 생성된 객체의 클래스를 확인할 수 있다.

3. 속성(attribute)과 메서드(method)

    attribute : 객체의 상태/데이터

    method : 특정 객체가 할 수 있는 행위

4. 인스턴스 메서드

    첫번째 인자로 자기 자신을 호출하는 self가 전달된다.

5. Self

    self의 존재이유는 instance의 attribute 및 method에 접근하기 위해서이다.

```python
class Person:
    
    def test(self):
        self.test()

p2 = Person()
p2.test()
```

    위 코드 실행 시 커널이 죽어버린다. 무한 재귀이기 때문이다.

6. 생성자(constructor)/소멸자(destructor) 메서드

    `__init__(self)` / `__del__(self)` 로 정의

```python
class Person:

def __init__(self, name):
    self.name = name
    print('응애~', self.name)

def __del__(self):
    print('R.I.P. ', self.name)

p1 = Person('김종원')  # 1번
p1 = Person('김종원')  # 2번
```

    재할당 시 생성자가 먼저 실행된다.

7. 스페셜 메서드(Special method)

    `__str__(self)` : 특정 객체를 print 할 때 보여줄 내용 정의

    `__add__` : 덧셈

    `__getitem__` : 인덱싱

    `__gt__` : greater

    `__eq__` : equal

8. 국룰

    일반 변수/함수명은 전부 소문자 및 띄어쓰기가 필요하면 `_`로 사용. 이를 snake_case라 한다.

    클래스명은 첫글자 대문자에, 띄어쓰기가 필요하면 또 대문자로 사용. 이를 PascalCase 또는 UpperCamelCase라 한다.

9. 클래스 변수/메서드

    클래스의 속성으로 모든 인스턴스가 공유된다. 클래스 선언 내부에서 정의한다.

    `@classmethod`라는 데코레이터를 사용하여 정의한다. `self`처럼 첫 번째 인자로 `cls`가 전달된다.

10. 스태틱 메서드(Static method)

    `@staticmethod`라는 데코레이터를 사용하여 정의한다. 클래스가 사용할 메서드로, 자동으로 전달되는 인자(`self` `cls`)가 없다.

11. 인스턴스와 클래스 간 이름 공간(namespace)

    변수는 LEGB 순으로 찾고, 객체의 속성이나 메서드는 instance - class - 상위 class ... 순으로 찾는다.

12. 인스턴스와 메서드

    인스턴스는 인스턴스/클래스/정적 메서드 모두에 접근 가능하다.

    - 인스턴스에서 클래스/스태틱 메서드는 호출하지 않는다. (국룰)

    인스턴스가 할 행동은 모두 인스턴스 메서드로 한정 지어 설계한다.

13. 클래스와 메서드

    클래스는 인스턴스/클래스/정적 메서드 모두에 접근 가능하다.

    - 클래스에서 인스턴스 메서드는 호출하지 않는다. (국룰)

    클래스 자체(cls)와 그 속성에 접근할 필요가 있다면 `클래스 메서드`로 정의. (국룰)

    클래스 자체(cls)와 그 속성에 접근할 필요가 없다면 `정적 메서드`로 정의. (국룰)

14. 상속

```python
class ChildClass(ParentClass):
    <code block>
```

    코드의 재사용성이 높아짐.

    issubclass(class, classinfo) : class가 classinfo의 subclass인 경우 `True` 반환

    isinstance(object, classinfo) : object가 classinfo의 인스턴스거나 subclass인 경우 True를 반환.

    모든 클래스는 type 클래스를 상속받았다.

    super() : 부모 클래스의 내용을 사용하고자 할 때 사용.

15. 메서드 오버라이딩

    자식 클래스에서 부모 클래스의 메서드를 재정의하는 것.

16. Public Member

    `_` 없이 시작하는 메서드나 속성. 어디서나 호출 가능. 하위 클래스에서 메서드 오버라이딩 허용.

17. Protected Member

    `_` 로 시작하는 메서드나 속성. 암묵적으로 부모 클래스 내부 및 자식 클래스에서만 호출 가능. 하위 클래스에서 메서드 오버라이딩 허용.

18. Private Member

    `__`로 시작하는 메서드나 속성. 본 클래스 내부에서만 사용 가능. 하위 클래스 상속 및 호출 불가능. 외부 호출 불가능.
