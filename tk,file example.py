import random
from tkinter import*
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

tk=Tk()
class_list=[]
for i in range(4):  # 4개의 반
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

            def cl(cn):
                if (cn==1):
                    print("dd")


            c1=Button(tk,text="1반",command=cl(1))
            c2=Button(tk,text="2반",command=cl(2))
            c3=Button(tk,text="3반",command=cl(3))
            c4=Button(tk,text="4반",command=cl(4))

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
