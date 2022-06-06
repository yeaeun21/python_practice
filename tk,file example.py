import random
from tkinter import*
from tkinter.filedialog import askopenfilename

tk=Tk()
class_list=[]
for i in range(4):  # 4개의 반
    score = []  # 반별로 점수를 저장하기 위한 리스트 선언 및 초기화
    sum = 0  # 반별 점수 합 변수 초기화
    class_list.append(score)  # 반별 점수가 담긴 리스트를 다른 리스트로 저장
    for j in range(20):  # 20명이므로 20번 반복해서 난수생성 후 score리스트에 저장
        score.append(random.randint(0, 100))


outfile=open("score.txt","w") #score.txt파일에 저장
outfile.write(str(class_list)) #str형태로만 저장 가능
outfile.close()

#학급별 통계 함수
def openscore():
    readFile=askopenfilename()
    if(readFile!=None):
        infile=open(readFile,"r")

        def separate():
            tk=Tk()
##############################1반
            def c1():
                tk=Tk()
                Label(tk,text="1반의 성적").grid(row=0,column=0,pady=10)
                #20명의 학생들의 점수 출력
                for i in range(20):
                    Label(tk, text=f"{i+1}번").grid(row=1, column=i+1,pady=10) #1번부터 20번 text를 1번째 행의 1~20번째 열에 출력, y축으로 여백10만큼 줌
                    Label(tk, text=class_list[0][i]).grid(row=2, column=i+1,pady=10) #1번부터 20번의 점수를 2번째 행의 1~20번째 열에 출력, y축으로 여백10만큼 줌
                #오름차순 출력 함수
                def upsort():
                    for i in range(20):
                        class_list[0].sort() #sort()함수로 오름차순으로 list를 정리
                        Label(tk, text=class_list[0][i]).grid(row=3, column=i + 1,pady=10) #오름차순된 list값을 출력해서 3번째 행의 1~20번째 열에 출력, y축으로 여백10만큼 줌
                #내림차순 출력 함수
                def downsort():
                    for i in range(20):
                        class_list[0].sort(reverse=True) #sort()함수로 오름차순 된 리스트 값을 reverse=True로서 역전
                        Label(tk, text=class_list[0][i]).grid(row=4, column=i + 1,pady=10) #내림차순된 list값을 출력해서 4번째 행의 1~20번째 열에 출력, y축으로 여백10만큼 줌
                #평균 출력 함수
                def average():
                    sum=0 #리스트의 모든 값을 더한 값을 담을 변수sum 초기화
                    for i in range(20): #20명의 점수를 모두 더함
                        sum+=class_list[0][i]
                    Label(tk, text=sum/20).grid(row=5, column=1, columnspan=30,pady=10) #sum을 20으로 나눠 평균출력 후 5번째 행의 1번째 30만큼 영역 차지하는 열에 출력
                #최대값 최소값 출력 함수
                def maxmin(): #max,min함수 이용
                    Label(tk, text=f"최고: {max(class_list[0])} 최저: {min(class_list[0])}").grid(row=6, column=1, columnspan=30,pady=10)

                #오름차순,내림차순,평균,최고최소 구할 수 있는 버튼 생성
                Button(tk, text="오름차순", command=upsort).grid(row=3,column=0,pady=10)
                Button(tk, text="내림차순", command=downsort).grid(row=4,column=0,pady=10)
                Button(tk, text="평균", command=average).grid(row=5,column=0,pady=10)
                Button(tk, text="최고점과 최저점", command=maxmin).grid(row=6,column=0,pady=10)

            #################2반

            def c2():
                tk = Tk()
                Label(tk, text="2반의 성적").grid(row=0, column=0, pady=10)
                # 20명의 학생들의 점수 출력
                for i in range(20):
                    Label(tk, text=f"{i + 1}번").grid(row=1, column=i + 1,pady=10)  # 1번부터 20번 text를 1번째 행의 1~20번째 열에 출력, y축으로 여백10만큼 줌
                    Label(tk, text=class_list[1][i]).grid(row=2, column=i + 1,pady=10)  # 1번부터 20번의 점수를 2번째 행의 1~20번째 열에 출력, y축으로 여백10만큼 줌

                # 오름차순 출력 함수
                def upsort():
                    for i in range(20):
                        class_list[1].sort()  # sort()함수로 오름차순으로 list를 정리
                        Label(tk, text=class_list[1][i]).grid(row=3, column=i + 1,
                                                              pady=10)  # 오름차순된 list값을 출력해서 3번째 행의 1~20번째 열에 출력, y축으로 여백10만큼 줌

                # 내림차순 출력 함수
                def downsort():
                    for i in range(20):
                        class_list[1].sort(reverse=True)  # sort()함수로 오름차순 된 리스트 값을 reverse=True로서 역전
                        Label(tk, text=class_list[1][i]).grid(row=4, column=i + 1,
                                                              pady=10)  # 내림차순된 list값을 출력해서 4번째 행의 1~20번째 열에 출력, y축으로 여백10만큼 줌

                # 평균 출력 함수
                def average():
                    sum = 0  # 리스트의 모든 값을 더한 값을 담을 변수sum 초기화
                    for i in range(20):  # 20명의 점수를 모두 더함
                        sum += class_list[1][i]
                    Label(tk, text=sum / 20).grid(row=5, column=1, columnspan=30,
                                                  pady=10)  # sum을 20으로 나눠 평균출력 후 5번째 행의 1번째 30만큼 영역 차지하는 열에 출력

                # 최대값 최소값 출력 함수
                def maxmin():  # max,min함수 이용
                    Label(tk, text=f"최고: {max(class_list[1])} 최저: {min(class_list[1])}").grid(row=6, column=1,
                                                                                              columnspan=30, pady=10)

                # 오름차순,내림차순,평균,최고최소 구할 수 있는 버튼 생성
                Button(tk, text="오름차순", command=upsort).grid(row=3, column=0, pady=10)
                Button(tk, text="내림차순", command=downsort).grid(row=4, column=0, pady=10)
                Button(tk, text="평균", command=average).grid(row=5, column=0, pady=10)
                Button(tk, text="최고점과 최저점", command=maxmin).grid(row=6, column=0, pady=10)

            #################3반

            def c3():
                tk = Tk()
                Label(tk, text="3반의 성적").grid(row=0, column=0, pady=10)
                # 20명의 학생들의 점수 출력
                for i in range(20):
                    Label(tk, text=f"{i + 1}번").grid(row=1, column=i + 1,
                                                     pady=10)  # 1번부터 20번 text를 1번째 행의 1~20번째 열에 출력, y축으로 여백10만큼 줌
                    Label(tk, text=class_list[2][i]).grid(row=2, column=i + 1,
                                                          pady=10)  # 1번부터 20번의 점수를 2번째 행의 1~20번째 열에 출력, y축으로 여백10만큼 줌

                # 오름차순 출력 함수
                def upsort():
                    for i in range(20):
                        class_list[2].sort()  # sort()함수로 오름차순으로 list를 정리
                        Label(tk, text=class_list[2][i]).grid(row=3, column=i + 1,
                                                              pady=10)  # 오름차순된 list값을 출력해서 3번째 행의 1~20번째 열에 출력, y축으로 여백10만큼 줌

                # 내림차순 출력 함수
                def downsort():
                    for i in range(20):
                        class_list[2].sort(reverse=True)  # sort()함수로 오름차순 된 리스트 값을 reverse=True로서 역전
                        Label(tk, text=class_list[2][i]).grid(row=4, column=i + 1,
                                                              pady=10)  # 내림차순된 list값을 출력해서 4번째 행의 1~20번째 열에 출력, y축으로 여백10만큼 줌

                # 평균 출력 함수
                def average():
                    sum = 0  # 리스트의 모든 값을 더한 값을 담을 변수sum 초기화
                    for i in range(20):  # 20명의 점수를 모두 더함
                        sum += class_list[2][i]
                    Label(tk, text=sum / 20).grid(row=5, column=1, columnspan=30,
                                                  pady=10)  # sum을 20으로 나눠 평균출력 후 5번째 행의 1번째 30만큼 영역 차지하는 열에 출력

                # 최대값 최소값 출력 함수
                def maxmin():  # max,min함수 이용
                    Label(tk, text=f"최고: {max(class_list[2])} 최저: {min(class_list[2])}").grid(row=6, column=1,
                                                                                              columnspan=30, pady=10)

                # 오름차순,내림차순,평균,최고최소 구할 수 있는 버튼 생성
                Button(tk, text="오름차순", command=upsort).grid(row=3, column=0, pady=10)
                Button(tk, text="내림차순", command=downsort).grid(row=4, column=0, pady=10)
                Button(tk, text="평균", command=average).grid(row=5, column=0, pady=10)
                Button(tk, text="최고점과 최저점", command=maxmin).grid(row=6, column=0, pady=10)
#################4반
            def c4():
                tk = Tk()
                Label(tk, text="4반의 성적").grid(row=0, column=0, pady=10)
                # 20명의 학생들의 점수 출력
                for i in range(20):
                    Label(tk, text=f"{i + 1}번").grid(row=1, column=i + 1,pady=10)  # 1번부터 20번 text를 1번째 행의 1~20번째 열에 출력, y축으로 여백10만큼 줌
                    Label(tk, text=class_list[3][i]).grid(row=2, column=i + 1,pady=10)  # 1번부터 20번의 점수를 2번째 행의 1~20번째 열에 출력, y축으로 여백10만큼 줌

                # 오름차순 출력 함수
                def upsort():
                    for i in range(20):
                        class_list[3].sort()  # sort()함수로 오름차순으로 list를 정리
                        Label(tk, text=class_list[3][i]).grid(row=3, column=i + 1,
                                                              pady=10)  # 오름차순된 list값을 출력해서 3번째 행의 1~20번째 열에 출력, y축으로 여백10만큼 줌

                # 내림차순 출력 함수
                def downsort():
                    for i in range(20):
                        class_list[3].sort(reverse=True)  # sort()함수로 오름차순 된 리스트 값을 reverse=True로서 역전
                        Label(tk, text=class_list[3][i]).grid(row=4, column=i + 1,
                                                              pady=10)  # 내림차순된 list값을 출력해서 4번째 행의 1~20번째 열에 출력, y축으로 여백10만큼 줌

                # 평균 출력 함수
                def average():
                    sum = 0  # 리스트의 모든 값을 더한 값을 담을 변수sum 초기화
                    for i in range(20):  # 20명의 점수를 모두 더함
                        sum += class_list[3][i]
                    Label(tk, text=sum / 20).grid(row=5, column=1, columnspan=30,
                                                  pady=10)  # sum을 20으로 나눠 평균출력 후 5번째 행의 1번째 30만큼 영역 차지하는 열에 출력

                # 최대값 최소값 출력 함수
                def maxmin():  # max,min함수 이용
                    Label(tk, text=f"최고: {max(class_list[3])} 최저: {min(class_list[3])}").grid(row=6, column=1,
                                                                                              columnspan=30, pady=10)

                # 오름차순,내림차순,평균,최고최소 구할 수 있는 버튼 생성
                Button(tk, text="오름차순", command=upsort).grid(row=3, column=0, pady=10)
                Button(tk, text="내림차순", command=downsort).grid(row=4, column=0, pady=10)
                Button(tk, text="평균", command=average).grid(row=5, column=0, pady=10)
                Button(tk, text="최고점과 최저점", command=maxmin).grid(row=6, column=0, pady=10)






            c1=Button(tk,text="1반",command=c1)
            c2=Button(tk,text="2반",command=c2)
            c3=Button(tk,text="3반",command=c3)
            c4=Button(tk,text="4반",command=c4)

            c1.pack(padx=20,pady=10)
            c2.pack(padx=20,pady=10)
            c3.pack(padx=20,pady=10)
            c4.pack(padx=20,pady=10)


#전체통계 함수
        def all():
            tk=Tk()
            all_s=[]
            a_sum=0
            count = 0 #득점자수를 센 값을 넣을 변수 초기화
            count20 = 0
            count40 = 0
            count60 = 0
            count80 = 0
            Label(tk, text="1반").grid(row=1, column=0, pady=10)
            Label(tk, text="2반").grid(row=2, column=0, pady=10)
            Label(tk, text="3반").grid(row=3, column=0, pady=10)
            Label(tk, text="4반").grid(row=4, column=0, pady=10)

            for i in range(20):
                Label(tk, text=f"{i + 1}번").grid(row=0, column=i + 1, pady=10)  # 1번부터 20번 text를 1번째 행의 1~20번째 열에 출력, y축으로 여백10만큼 줌
                Label(tk, text=class_list[0][i]).grid(row=1, column=i + 1,pady=10)  # 1번부터 20번의 점수를 2번째 행의 1~20번째 열에 출력, y축으로 여백10만큼 줌
                Label(tk, text=class_list[1][i]).grid(row=2, column=i + 1, pady=10)
                Label(tk, text=class_list[2][i]).grid(row=3, column=i + 1, pady=10)
                Label(tk, text=class_list[3][i]).grid(row=4, column=i + 1, pady=10)
            for i in range(4):
                for j in class_list[i]:
                    all_s.append(j)

            for j in all_s:
                a_sum+=j
                if (0<=j and j<20):
                    count+=1
                    Label(tk, text=f"0점 보다 크거나 같고 20점 보다 작은 점수 득점자 수:{count}").grid(row=0, column=21, padx=5, pady=10)
                elif (20<=j and j<40):
                    count20+=1
                    Label(tk, text=f"20점 보다 크거나 같고 40점 보다 작은 점수 득점자 수:{count20}").grid(row=1, column=21, padx=5, pady=10)
                elif (40 <= j and j < 60):
                    count40 += 1
                    Label(tk, text=f"40점 보다 크거나 같고 60점 보다 작은 점수 득점자 수:{count40}").grid(row=2, column=21, padx=5, pady=10)
                elif (60 <= j and j < 80):
                    count60 += 1
                    Label(tk, text=f"60점 보다 크거나 같고 80점 보다 작은 점수 득점자 수:{count60}").grid(row=3, column=21, padx=5, pady=10)
                elif (80 <= j and j <= 100):
                    count80 += 1
                    Label(tk, text=f"80점 보다 크거나 같고 100점 보다 작거나 같은 점수 득점자 수:{count80}").grid(row=4, column=21, padx=5, pady=10)
            Label(tk, text=f"평균:{a_sum/80}").grid(row=5, column=21, columnspan=30, pady=10)
            Label(tk, text=f"최고점: {max(all_s)}, 최저점: {min(all_s)}").grid(row=6, column=21,columnspan=30, pady=10)
        tk = Tk()
        separate = Button(tk, text="학습별통계", command=separate)
        all = Button(tk, text="전체통계", command=all)

        separate.pack(padx=10, pady=20)
        all.pack(padx=10, pady=20)

        infile.close()



openscore=Button(tk,text="학생성적 열람",command=openscore)
label=Label(tk,text="주의! 띄어쓰기로 구분 된 score.txt파일만 정상 실행됩니다.")
openscore.pack(padx=100, pady=20)
label.pack(pady=50)
tk.mainloop()
