#
#
n=-4365
str1=str(n)
str2=''
l=len(str1)
for i in str1:
    if i.isdigit():
        str2=i+str2
    else:
        pass

print(str2)
print('*'*40)
a = 2
b = 5
a,b = b,a
print(a,b)