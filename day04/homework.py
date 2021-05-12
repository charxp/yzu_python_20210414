# print ２－１００ 質數
#判斷2到100之間，哪些是質數

for i in range(2,101):
    s=0
    for j in range(1,i+1):
        if i%j==0:
            s+=1
    if s==2:
        print ("質數=%2d" % (i),end=" ")
