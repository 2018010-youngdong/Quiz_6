r_num=input('주민번호 13자리를 입력하세요 (-제외) : ')
product=[2,3,4,5,6,7,8,9,2,3,4,5]
sum=0
for i in range(12):
    sum += int(r_num[i])*product[i]
x=(11-(sum%11))%10
y=int(r_num[12])

print(x)
print(y)
if x==y:
    print('유효합니다')
else:
    print('유효하지 않습니다')
