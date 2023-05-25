# Data Handling

## pandas 데이터처리 및 변환 관련 함수

1. count() : 데이터 개수 반환

- NaN은 세지 않음

1. value_counts() : 데이터 빈도 수 반환

- `dropna=True` (defalt, NaN 무시)

- `ascending=True` (defalt, 오름차순 정렬)

- `normalize=False` (defalt, 범주형 데이터의 비율 계산)

1. sort_index() : 인덱스를 기준으로 정렬

1. sort_values() : 데이터 값을 기준으로 정렬

- `by=기준 열`

- `by=[기준 열1, 기준 열2]`

- `ascending=True/Fasle`

1. sum() : 행/열 합계

- axis=0/1 (열/행의 합계)

1. dropna() : NaN 제거

- `axis=0/1` (NaN 값이 있는 열/행 삭제)

- `inplace=True/False` (원본 데이터에 반영)

1. fillna() : NaN을 다른 값으로 채움

- `axis=0/1` (NaN 값이 있는 열/행 삭제)

- `inplace=True/False` (원본 데이터에 반영)

1. apply() : 동일한 반복 연산에 함수 적용

- `axis=0/1` (열/행 마다 반복)

1. cut() : 데이터 구간 분할

- `cut(data, bins, labels)`

- bins : 구간 경계 값

- labels : 카테고리 값

1. qcut() : 경계선 없이 데이터 수가 동일한 구간으로 분할

- `qcut(data, 구간 수, labels)`

1. set_index() : 열로 인덱스 설정

- 열 -> 인덱스

1. reset_index() : 인덱스 제거하고 열로 추가

- 인덱스 -> 열

1. rename() : 열/행 인덱스 이름 변경

- `rename(index={현재 index:새index})`

- `rename(columns={현재 index:새index})`

```python
df.rename(index={0:'1반',1:'2반', 2:'3반', 3:'4반',4:'5반'}, inplace=True)
```
