import random
from tkinter import*
from tkinter.filedialog import askopenfilename

tk=Tk()
class_list=[]
for i in range(1,5):  # 4개의 반
    score = []  # 반별로 점수를 저장하기 위한 리스트 선언 및 초기화
    sum = 0  # 반별 점수 합 변수 초기화
    class_list.append(score)  # 반별 점수가 담긴 리스트를 다른 리스트로 저장
    for j in range(20):  # 20명이므로 20번 반복해서 난수생성 후 score리스트에 저장
        score.append(random.randint(0, 100))


outfile=open("score.txt","w")
outfile.write(str(class_list))
outfile.close()

def openscore():
    readFile=askopenfilename()
    if(readFile!=None):
        infile=open(readFile,"r")

        def separate():
            tk=Tk()
            # num=[]
            def c1():
                tk=Tk()
                Label(tk,text="1반의 성적").grid(row=0,column=0,pady=10)
                for i in range(20):
                    Label(tk, text=f"{i+1}번").grid(row=1, column=i+1,pady=10)
                    Label(tk, text=class_list[1][i]).grid(row=2, column=i+1,pady=10)
                def upsort():
                    for i in range(20):
                        class_list[1].sort()
                        Label(tk, text=class_list[1][i]).grid(row=3, column=i + 1,pady=10)
                def downsort():
                    for i in range(20):
                        class_list[1].sort(reverse=True)
                        Label(tk, text=class_list[1][i]).grid(row=4, column=i + 1,pady=10)

                def average():
                    sum=0
                    for i in range(20):
                        sum+=class_list[1][i]
                    Label(tk, text=sum/20).grid(row=5, column=1, columnspan=30,pady=10)
                def maxmin():
                    Label(tk, text=f"최고: {max(class_list[1])} 최저: {min(class_list[1])}").grid(row=6, column=1, columnspan=30,pady=10)


                Button(tk, text="오름차순", command=upsort).grid(row=3,column=0,pady=10)
                Button(tk, text="내림차순", command=downsort).grid(row=4,column=0,pady=10)
                Button(tk, text="평균", command=average).grid(row=5,column=0,pady=10)
                Button(tk, text="최고점과 최저점", command=maxmin).grid(row=6,column=0,pady=10)

            #################2반

            def c2():
                tk=Tk()
                Label(tk,text="2반의 성적").grid(row=0,column=0,pady=10)
                for i in range(20):
                    Label(tk, text=f"{i+1}번").grid(row=1, column=i+1,pady=10)
                    Label(tk, text=class_list[2][i]).grid(row=2, column=i+1,pady=10)
                def upsort():
                    for i in range(20):
                        class_list[2].sort()
                        Label(tk, text=class_list[2][i]).grid(row=3, column=i + 1,pady=10)
                def downsort():
                    for i in range(20):
                        class_list[2].sort(reverse=True)
                        Label(tk, text=class_list[2][i]).grid(row=4, column=i + 1,pady=10)

                def average():
                    sum=0
                    for i in range(20):
                        sum+=class_list[1][i]
                    Label(tk, text=sum/20).grid(row=5, column=1, columnspan=30,pady=10)
                def maxmin():
                    Label(tk, text=f"최고: {max(class_list[2])} 최저: {min(class_list[2])}").grid(row=6, column=1, columnspan=30,pady=10)


                Button(tk, text="오름차순", command=upsort).grid(row=3,column=0,pady=10)
                Button(tk, text="내림차순", command=downsort).grid(row=4,column=0,pady=10)
                Button(tk, text="평균", command=average).grid(row=5,column=0,pady=10)
                Button(tk, text="최고점과 최저점", command=maxmin).grid(row=6,column=0,pady=10)

            #################4반

            def c3():
                tk=Tk()
                Label(tk,text="1반의 성적").grid(row=0,column=0,pady=10)
                for i in range(20):
                    Label(tk, text=f"{i+1}번").grid(row=1, column=i+1,pady=10)
                    Label(tk, text=class_list[3][i]).grid(row=2, column=i+1,pady=10)
                def upsort():
                    for i in range(20):
                        class_list[3].sort()
                        Label(tk, text=class_list[3][i]).grid(row=3, column=i + 1,pady=10)
                def downsort():
                    for i in range(20):
                        class_list[3].sort(reverse=True)
                        Label(tk, text=class_list[3][i]).grid(row=4, column=i + 1,pady=10)

                def average():
                    sum=0
                    for i in range(20):
                        sum+=class_list[3][i]
                    Label(tk, text=sum/20).grid(row=5, column=1, columnspan=30,pady=10)
                def maxmin():
                    Label(tk, text=f"최고: {max(class_list[3])} 최저: {min(class_list[3])}").grid(row=6, column=1, columnspan=30,pady=10)


                Button(tk, text="오름차순", command=upsort).grid(row=3,column=0,pady=10)
                Button(tk, text="내림차순", command=downsort).grid(row=4,column=0,pady=10)
                Button(tk, text="평균", command=average).grid(row=5,column=0,pady=10)
                Button(tk, text="최고점과 최저점", command=maxmin).grid(row=6,column=0,pady=10)
#################4반
            def c4():
                tk=Tk()
                Label(tk,text="1반의 성적").grid(row=0,column=0,pady=10)
                for i in range(20):
                    Label(tk, text=f"{i+1}번").grid(row=1, column=i+1,pady=10)
                    Label(tk, text=class_list[4][i]).grid(row=2, column=i+1,pady=10)
                def upsort():
                    for i in range(20):
                        class_list[4].sort()
                        Label(tk, text=class_list[4][i]).grid(row=3, column=i + 1,pady=10)
                def downsort():
                    for i in range(20):
                        class_list[4].sort(reverse=True)
                        Label(tk, text=class_list[4][i]).grid(row=4, column=i + 1,pady=10)

                def average():
                    sum=0
                    for i in range(20):
                        sum+=class_list[4][i]
                    Label(tk, text=sum/20).grid(row=5, column=1, columnspan=30,pady=10)
                def maxmin():
                    Label(tk, text=f"최고: {max(class_list[4])} 최저: {min(class_list[4])}").grid(row=6, column=1, columnspan=30,pady=10)


                Button(tk, text="오름차순", command=upsort).grid(row=3,column=0,pady=10)
                Button(tk, text="내림차순", command=downsort).grid(row=4,column=0,pady=10)
                Button(tk, text="평균", command=average).grid(row=5,column=0,pady=10)
                Button(tk, text="최고점과 최저점", command=maxmin).grid(row=6,column=0,pady=10)






            c1=Button(tk,text="1반",command=c1)
            c2=Button(tk,text="2반",command=c2)
            c3=Button(tk,text="3반",command=c3)
            c4=Button(tk,text="4반",command=c4)

            c1.pack(padx=20,pady=10)
            c2.pack(padx=20,pady=10)
            c3.pack(padx=20,pady=10)
            c4.pack(padx=20,pady=10)



        def all():
            print("hdd")

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
