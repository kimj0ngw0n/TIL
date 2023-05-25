# Merge

## merge 병합 방식

```python
pd.merge(df1, df2,
         on='key',
         left_on='left_key',
         right_on='right_key',
         left_index=False,
         right_index=False,
         how='병합 방식',
        )
```

- inner, left, right, outer(full outer)

## concat

```python
pd.concat(df1, df2,
          axis=0,  # 행 연결
          join='병합 방식',  # outer, inner
          ignore_index=False,  # Fasle : 기존 index 유지
                               # True  : 0-base 인덱스 설정
          keys=None,  # 다중(계층적) 인덱스 사용하려면 keys 설정
         )
```

- 아래는 다중(계층적) 인덱스 예시이다.

```python
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'], 
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                   index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'E': ['C4', 'C5', 'C6', 'C7'],
                    'F': ['D4', 'D5', 'D6', 'D7']},
                   index=[0, 1, 2, 3])

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'O': ['D8', 'D9', 'D10', 'D11']},
                   index=[1,2,3,4])
```

```python
df = pd.concat([df1, df2, df3], keys=['x', 'y', 'z'])
df
```