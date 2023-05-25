# Series

## 판다스(pandas)의 목적

- 서로 다른 여러 가지 유형의 데이터를 공통된 포맷으로 정리하는 것

- 특히, 행과 열로 이루어진 2차원 구조의 데이터프레임 형식으로 사용

- 데이터 분석 실무에서 사용됨

## Series 생성

- 리스트/튜플로 생성

- 딕셔너리로 생성

- `range()`/`np.arange()`로 생성

## nan

- `None`은 `numpy`에서 연산이 불가능하다.

- 혼동을 막기 위해 `NaN`만 있다고 생각해도 좋다.

## 인덱스 종류

1. 문자형 인덱스

- index를 명시하지 않으면 0부터 시작하는 정수형 인덱스 자동 지정

2. 정수형 인덱스

- 정수형 인덱스로 명시할 경우 0-base 위치 인덱스 사용 못함

3. 위치 인덱스

- 0-base 인덱스

## 슬라이싱

1. 0-base 위치 인덱스를 이용한 슬라이싱

- [start:end] : start ~ end-1 까지 추출

2. 문자(라벨) 인덱스를 이용한 슬라이싱

- [start:end] : start ~ end 까지 추출

## Series의 특징

1. 벡터화 연산

2. Boolean selection

3. 두 시리즈 간의 연산

4. in 연산자 사용 가능

5. for 루프로 key와 value에 접근 가능

```python
for k, v in SERIES.items():
    print(k,' : ', v)

for k in SERIES.keys():
    print(k)

for v in SERIES.values:
    print(v)
```

## Series Method

- size 속성 : 원소 개수 반환  

- shape 속성 : 튜플형태로 shape반환  

- len() : 길이 (원소 개수 반환)

- unique() : 유일한 값만 ndarray로 반환  

- count() : NaN을 제외한 개수를 반환  

- mean(): NaN을 제외한 평균  

- value_counts() : NaN을 제외하고 각 값들의 빈도를 반환 

## date_range(날짜 생성)

`pd.date_range(start, end, periods, freq)`
