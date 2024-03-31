num=list(map(int,input(' '),spilt()))

avg = sum(num) / len(num)

check = 0

for i in num:
    if i >= avg:
        check=check+1

print(avg)
print(check)
