# Control Statment

1. Dictionary for문

- key 값을 반복하여 얻는다.

2. Enumerate

- enumerate(iterable, start = 0)

- dictionary 형에 대해서도 사용 가능

3. List Comprehension 사용 예시

- 0으로 채워진 N x M 행렬 생성

```python
[
  [0 for _ in range(n)] for _ in range(n)
]

> [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
```

4. Dictionary comprehension

```python
{num: num ** 3 for num in range(1, 4)}

> {1: 1, 2: 8, 3: 27}
```

5. pass 목적

- 코드 작성 중 임시 명령 또는 코드 확장성을 위해 존재한다.

6. for문의 else

- break 문으로 종료될 경우 실행되지 않음.