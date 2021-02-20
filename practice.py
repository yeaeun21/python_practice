# # print(5+3)
# # print(2*8)
# # print(3*(3+1))
# # print("ㅋ"*9)
# # #참 / 거짓
# # print(5>10)
# # print(5<10)
# # print(True)
# # print(not True)
# # #변수
# # #애완 동물 소개
# # animal = "강아지"
# # name= "몽이"
# # age= 12
# # hobby="산책"
# # is_adult = age >=3

# # print("우리집"+animal+ "는"+name)
# # #print(name+"는"+str(age)+"살, 취미는" + hobby) 
# # print(name, "는", age, "살, 취미는",  hobby)
# #  #---> +로 연결시에는 정수를 문자열로 바꿔줘야 하므로 str필수고 ,로 연결시에는 안해도됨 대신 ,옆에 자동 띄어쓰기 됨
# # print(name+"는 어른일까요?"+ str(is_adult))

# #연산자
# print(2**3) #2^3=8
# print(5%3) #나머지 구하기 2
# print(5//3) #몫 1
# print(1 != 3) #1과 3은 같지 않다
# print(not(1!=3)) #false

# #and와 &은 둘 다, or는 둘 중 하나

# #숫자처리함수
# abs 절대값
# pow(4,2) 4의 2승
# max(a,b) 둘중 큰거 출력
# min(a,b) 둘중 작은거
# round 반올림

# from math import *
# print(floor(4.99)) #내림 4
# print(ceil(3.14)) #올림. 4
# print(squrt(16))#제곱근.4

# 랜덤함수

# print(random()) #0.0~1.0 미만의 임의의 값 생성
# print(random()*10) #0.0~10.0 미만의 임의의 값 생성
# print(int(random()*10)) #0~10 미만의 임의의 값 생성
# print(int(random()*10+1)#1~10 이하의 임의의 값 생성
# print(int(random()*45 +1) #1~45 이하의 임의의 값 생성
# print(randrange(1,46))#1이상 46미만의 임의의 값 생성
#1이상 45이하의 임의의 값 생성
from random import *
date = randint(4, 28)
print("이렇게도"+str(date)+"돼요")

sentence = '나는 소녀입니다'
print(sentence)
sentence2="파이썬은 쉽다"
print(sentense3)
sentence3="""
이렇게도,
할수있어요.
"""
print(sentence3)

#슬라이싱

jumin = "990908-2134567"

print("성별:"+ jumin[7])#7번째 값 가져옴
print("연 : "+jumin[0:2])#0부터 2 직전까지 (0~1까지)
print("월 : "+ jumin[2:4])

print("생년월일 : "+jumin[:6])# 처음부터 6직전까지
print("뒤 7자리 :"+jumin[7:])#7번째 부터 끝까지
print("뒤 7자리 (뒤에서 부터 계산)"+jumin[-7:])
#맨뒤에서 7번째부터 끝까지 

문자열처리함수
python = "python is Amazing"
print(python.lower())#소문자로 출력
print(pyhon.upper())#대문자로 출력
print(python[0].isupper())#0번째가 대문자인지?
print(len(python))#문자열의 길이
print(python.replace("python", "Java")) #문자열안의 python을 Java로 교체

index = python.index("n")#python이라는 변수에서 n이 몇번째
print(index) #5
index = python.index("n",index +1) #두번째 n의 위치
print(index)#15

print(python.find("n"))
# n의 위치 차이점>없는 문자는 마이너스반환, index는 오류나면서 프로그램 종료
print("hi")#find면 -1찍고 출력, index면 오류나서 출력안됨

print(python.count("n"))#n이 총 몇번나오는지

<문자열포맷>
방법1
print("나는 %d살 입니다." % 20)
print("나는 %s을 좋아해요." % "파이썬")# d,c,다됨
print("Apple은 %c로 시작해요" % "A")
print("나는 %s 색과 %s색을 좋아해요" %("파란","빨간"))

방법2
print("나는 {}살입니다." .format(20))
print("나는 {} 색과 {}색을 좋아해요" .format("파란","빨간"))
print("나는 {1} 색과 {0}색을 좋아해요" .format("파란","빨간"))
#순번에 맞게 출력> 빨간색과 파란색

방법3
print("나는 {age}살이며, {color}색을 좋아해요" .format(age=20,color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요" .format(color="빨간",age=20))

방법4 (v3.6이상)
age=20
color="빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

<탈출문자>
print("백문이 불여일견 \n백견이 불여일타") #줄바꿈
print('나는 "예은"입니다')
print("나는 \"예은\"입니다.")#문장내에서 따옴표

#\\ : 문장 내에서 \
print("\\Users\\User\\Desktop\\코딩")

#\r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")

#\b : 백스페이스 (한글자 삭제)
print("Redd\bApple")

#\t: 탭
print("Red\tApple")