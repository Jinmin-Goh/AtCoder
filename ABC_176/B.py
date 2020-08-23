n = input()
ans = 0
for i in n:
    ans += int (i) 
    ans %= 9

if ans == 0:
    print("Yes")
else:
    print("No")