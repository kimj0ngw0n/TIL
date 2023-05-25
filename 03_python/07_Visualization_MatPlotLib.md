# Matplotlib

```python
import matplotlib.pyplot as plt
%matplotlib inline
```

## 그래프 관련 함수 및 속성

1. figure(x,y) : 그래프 크기 설정 : 단위 인치

1. title() : 제목 출력

1. xlim(범위값): x 축 범위

1. ylim(범위값) : y 축 범위

1. xticks()/yticks() : 축과 값을 잇는 실선 (눈금)

1. legend() : 범례

1. xlabel() : x축라벨(값)

1. ylabel() : y축라벨(값)

1. grid() : 그래프 배경으로 grid 사용 결정 함수

## line plot에서 자주 사용되는 스타일 속성 (약자로도 표기 가능)

1. color : c (선색상)

1. linewidth : lw (선 굵기)

1. linestyle : ls (선스타일)

1. marker : 마커 종류

1. markersize : ms (마커크기)

1. markerfacecolor : mfc (마커 내부 색상)

1. markeredgecolor : mec (마커 테두리 색상)

1. markeredgewidth : mew (마커 테두리 굵기)

## 선 스타일

1. `-` solid(default)

1. `--` dashed

1. `:` dotted

1. `-.` dashdot

## 마커 유형

1. `+`

1. `o`

1. `*`

1. `.` 점

1. `x` 십자

1. `s` 정사각형

1. `d` 다이아몬드

1. `^` 위쪽 방향 삼각형

1. `v` 아래쪽 방향 삼각형

1. `>` 오른쪽 방향 삼각형

1. `<` 왼쪽 방향 삼각형

1. `p` 오각별(펜타그램)

1. `h` 팔각별(헥사그램)

## subplot

- 화면을 분할하여 여러 개의 그래프를 출력

- `subplot(인수1, 인수2, 인수3)` 또는 `subplot(인수1인수2인수3)`

- 인수1, 2 : 전체 그리드 행렬의 모양 지시 (2행 3열)

- 인수3 : 그래프 위치 순서 번호

- tight_layout(pad=간격값(실수)) : 플롯 간 간격 설정

## plt.subplots(행, 열)

```python
fig, axes = plt.subplots(2, 2)

axes[0, 0].plot(np.random.rand(5))

#...
```

## 범례(legend) 표시

- `plt.legend(loc=, ncol=)`

- loc : 범례 표시 위치 값

    - 0 ~ 10 또는 best, right, left, center... 로 설정

- ncol : 열의 개수

- 범례 표시를 위해 plot에 label 속성이 추가되어 있어야 한다.

## 막대 그래프 : `bar() / barh()`

- `bar(x, y, color=, alpha=)`

- color=[] : 색상 값 설정

- alpha : 투명도 설정

## 산점도 : `scatter()`

- `plt.colorbar()` 와 같이 사용 가능

## 히스토그램 : `hist()`

## 박스 그래프 : `boxplot()`

## 파이 차트 : `pie()`
