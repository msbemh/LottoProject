# Pandas
import pandas as pd
import math
import random

bundle_num = 12
price = 1000
purchase_count = 100000

# ==========[ 로또 데이터 Read ]==========
# type : DataFrame
lotto_data_csv = pd.read_csv('./lotto.csv')
lotto_data_csv_len = len(lotto_data_csv)
# 내림차순 정렬 - 최신순
lotto_data_csv.sort_index(axis=0, ascending=False)

# ==========[ 데이터 정리 ]==========
# Object - 회차별 당첨 번호
# key - 회차
# value - 정보(추첨일, 당첨번호)
oTurnInfo = {}
for item in lotto_data_csv.iterrows():
    index = item[0]
    data = item[1]
    oTurnInfo[data['회차']] = [
        data['1번'],
        data['2번'],
        data['3번'],
        data['4번'],
        data['5번'],
        data['6번'],
        data['보너스']
    ]

# Array - Object 리스트
# Object - bundle_num 횟수 동안 당첨 번호별 중복 개수
# key - 당첨 번호
# value - 중복 개수
aBundleData = []
number_of_iterations = math.ceil(lotto_data_csv_len / bundle_num)
start = 0
end = bundle_num
num = 0

# Object - aBundleData의 번호와 회차를 매핑하기 위한 오브젝트
# key - 번호
# value - 회차
# Index = 번호 - 1
oTurnNumMapping = {}
while end <= lotto_data_csv_len:
    # return type : Series
    series_data = lotto_data_csv.iloc[start:end]

    obj = {
        1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0, 21: 0, 22: 0, 23: 0, 24: 0, 25: 0, 26: 0, 27: 0, 28: 0, 29: 0, 30: 0, 31: 0, 32: 0, 33: 0, 34: 0, 35: 0, 36: 0, 37: 0, 38: 0, 39: 0, 40: 0, 41: 0, 42: 0, 43: 0, 44: 0, 45: 0
    }
    # 번호 넘버링
    num = num + 1
    oTurnNumMapping[series_data['회차'].iloc[0]] = num

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

# Object - 중복 개수별 당첨번호 개수
nBundleLength = len(aBundleData)
sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
sum5 = 0
sum6 = 0
sumBonus = 0
oBundleSame = {
    0: {},
    1: {},
    2: {},
    3: {},
    4: {},
    5: {},
    6: {},
    7: {}
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
    for j in range(1, 46):
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

    oBundleSame[0][i+1] = sum0
    oBundleSame[1][i+1] = sum1
    oBundleSame[2][i+1] = sum2
    oBundleSame[3][i+1] = sum3
    oBundleSame[4][i+1] = sum4
    oBundleSame[5][i+1] = sum5
    oBundleSame[6][i+1] = sum6
    oBundleSame[7][i+1] = sum7

# Object - 중복 개수별 당첨 개수 평균
oAverage = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0
}
for sameNum, innerObj in oBundleSame.items():
    sum = 0
    for key, value in innerObj.items():
        sum += value
    oAverage[sameNum] = round(sum/len(innerObj.keys()), 1)

# ==========[ 테스트 ]==========
predict_turn = int(input("예측할 회차 번호를 입력하세요: "))
inspect_turn = int(predict_turn) - 1
inspect_num = oTurnNumMapping[inspect_turn]
inspect_index = inspect_num - 1

inspect_data = aBundleData[inspect_index]
# print('inspect_data:', inspect_data)

# Object - 중복 개수별 당첨번호 리스트
oSameNum = {
    0: [],
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: []
}
for key, value in inspect_data.items():
    oSameNum[value].append(key)

# ==========[ 계산 ]==========
# 차이 : 개당 10점
# 평균 : 개당 1점
# 점수가 높을 수록 당첨될 확률이 높음
oDifference = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0
}
oScore = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0
}
for key, value in oDifference.items():
    oDifference[key] = abs(
        round(oAverage[key] - oBundleSame[key][inspect_num], 0))
    oScore[key] = oDifference[key] ** 4 + oAverage[key] * 1

sum = 0
for key, value in oScore.items():
    sum += oScore[key]

# Object - 중복범위에서 당첨될 확률
oPercentage = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0
}
for key, value in oPercentage.items():
    oPercentage[key] = round(oScore[key]/sum * 100, 0)


# 중복된 데이터일 경우 Recursive
def select_choice_num(choice_same, ticket):
    temp = [0, 1, 2, 3, 4, 5, 6]
    if len(oSameNum[choice_same[0]]) == 0:
        choice_num = random.choices(temp)
    else:
        choice_num = random.choices(oSameNum[choice_same[0]])

    if choice_num[0] in ticket:
        choice_same = random.choices([0, 1, 2, 3, 4, 5, 6, 7], [
            oPercentage[0], oPercentage[1], oPercentage[2], oPercentage[3], oPercentage[4], oPercentage[5], oPercentage[6], oPercentage[7]])
        choice_num = select_choice_num(choice_same, ticket)
    return choice_num


# purchase_count 번 복권 구입
total_expenditure = 0
tickets = []
temps = []
for i in range(purchase_count):
    ticket = []
    temp = []
    # 중복 범위 번호 확률에 따른 랜덤 추출
    for j in range(7):
        choice_same = random.choices([0, 1, 2, 3, 4, 5, 6, 7], [
            oPercentage[0], oPercentage[1], oPercentage[2], oPercentage[3], oPercentage[4], oPercentage[5], oPercentage[6], oPercentage[7]])

        temp.append(choice_same[0])

        choice_num = select_choice_num(choice_same, ticket)
        ticket.append(choice_num[0])
        ticket.sort()

    tickets.append(ticket)
    temps.append(temp)
    total_expenditure -= price


# print('tickets:', tickets)
# print('total_expenditure:', total_expenditure)
# ==========[ 결과 확인 ]==========
oAnswer = oTurnInfo[predict_turn][0:6]
nAnswerBonus = oTurnInfo[predict_turn][6]
print('정답 : ', oAnswer)
# print('temps : ', temps)
# print('nAnswerBonus : ', nAnswerBonus)
answerCount = 0
rank = '꽝'
oRank = {
    '꽝': 0,
    '1등': 0,
    '2등': 0,
    '3등': 0,
    '4등': 0,
    '5등': 0,
}
for item in tickets:
    ticket = item[0:6]
    nTicketBonus = item[6]
    for index, value in enumerate(ticket):
        if value in oAnswer:
            answerCount += 1

    if answerCount == 3:
        rank = '5등'
        total_expenditure += 5000
    elif answerCount == 4:
        rank = '4등'
        total_expenditure += 50000
    elif answerCount == 5:
        if nTicketBonus == nAnswerBonus:
            rank = '2등'
            total_expenditure += 50000000
        else:
            rank = '3등'
            total_expenditure += 1500000
    elif answerCount == 6:
        rank = '1등'
        total_expenditure += 2740000000

    oRank[rank] += 1
    # print(ticket, ':', oAnswer, ':', rank)

    answerCount = 0
    rank = '꽝'

print('oRank:', oRank)
print('지갑:', total_expenditure)
