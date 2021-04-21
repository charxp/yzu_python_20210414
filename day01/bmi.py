
i = input('請輸入身高 (例如:170) + Enter：')
j = input('請輸入體重 (例如:50) + Enter：')

family_data = [
    ['Dad', 181, 80],
    ['Mom', 160, 80],
    ['Kid_1',117,25],
    ['Kid_2',100,21],
    ['my_bmi',float(i),float(j)]
]

for each_one in family_data:
    this_bmi = each_one[2] / ((each_one[1] / 100) ** 2)
    each_one.append(this_bmi)

for each_one in family_data:
    if each_one[3] < 18.5:
        bmi_index = '體重過輕'
    elif 18.5 <= each_one[3] < 24.0:
        bmi_index = '正常範圍'
    elif 24.0 <= each_one[3] < 27.0:
        bmi_index = '體重過重'
    elif 27.0 <= each_one[3] < 30.0:
        bmi_index = '輕度肥胖'
    elif 30.0 <= each_one[3] < 35.0:
        bmi_index = '中度肥胖'
    else:
        bmi_index = '重度肥胖'
    each_one.append(bmi_index)

for each_one in family_data:
    if each_one[4] == '正常範圍':
        is_normal = True
    else:
        is_normal = False
    each_one.append(is_normal)

print(each_one)