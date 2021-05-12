import random as r
ans = r.randint(1, 99)
min = 0
max = 100
count = 5
<<<<<<< HEAD
while True:
    guess = int(input('請輸入 %d ~ %d 之間:' % (min, max)))
=======
while count > 0:
    guess = int(input('(%d). 請輸入 %d ~ %d : ' % (count, min, max)))
>>>>>>> python_yzu
    # 檢查 guess 的資料是否在 min 與 max 之間 ?
    if guess <= min or guess >= max:
        print('數字範圍錯誤')
        continue
<<<<<<< HEAD
=======
    # 將 count 減去一次
    count = count - 1
    # 判定結果
>>>>>>> python_yzu
    if guess > ans:
        max = guess
    elif guess < ans:
        min = guess
    else:
        print('答對了')
        break