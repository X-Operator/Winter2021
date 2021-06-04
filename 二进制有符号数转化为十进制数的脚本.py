a = input()
l = len(a)
ans = 0 
for i in range(l):
    if(i == 0):
        ans = ans - int(a[i])*pow(2,l-i-1)
    else:
        ans = ans + int(a[i])*pow(2,l-i-1)
print(ans)
        
