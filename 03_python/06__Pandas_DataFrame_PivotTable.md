# Pivot Table

## pivot 메서드

- `pivot_table(data, values, index, columns, aggfun, fill_value, margins, margins_name)`

1. data : 분석할 데이터 프레임. 메서드 형식일때는 필요하지 않음 ex)df1.pivot_table()

1. values : 분석할 데이터 프레임에서 분석할 열

1. index : 행 인덱스로 들어갈 키열 또는 키열의 리스트

1. columns : 열 인덱스로 들어갈 키열 또는 키열의 리스트

1. aggfunc(agg) : 분석 메소드. mean이 기본 함수

1. fill_value : NaN 대체값 지정

1. margins : 모든 데이터를 분석한 결과를 행열로 추가할 지 여부

1. margins_name : margins가 추가될 때 그 열(행)의 이름`, 여러 개 출력 가능

## pivot table 작성 시 반드시 설정해야 하는 인수

1. data : 사용 데이터 프레임

1. index : 행 인덱스로 사용할 필드(기준 필드로 작용됨)

1. 인덱스 명을 제외한 나머지 값(data)은 수치 data 만 사용함

1. 기본 함수가 평균(mean)함수 이기 때문에 각 데이터의 평균값이 반환 => aggfunc 인자

## groupby

- 그룹 연산 메서드

- 열 또는 열 리스트, 행 인덱스를 인자로 받는다.

- GroupBy 클래스 객체를 반환한다.

## GroupBy 클래스 객체의 그룹 연산 메서드

1. get_group() : 지정한 조건에 맞는 그룹 반환

1. size(), count() : 그룹 데이터의 개수 반환

1. count() : Null 값이 아닌 행만 반환

1. size() : Null 값인 행도 모두 포함해서 반환

1. mean(), median(), min(), max() : 그룹 데이터의 평균, 중앙값, 
최소, 최대 값 반환

1. sum(), prod(), std(),var(), quantile() : 그룹 데이터의 합계, 곱, 표준편차, 분산, 사분위수 반환

1. first(), last() : 그룹 데이터 중 가장 첫 번째, 마지막 데이터 반환

## apply

- 데이터프레임 출력

- 사용자 지정 함수로 연산 가능
