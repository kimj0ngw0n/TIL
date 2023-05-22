# DataFrame

## dataframe 생성 방법

1. list로 생성

2. dictionary로 생성

- `key`가 열 이름이 되고, `index`가 행 방향 인덱스가 됨

3. series로 생성

4. file로 생성

- `read_csv()`

## 열/인덱스의 이름 설정

```python
df.index.name = 'index_name'
df.columns.name = 'columns_name'
```

## read_csv 주요 파라미터

- sep : 각 데이터 값을 구별하기 위한 구분자(separator) 설정

- header : 헤더(제목) 위치. header를 무시할 경우, None 설정

- skiprows : 제외하는 행 지정

- thousands : 천 단위 구분 표시 제거

- index_col : index로 사용할 열 설정

- usecols : 선택 열 지정

- encoding : 인코딩 설정  

## df.drop(행/열 삭제)

```python
df.drop(인덱스 이름, axis=0, inplace=False)
```

- axis=0 : 행 의미 (디폴트로 생략 가능)

- axis=1 : 열 의미

- inplace=True : 결과 반영 (원본 데이터 변경)
