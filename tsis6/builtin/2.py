s = input()
upper = 0
lower = 0
for i in range (len(s)):
     if(s[i].isupper()):
       upper += 1
     if(s[i].islower()):
       lower += 1

print('Upper letters:', upper)
print('Upper letters:', lower)


