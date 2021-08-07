new_num=1
old_num=0
sum=0
print(old_num)
while sum<50:
    sum = old_num+new_num
    if sum>50:
        break
    print(sum)
    old_num=new_num
    new_num=sum


