//원

str_input = float(input("원의 반지름 입력>"))
num_input = float(str_input)
print()
print("반지름", num_input)
print("둘레",2* 3.14 * num_input)
print("넓이:", 3.14 * num_input **2)

//시간

import datetime
now = datetime.datetime.now()
if now.hour < 12 :
    print("현재 시간은{}시 {}분으로 오전입니다".format(now.hour,now.minute))
if now.hour >= 12 :
    print("현재 시간은{}시 {}분으로 오전입니다".format(now.hour,now.minute))

# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)

//성적

score = float(input("성적을 입력해주세요>>>"))

if score == 4.5 :
    print("신")
elif 4.2<= score :
    print("교수님의 사랑")

elif 3.5<= score :
    print("현 체제의 수호자")

elif 2.8<= score :
    print("일반인")

elif 2.3<= score :
    print("일탈을 꿈꾸는 소시민")

elif 1.75< score :
    print("오락문화의 선구자")

elif 1.0 <= score :
    print("불가촉천민")

elif 0.5 <= score :
    print("자벌레")

elif 0 <= score  :
    print("플랑크톤")

else :
    print("시대를 앞서가는 혁명가")

# numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
# output = [[],[],[]]

# for number in numbers :
#     output[number%3].append(number)
# print(output)

number_1 = [273, 103, 5, 32, 65, 9, 72, 800, 99]

holzzak = ["짝수", "홀수"]
for number in number_1:
    print("{}는 {} 입니다.".format(number, holzzak[number % 3]))