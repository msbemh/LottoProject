# Pandas
import pandas as pd
import math

bundle_num = 12

# 1. 로또 데이터를 읽어온다.
# type : DataFrame
lotto_data_csv = pd.read_csv('./lotto.csv')
lotto_data_csv_len = len(lotto_data_csv)
# lotto_data_csv = lotto_data_csv.iloc[2:]

# 내림차순 정렬 - 최신순
lotto_data_csv.sort_index(axis=0, ascending=False)

# print('[TEST]lotto_data_csv:', lotto_data_csv)

# 2. 
# 첫 번째 회차부터 bundle_num 범위까지 묶는다.
# 두 번째 회차부터 bundle_num 범위까지 묶는다.
# ...
# 마지막 - bundle_num 회차부터 bundle_num 범위까지 묶는다.
# 묶은 데이터는 당첨 번호 count값을 구한다.

# 변수할당
number_of_iterations = math.ceil(lotto_data_csv_len / bundle_num)
start = 0
end = bundle_num

aBundleData = []
num = 0
while end <= lotto_data_csv_len:
    # return type : Series
    series_data = lotto_data_csv.iloc[start:end]
  
    # 껍대기 생성
    obj = {
        1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0, 7 : 0, 8 : 0, 9 : 0, 10 : 0, 11 : 0, 12 : 0, 13 : 0, 14 : 0, 15 : 0, 16 : 0, 17 : 0, 18 : 0, 19 : 0, 20 : 0, 21 : 0, 22 : 0, 23 : 0, 24 : 0, 25 : 0, 26 : 0, 27 : 0, 28 : 0, 29 : 0, 30 : 0, 31 : 0, 32 : 0, 33 : 0, 34 : 0, 35 : 0, 36 : 0, 37 : 0, 38 : 0, 39 : 0, 40 : 0, 41 : 0, 42 : 0, 43 : 0, 44 : 0, 45 : 0
    }
    num = num + 1
    obj['번호'] = num

    for item in series_data.iterrows():
        index = item[0]
        data = item[1]

        num1 = data['1번']
        num2 = data['2번']
        num3 = data['3번']
        num4 = data['4번']
        num5 = data['5번']
        num6 = data['6번']
        num7 = data['보너스']
        obj[num1] = obj[num1] + 1
        obj[num2] = obj[num2] + 1
        obj[num3] = obj[num3] + 1
        obj[num4] = obj[num4] + 1
        obj[num5] = obj[num5] + 1
        obj[num6] = obj[num6] + 1
        obj[num7] = obj[num7] + 1

    start += 1
    end += 1

    aBundleData.append(obj)

# print('[TEST]aBundleData:', aBundleData)
aAverage = []
nBundleLength = len(aBundleData)
sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
sum5 = 0
sum6 = 0
sumBonus = 0
obj = {
    0 : {},
    1 : {},
    2 : {},
    3 : {},
    4 : {},
    5 : {},
    6 : {},
    7 : {}
}
for i in range(nBundleLength):
    item = aBundleData[i]
    sum0 = 0
    sum1 = 0
    sum2 = 0
    sum3 = 0
    sum4 = 0
    sum5 = 0
    sum6 = 0
    sum7 = 0
    for j in range(1, 45):
        value = item[j]
        if value == 0:
            sum0 += 1
        elif value == 1:
            sum1 += 1
        elif value == 2:
            sum2 += 1
        elif value == 3:
            sum3 += 1
        elif value == 4:
            sum4 += 1
        elif value == 5:
            sum5 += 1
        elif value == 6:
            sum6 += 1
        elif value == 7:
            sum7 += 1
    
    obj[0][i+1] = sum0
    obj[1][i+1] = sum1
    obj[2][i+1] = sum2
    obj[3][i+1] = sum3
    obj[4][i+1] = sum4
    obj[5][i+1] = sum5
    obj[6][i+1] = sum6
    obj[7][i+1] = sum7
    aAverage.append(obj)

# print('[TEST]aAverage:', aAverage)

# 6. 묶음 데이터를 읽는다.
# 7. 평균(기준)과 묶음 데이터에서의 같은 숫자 반복횟수를 뺀다.
# 8. 가장 차이가 큰 숫자를 가진 번호들에 우선순위 값을 높게 평가한다.
# 9. 차이가 같을 경우, 평균이 높은 곳에 우선순위를 더 높게 평가한다.
# 10. 우선순위에 따라 주머니에 숫자개수를 높여서 넣는다.
# 11. 랜덤으로 뽑느다. (10개)
# 12. 정답과 비교하여 확률이 몇인지 분서한다.
# 13. 묶음 범위를 조정하거나, 숫자개수를 조정하거나, 우선순위 평가하는 방법을 바꿔가며 비교하자.

