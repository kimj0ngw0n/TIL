# Data Methods

### 1. String : immutable, ordered, iterable

    .find

    .index

    .isalpha

    .isspace

    .isdigit

    .isnumeric

    .replace

    .strip

    .split

    .join


### 2. List : mutable, ordered, iterable

    .append

    .extend : 묶인 것을 풀어서 추가

    .insert

    .remove

    .pop

    .index

    .count

    .sort

    .reverse


### 3. Set : mutable, unordered, iterable

    .add

    .update

    .remove

    .discard : error 없음


### 4. Dictionary : mutable, unordered, iterable

    .get

    .pop

    .update


### 5. 얕은 복사와 깊은 복사

    1. 할당

    같은 주소 값을 할당하여 복사. 두 객체의 값 중 하나만 변경해도 둘 다 변경됨.

    2. 얕은 복사(Shallow copy)

    리스트를 slicing 또는 list() 를 활용하여 복사. 두 객체의 값을 복사하기 때문에 값을 변경 시 따로 변경됨. 하지만 그 값이 다른 값을 가리키는 주소 값일 경우, 다른 값들은 복사가 안된 상태.

    3. 깊은 복사(Deep copy)

    `copy` 모듈의 deepcopy 함수를 사용하여 복사. 내부의 모든 객체까지 새롭게 값이 복사됨.